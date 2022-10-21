import random
from unittest.mock import patch
import os
from data.data import Person
from faker import Faker


fake_ru = Faker("ru_RU")
fake_en = Faker("en_US")
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
        mobile=fake_ru.msisdn(),
        current_address=fake_ru.address(),
        permanent_address=fake_ru.address(),
        birth_date=str(fake_ru.date_of_birth())

    )


def generated_file():
     path = os.path.abspath(f"test_{fake_ru.file_name(category='text')}")
     file = open(path, "w+")
     file.write(f'{fake_ru.paragraph(nb_sentences=2)}')
     file.close()
     return path


