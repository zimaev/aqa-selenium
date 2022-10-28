import random
from itertools import product
import os
from data.data import Person, Color, Date
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


def generated_color():
    yield Color(
        color_name=['Red', 'Blue', 'Green',
                    'Yellow', 'Purple', 'Black',
                    'White', 'Voilet', 'Indigo',
                    'Magenta', 'Aqua']
                )


def generated_date():
    yield Date(
        year=str(random.randint(2017, 2027)),
        month=fake_en.month_name(),
        day=fake_ru.day_of_month(),
        time=random.choice([f"{h:02d}:{m:02d}" for h,m in product(range(24), range(0, 60, 15))])
    )

