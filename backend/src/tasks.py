#from typing import Protocol
#from abc import abstractmethod
import sys, inspect
import random

MAX_TASK_ATTEMPTS = 3

def get_2_ints(_from: int = 1, _to: int = 10) -> list[int]:
    if _from > _to: _from, _to = _to, _from
    return [random.randint(_from, _to), random.randint(_from, _to)]

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
        a = random.randint(1,10)
        b = random.randint(1,10)
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
        self.x = a * b
        self.y = b
        self.z = a

    def new_task(self):
        return random.randint(1, 10), random.randint(1, 10)

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

class PlusMinusBis10(Task):
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


## WHY is this not working anymore?
## not even with 
##    tasks[cls.__name__] = cls(*cls.new_task(cls))
tasks = {}
for cls in Task.__subclasses__():
    tasks[cls.__name__] = cls()

def choose_task(task):
    tasks_here = {
        "kleines_1x1": kleines_1x1(
            random.randint(1, 10), 
            random.randint(1, 10)
        ),
        "Division": Division(
            random.randint(1,10),
            random.randint(1,10)
        ),
        "PlusMinusBis10": PlusMinusBis10()
    }
    return tasks_here[task]

all_tasks = tuple((cls.__name__, True) for cls in Task.__subclasses__())

print(all_tasks)