import random 
from collections.abc import Callable
from dataclasses import asdict, dataclass
from enum import StrEnum
from typing import Any, Self


class TaskType(StrEnum):
	MULTIPLY = 'multiply'
	DIVIDE = 'divide'
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

	def check(self, num: int) -> bool:
		return num == self.result

	def to_dict(self) -> dict[str, Any]:
		return {**asdict(self), 'expr': str(self)}

def multiply(a: int, b: int) -> Task:
	return Task(a, b, a * b, '*')

def divide(a: int, b: int) -> Task:
	return Task(a * b, b, a, '/')

TASKS: dict[TaskType, Callable[[int, int], Task]] = {
	TaskType.MULTIPLY: multiply, 
	TaskType.DIVIDE: divide, 
}

_TASK_TYPES = tuple(TASKS.keys())

def choose_task(task_type: TaskType) -> Task:
	if task_type is TaskType.RANDOM:
		task_type = random.choice(_TASK_TYPES)

	a = random.randint(1, 10) 
	b = random.randint(1, 10)

	return TASKS[task_type](a, b)
