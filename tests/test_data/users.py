from dataclasses import dataclass
from enum import Enum
from typing import Tuple


class Subject(Enum):
    History = 'History'
    Maths = 'Maths'
    Physics = 'Physic'


class Hobby(Enum):
    Sports = '1'
    Reading = '2'
    Music = '3'


class Gender(Enum):
    Male = 'Male'
    Female = 'Female'
    Other = 'Other'


@dataclass
class User:
    gender: Gender
    name: str
    last_name: str = 'Romanova'
    email: str = 'elena@mail.ru'
    mobile: str = '1234567891'
    birth_day: str = '30'
    birth_month: str = 'March'
    birth_year: str = '1995'
    subjects: Tuple[Subject] = (Subject.History, Subject.Maths, )
    hobbies: Tuple[Hobby] = (Hobby.Sports, Hobby.Reading)
    current_address: str = 'Astana'
    picture_file: str = 'photo.jpg'
    state: str = 'Haryana'
    city: str = 'Karnal'


elena = User(name='Elena', gender=Gender.Female)
