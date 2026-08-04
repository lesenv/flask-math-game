from typing import Protocol
from abc import abstractmethod
import random

MAX_TASK_ATTEMPTS = 3

def get_2_ints(_from: int = 1, _to: int = 10) -> list[int]:
    if _from > _to: _from, _to = _to, _from
    return [random.randint(_from, _to), random.randint(_from, _to)]

class _Task(Protocol):
    symbol: str
    
    @abstractmethod
    def check(self) -> int:
        ...

class Multiply(_Task):
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.c = a * b

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

class Division(_Task):
    def __init__(self, a, b):
        self.x = a * b
        self.y = b
        self.z = a

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

def choose_task():
    if Multiply:
        return Division(
                    random.randint(1, 10), 
                    random.randint(1, 10))
    return _Task
        