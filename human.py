from __future__ import annotations
from typing import Union
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

        self.parents: dict[str: Union[Human, None]] = {'father': None, 'mother': None}
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

    def edit_name(self, name: str):
        self.name = name.title()

    def edit_surname(self, surname: str, new: bool = False):
        self.surname = surname.title()
        if new: self.all_surnames.append(self.surname)

    def edit_lastname(self, lastname: str):
        self.lastname = lastname.title()

    def edit_born_time(self, born_time: tuple[int, int, int]):
        self.born_time = born_time

    def edit_die_time(self, die_time: tuple[int, int, int]):
        self.die_time = die_time

    def edit_gender(self, gender: str):
        self.gender = gender

    def edit_parents(self, human: Human):
        t = ["mother", "father"][human.gender == "man"]
        self.parents[t] = human
        if self not in human.children:
            human.edit_children(self)

    def edit_partner(self, partner: Human, other: bool = True):
        self.partner = partner
        self.all_partners.append(self.partner)
        if other: partner.edit_partner(self, False)

    def edit_children(self, child: Human):
        self.children.append(child)
        t = ["mother", "father"][self.gender == "man"]
        child.parents[t] = self


    def edit_biography(self, biography: str):
        self.biography = biography


    # ВЫВОД ИНФОРМАЦИИ

    def get_all_name(self):
        return f"{self.surname} {self.name} {self.lastname}"

    def get_born_time(self):
        return (f"{self.born_time[2]:0>2}."
                f"{self.born_time[1]:0>2}."
                f"{self.born_time[1]}")

    def get_die_time(self):
        if self.die_time:
            return (f"{self.die_time[2]:0>2}."
                    f"{self.die_time[1]:0>2}."
                    f"{self.die_time[1]}")
        return "нет"

    def try_get_human(self, human: Union[Human, None]) -> str:
        if human is None: return ""
        return human.get_all_name()

    def get_all_children(self):
        if len(self.children) == 0: return ""

        text = "\n"
        for child in self.children:
            text += f"- {child.get_all_name()}\n"

        return text

    def show_human_info(self):
        text_info = (f"{self.get_all_name()}\n"
        f"Пол: {self.gender}\n"
        f"Дата рождения: {self.get_born_time()}\n"
        f"Дата смерти: {self.get_die_time()}\n"
        f"Возраст: {self.age} полных лет\n"
        f"Родители:\n"
        f"  Отец: {self.try_get_human(self.parents['father'])}\n"
        f"  Мать: {self.try_get_human(self.parents['mother'])}\n"
        f"\n{(lambda: 'Жена' if self.gender == 'man' else 'Муж')()}: {self.try_get_human(self.partner)}\n"
        f"Дети: {self.get_all_children()}\n")


        return text_info
