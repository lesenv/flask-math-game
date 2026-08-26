import secrets, string, random
from tasks import choose_task, all_tasks
import json

try:
    with open("./backend/src/saves.json", "r") as js:
        all_users = [str(name) for name in json.load(js).keys()]
except KeyError:
        all_users = None
print(f"IN MODELS.PY: all_users = {all_users}")

class User:
    def __init__(self, sid, username, points=0):
        self._sid = sid
        self._username = username
        self._points = points
        self._saved_tasks = self._get_saved_tasks()

    def _get_saved_tasks(self):
        try:
            with open("./backend/src/saves.json", "r") as js:
                saved_tasks = json.load(js)[self._username]["enabled_tasks"]
        except KeyError:
            saved_tasks = None
        return saved_tasks

    @property
    def saved_tasks(self):
        return self._saved_tasks

    @property
    def sid(self):
        return self._sid
    
    @property
    def username(self):
        return self._username
    
    @property
    def points(self):
        return self._points
    
    @points.setter
    def points(self, value):
        self._points = value

    def remove(self):
        del self.__class__.all_users[self.sid]

    all_users = {}

    @classmethod
    def create(cls, sid, username, points=0):
        obj = cls(sid, username, points)
        cls.all_users[sid] = obj
        return obj

    @classmethod
    def find_by_sid(cls, sid):
        return cls.all_users.get(sid)

    @classmethod
    def find_by_username(cls, username):
        for v in cls.all_users.values():
            if v.username == username:
                return v
        return None


MAX_ROOM_MEMBERS = 1
MAX_TASK_ATTEMPTS = 3

class Room:
    def __init__(self, code):
        self._code = code
        self._members = {}
        self.won = False

    def __len__(self):
        return len(self._members)
    
    @property
    def code(self):
        return self._code

    @property
    def is_closed(self):
        return not self.is_open

    @property
    def is_empty(self):
        return len(self) == 0

    @property
    def is_open(self):
        return len(self) < MAX_ROOM_MEMBERS

    def add_member(self, user):
        self._members[user.sid] = user

    def is_member(self, user):
        return user.sid in self._members

    def remove_member(self, user):
        del self._members[user.sid]

    def remove(self):
        del self.__class__.all_rooms[self.code]

    all_rooms = {}

    @classmethod
    def create(cls):
        key = cls.generate_room_code()
        obj =  cls(key)
        cls.all_rooms[key] = obj
        return obj

    @classmethod
    def generate_room_code(cls, size=8):
        alphanum = string.ascii_letters + string.digits
        return ''.join(secrets.choice(alphanum) for _ in range(size))

    @classmethod
    def find_by_code(cls, code):
        return cls.all_rooms.get(code)

    @classmethod
    def find_open_room(cls):
        for v in cls.all_rooms.values():
            if v.is_open: 
                return v
        return None

MAX_TASK_ATTEMPTS = 3
MAX_ROUNDS = 10

class Match(Room):
    def __init__(self, code):
        super().__init__(code)
        self._attempts = 0
        self._task = None
        self._enabled_tasks = dict(all_tasks)

    @property
    def enabled_tasks(self):
        return self._enabled_tasks
    
    def apply_tasks(self, task_bools):
        for t,v in task_bools.items():
            self._enabled_tasks[t] = v

        # if no task is chosen, take a default one
        if all(not v for _, v in task_bools.items()):
            self._enabled_tasks[self._enabled_tasks[0]] = True
    
    @property
    def is_current_task_enabled(self):
        return self._enabled_tasks[type(self._task).__name__]

    @property
    def attempts(self):
        return self._attempts

    @attempts.setter
    def attempts(self, value):
        self._attempts = value

    def create_task(self):
        available_tasks = [t for t,s in self.enabled_tasks.items() if s]
        task = random.choice(available_tasks)
        self._task = choose_task(task)
        return self._task

    def process(self, num):
        success = self._task.check(num)
        if success:
            self._task = self.create_task()
            self.attempts = 0
        else:
            self.attempts += 1 
            if self.attempts >= MAX_TASK_ATTEMPTS:
                self._task = self.create_task()
                self.attempts = 0 
        return self._task, self.attempts, success

    def reset_points(self):
        for m in self._members.values():
            m.points = 0
