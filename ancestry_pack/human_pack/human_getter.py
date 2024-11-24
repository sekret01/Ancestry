from ..human_pack import Human
from typing import Union

class HumanGetter:
    """
    Возвращает информацию о человеке.
    Любая функция принимает в качестве параметра человека
    """
    def get_all_name(self, human: Human) -> str:
        """Полное имя человека"""
        return f"{human.surname} {human.name} {human.lastname}"

    def get_born_time(self, human: Human) -> str:
        return (f"{human.born_time[2]:0>2}."
                f"{human.born_time[1]:0>2}."
                f"{human.born_time[0]}")

    def get_die_time(self, human: Human) -> str:
        if human.die_time:
            return (f"{human.die_time[2]:0>2}."
                    f"{human.die_time[1]:0>2}."
                    f"{human.die_time[0]}")
        return "нет"

    def try_get_human(self, human: Union[Human, None]) -> str:
        """
        Пытается получить имя человека.
        Если человек = None -> ''
        """
        if human is None: return ""
        return self.get_all_name(human)

    def get_all_children(self, human: Human) -> str:
        if len(human.children) == 0: return ""
        text = "\n"
        for child in human.children:
            text += f"- {self.get_all_name(child)}\n"
        return text

    def get_biography(self, human: Human) -> str:
        return human.biography

    def get_human_info(self, human: Human) -> str:
        """Полная информация о человеке без биографии"""
        text_info = (f"{self.get_all_name(human)}\n"
        f"Пол: {human.gender}\n"
        f"Дата рождения: {self.get_born_time(human)}\n"
        f"Дата смерти: {self.get_die_time(human)}\n"
        f"Возраст: {human.age} полных лет\n"
        f"Родители:\n"
        f"  Отец: {self.try_get_human(human.parents['father'])}\n"
        f"  Мать: {self.try_get_human(human.parents['mother'])}\n"
        f"\n{(lambda: 'Жена' if human.gender == 'man' else 'Муж')()}: {self.try_get_human(human.partner)}\n"
        f"Дети: {self.get_all_children(human)}\n")

        return text_info