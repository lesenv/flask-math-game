import random, secrets, string
from tasks import Task, TaskType, choose_task
from typing import Any, ClassVar, Self


class User:
	def __init__(self, sid: str, username: str, points: int = 0) -> None:
		self._sid = sid
		self._username = username
		self._points = points

	@property
	def sid(self) -> str:
		return self._sid
	
	@property
	def username(self) -> str:
		return self._username
	
	@property
	def points(self) -> int:
		return self._points
	
	@points.setter
	def points(self, value: int) -> None:
		self._points = value

	def remove(self) -> None:
		type(self).all_users.pop(self.sid, None)

	all_users: ClassVar[dict[str, User]] = {}

	@classmethod
	def create(cls, sid: str, username: str, points: int=0) -> Self:
		obj = cls(sid, username, points)
		cls.all_users[sid] = obj
		return obj

	@classmethod
	def find_by_sid(cls, sid: str) -> User | None:
		return cls.all_users.get(sid)

	@classmethod
	def find_by_username(cls, username: str) -> User | None:
		return next((u for u in cls.all_users.values() if u.username == username), None)

MAX_ROOM_MEMBERS = 2

class Room:

	# Separate based on the subclass.
	# def __init_subclass__(cls, **kwargs: Any) -> None:
	# 	super().__init_subclass__(**kwargs)
	# 	cls.all_rooms = {}

	def __init__(self, code: str) -> None:
		self._code = code
		self._members: dict[str, User] = {} 

	def __len__(self) -> int:
		return len(self._members)

	@property
	def code(self) -> str:
		return self._code

	@property
	def is_closed(self) -> bool:
		return not self.is_open

	@property
	def is_empty(self) -> bool:
		return len(self) == 0

	@property
	def is_open(self) -> bool:
		return len(self) < MAX_ROOM_MEMBERS

	@property
	def task_type(self) -> TaskType:
		raise NotImplementedError

	def add_member(self, user: User) -> None:
		self._members[user.sid] = user

	def is_member(self, user: User) -> bool:
		return user.sid in self._members

	def remove_member(self, user: User) -> None:
		self._members.pop(user.sid, None)

	def remove(self) -> None:
		type(self).all_rooms.pop(self.code, None)

	all_rooms: ClassVar[dict[str, Any]] = {}

	@classmethod
	def create(cls, *args: Any, **kwargs: Any) -> Self:
		key = cls.generate_room_code()
		obj =  cls(key, *args, **kwargs)
		cls.all_rooms[key] = obj
		return obj

	@classmethod
	def generate_room_code(cls, size: int=8) -> str:
		alphanum = string.ascii_letters + string.digits
		return ''.join(secrets.choice(alphanum) for _ in range(size))

	@classmethod
	def find_by_code(cls, code: str) -> Self | None:
		return cls.all_rooms.get(code)

	@classmethod
	def find_open_room(cls) -> Self | None:
		return next((r for r in cls.all_rooms.values() if r.is_open), None)

	@classmethod
	def find_open_room_by_type(cls, task_type: TaskType) -> Self | None:
		return next(
			(r for r in cls.all_rooms.values() if r.task_type == task_type and r.is_open), 
			None
		)


MAX_TASK_ATTEMPTS = 3

class Match(Room):
	def __init__(self, code: str, task_type: TaskType=TaskType.RANDOM) -> None:
		super().__init__(code)
		self._attempts = 0
		self._task: Task | None = None 
		self._task_type = task_type

	@property
	def attempts(self) -> int:
		return self._attempts

	@property
	def task_type(self) -> TaskType:
		return self._task_type
	
	def create_task(self) -> Task:
		self._task = choose_task(self._task_type)
		return self._task

	def process(self, value: str) -> tuple[Task, int, bool]:
		if self._task is None:
			self.create_task()

		success = self._task.check(value)
		if success:
			self._task = self.create_task()
			self._attempts = 0
		else:
			self._attempts += 1 
			if self.attempts >= MAX_TASK_ATTEMPTS:
				self._task = self.create_task()
				self._attempts = 0 

		return self._task, self.attempts, success

	def reset_points(self) -> None:
		for m in self._members.values():
			m.points = 0
