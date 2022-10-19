from dataclasses import dataclass


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


