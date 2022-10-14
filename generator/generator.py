import random

from data.data import Person
from faker import Faker


fake_ru = Faker("ru_RU")
Faker.seed()


def generated_person():
    yield Person(
        first_name=fake_ru.first_name(),
        last_name=fake_ru.last_name(),
        full_name=f"{fake_ru.first_name()} {fake_ru.last_name()} {fake_ru.middle_name()}",
        age=random.randint(10, 80),
        department=fake_ru.job(),
        salary=random.randint(30000, 130000),
        email=fake_ru.email(),
        current_address=fake_ru.address(),
        permanent_address=fake_ru.address()
    )

