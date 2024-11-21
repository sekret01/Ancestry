from __future__ import annotations
from typing import Union, Type
import datetime

ONE_YEAR = 365

class Human:
    """
    Описание человека, его связей с другими людьми в роду

    формат даты: (ГГ, ММ, ДД)
    """
    def __init__(self,
                 name: str,
                 surname: str,
                 lastname: str,
                 born_time: tuple[int, int, int],
                 die_time: Union[tuple[int, int, int], None],
                 gender: str):

        self.name: str = name.title()
        self.surname: str = surname.title()
        self.lastname: str = lastname.title()
        self.all_surnames: list[str] = []

        self.born_time: tuple[int, int, int] = born_time
        self.die_time: Union[tuple[int, int, int], None] = die_time
        self.age: int = 0
        self.cause_of_death: Union[str, None] = None

        self.gender: str = gender

        self.parents: dict[str, Union[Human, None]] = {'father': None, 'mother': None}
        self.children: list[Human] = []
        self.partner: Union[Human, None] = None
        self.all_partners: list[Human] = []

        self.biography: str = ""

        self.count_age()

    def count_age(self):
        """Автоматический подсчет возраста"""
        if self.die_time is None:
            date_now = datetime.datetime.now()
            tuple_date_now = datetime.date(date_now.year, date_now.month ,date_now.day)
            age = tuple_date_now - datetime.date(*self.born_time)
            self.age = age.days // ONE_YEAR

        else:
            born_time = datetime.date(*self.born_time)
            die_time = datetime.date(*self.die_time)
            age = die_time - born_time
            self.age = age.days // ONE_YEAR

