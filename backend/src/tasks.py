import random 
from collections.abc import Callable
from dataclasses import asdict, dataclass
from enum import StrEnum
from fractions import Fraction
from math import gcd
from typing import Any, Self


class TaskType(StrEnum):
	ADD = 'add'
	SUBTRACT = 'subtract'
	DIVIDE = 'divide'
	MULTIPLY = 'multiply'
	REDUCE = 'reduce'
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
	result: int| Fraction
	op: str

	def __str__(self) -> str:
		return f'{self.left} {self.op} {self.right}'

	def check(self, value: str) -> bool:
		try:
			value = value.strip()

			target = self.result

			if '/' in value:
				numerator_str, denominator_str = value.split('/', maxsplit=1)
				numerator = int(numerator_str.strip())
				denominator = int(denominator_str.strip())

				if denominator <= 0:
					return False

				if gcd(abs(numerator), denominator) != 1:
					return False

				answer = Fraction(numerator, denominator)
			else:
				answer = int(value)

			return answer == target
		except ValueError:
			return False

	def to_dict(self) -> dict[str, Any]:
		def serialize(value: Any) -> Any:
			if isinstance(value, Fraction):
				return str(value)
			return value

		return {
			**{key: serialize(value) for key, value in asdict(self).items()},
			'expr': str(self),
		}

def add(a: int, b: int) -> Task:
	return Task(a, b, a + b, '+')

def subtract(a: int, b: int) -> Task:
	return Task(a, b, a - b, '-')

def divide(a: int, b: int) -> Task:
	return Task(a * b, b, a, '/')

def multiply(a: int, b: int) -> Task:
	return Task(a, b, a * b, '*')

def reduce_fraction(a: int, b: int) -> Task:
	return Task(a, b, Fraction(a, b), '/')

TASKS: dict[TaskType, Callable[[int, int], Task]] = {
	TaskType.ADD: add, 
	TaskType.SUBTRACT: subtract,
	TaskType.DIVIDE: divide, 
	TaskType.MULTIPLY: multiply, 
	TaskType.REDUCE: reduce_fraction, 
}

_TASK_TYPES = tuple(TASKS.keys())

def _generate_numbers(task_type: TaskType) -> tuple[int, int]:
	match task_type:
		case TaskType.ADD:
			a = random.randint(1, 99)
			b = random.randint(1, 100 - a)
			return a, b
		case TaskType.SUBTRACT:
			a = random.randint(2, 100)
			b = random.randint(1, a)
			return a, b
		case TaskType.REDUCE:
			divisor = random.randint(2, 10)
			numerator = random.randint(1, 10)
			denominator = random.randint(2, 10)
			return numerator * divisor, denominator * divisor
		case TaskType.MULTIPLY | TaskType.DIVIDE:
			a = random.randint(1, 10) 
			b = random.randint(1, 10)
			return a, b
		case _:
			raise ValueError(f'Unsupported task type: {task_type}')

def choose_task(task_type: TaskType) -> Task:
	if task_type is TaskType.RANDOM:
		task_type = random.choice(_TASK_TYPES)

	a, b = _generate_numbers(task_type)
	return TASKS[task_type](a, b)
