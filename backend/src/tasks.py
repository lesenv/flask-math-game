import random

MAX_TASK_ATTEMPTS = 3

class Task():
    ''' parent class for all the different Tasks available
    '''

class kleines_1x1(Task):
    def __init__(self, a = None, b = None):
        if not a:
            a = random.randint(1,10)
        if not b:
            b = random.randint(1,10)
        self.a = a
        self.b = b
        self.c = a * b

    def new_task(self):
        a, b = random.randint(1, 10), random.randint(1, 10)
        self.__init__(a, b)
        return a, b

    def string(self):
        return f"{self.a} * {self.b}"

    def check(self, num):
        return num == self.c

    def _asdict(self):
        return {
            'a': self.a,
            'b': self.b,
            'c': self.c,
            'str': self.string()
        }

class Division(Task):
    def __init__(self, a = None, b = None):
        if not a:
            a = random.randint(1,10)
        if not b:
            b = random.randint(1,10)
        self._assign_self_variables(a, b)

    def _assign_self_variables(self, a, b):
        self.x = a * b
        self.y = b
        self.z = a

    def new_task(self):
        a, b = random.randint(1, 10), random.randint(1, 10)
        self._assign_self_variables(a, b)
        return a, b

    def string(self):
        return f"{self.x} / {self.y}"

    def check(self, num):
        return num == self.z

    def _asdict(self):
        return {
            'a': self.x,
            'b': self.y,
            'c': self.z,
            'str': self.string()
        }

class plus_bis_10(Task):
    def __init__(self, c = None, b = None):
        if not c:
            c = random.randint(1,10)
        if not b:
            b = random.randint(1,c)
        self.a = c-b
        self.b = b
        self.c = c

    def new_task(self):
        c = random.randint(1,10)
        b = random.randint(1,c)
        self.__init__(c, b)
        return c, b

    def string(self):
        return f"{self.a} + {self.b}"

    def check(self, num):
        return num == self.c

    def _asdict(self):
        return {
            'a': self.a,
            'b': self.b,
            'c': self.c,
            'str': self.string()
        }

class plus_bis_100(plus_bis_10, Task):
    def __init__(self, c=None, b=None):
        super().__init__(c = random.randint(1,100))

class minus_bis_20(plus_bis_10, Task):
    def __init__(self, c=None, b=None):
        super().__init__(c = random.randint(1,20))

    def string(self):
        return f"{self.c} - {self.b}"
    
    def check(self, num):
        return num == self.a
    
tasks_class = {cls.__name__: cls() for cls in Task.__subclasses__()}
all_tasks = tuple((cls.__name__, True) for cls in Task.__subclasses__())

def choose_task(task):
    tasks_class[task].new_task()
    return tasks_class[task]
