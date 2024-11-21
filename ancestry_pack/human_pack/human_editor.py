from ..human_pack import Human

class HumanEditor:
    """
    Изменение параметров человека.
    Каждая функция принимает аргументом человека
    """
    def edit_name(self, human: Human, name: str) -> None:
        human.name = name.title()

    def edit_surname(self, human: Human, surname: str, new: bool = False) -> None:
        human.surname = surname.title()
        if new: human.all_surnames.append(human.surname)

    def edit_lastname(self, human: Human, lastname: str) -> None:
        human.lastname = lastname.title()

    def edit_born_time(self, human: Human, born_time: tuple[int, int, int]) -> None:
        human.born_time = born_time

    def edit_die_time(self, human: Human, die_time: tuple[int, int, int]) -> None:
        human.die_time = die_time

    def edit_gender(self, human: Human, gender: str) -> None:
        human.gender = gender

    def edit_parents(self, human: Human, parent: Human) -> None:
        """
        Меняет родителя человека;
        У родителя вызывает функцию добавления human в список детей

        :param human: (Human) человек, кому назначается родитель;
        :param parent: (Human) родитель
        :return: None
        """
        t = ["mother", "father"][parent.gender == "man"]
        human.parents[t] = parent
        if human not in parent.children:
            self.edit_children(human=parent, child=human)

    def edit_partner(self, human: Human,  partner: Human, other: bool = True) -> None:
        """
        Редактирование партнера (other) у human;
        Вызывается функция смены партнера у other

        :param human: человек
        :param partner: партнер человека (human)
        :param other: проверка на второй вызов функции для партнера
        :return: None
        """
        human.partner = partner
        human.all_partners.append(human.partner)
        if other: self.edit_partner(human=partner, partner=human, other=False)

    def edit_children(self, human: Human, child: Human) -> None:
        human.children.append(child)
        t = ["mother", "father"][human.gender == "man"]
        child.parents[t] = human

    def edit_biography(self, human: Human, biography: str) -> None:
        human.biography = biography
