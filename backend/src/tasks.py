import random 
from collections.abc import Callable
from dataclasses import asdict, dataclass
from enum import StrEnum
from typing import Any, Self


class TaskType(StrEnum):
	ADD = 'add'
	SUBTRACT = 'subtract'
	DIVIDE = 'divide'
	MULTIPLY = 'multiply'
	RANDOM = 'random'

	@classmethod
	def from_string(cls, stype: str) -> Self | None:
		try: 
			return cls(stype.lower()) 
		except ValueError: 
			return None

@dataclass(frozen=True)
class Task:
	left: int
	right: int
	result: int
	op: str

	def __str__(self) -> str:
		return f'{self.left} {self.op} {self.right}'

	def check(self, value: str) -> bool:
		try:
			value = value.strip()
			return self.result == int(value)
		except ValueError:
			return False

	def to_dict(self) -> dict[str, Any]:
		return {**asdict(self), 'expr': str(self)}

def add(a: int, b: int) -> Task:
	return Task(a, b, a + b, '+')

def subtract(a: int, b: int) -> Task:
	return Task(a, b, a - b, '-')

def divide(a: int, b: int) -> Task:
	return Task(a * b, b, a, '/')

def multiply(a: int, b: int) -> Task:
	return Task(a, b, a * b, '*')

TASKS: dict[TaskType, Callable[[int, int], Task]] = {
	TaskType.ADD: add, 
	TaskType.SUBTRACT: subtract,
	TaskType.DIVIDE: divide, 
	TaskType.MULTIPLY: multiply, 
}

_TASK_TYPES = tuple(TASKS.keys())

def choose_task(task_type: TaskType) -> Task:
	if task_type is TaskType.RANDOM:
		task_type = random.choice(_TASK_TYPES)

	match task_type:
		case TaskType.ADD:
			a = random.randint(1, 99)
			b = random.randint(1, 100 - a)
		case TaskType.SUBTRACT:
			a = random.randint(2, 100)
			b = random.randint(1, a)
		case _:
			a = random.randint(1, 10) 
			b = random.randint(1, 10)

	return TASKS[task_type](a, b)
