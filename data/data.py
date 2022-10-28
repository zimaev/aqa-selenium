from dataclasses import dataclass
from datetime import datetime


@dataclass()
class Person:
    first_name: str = None
    last_name: str = None
    full_name: str = None
    email: str = None
    mobile: int = None
    age: int = None
    birth_date: str = None
    salary: int = None
    department: str = None
    current_address: str = None
    permanent_address: str = None


@dataclass()
class Color:
    color_name: list = None


@dataclass()
class Date:
    day: str = None
    month: str = None
    year: str = None
    time: str = None

