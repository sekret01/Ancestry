from ancestry_pack.input_formatters import form
from ancestry_pack.human_pack import Human, HumanGetter, HumanEditor


class Ancestry:
    """
    Список людей, связанных между собой

    """
    def __init__(self):
        self.human_list: list[Human] = []
        self.getter = HumanGetter()
        self.editor = HumanEditor()

    def add_human(self, human: Human) -> None:
        try:
            self.human_list.append(human)
        except Exception as ex:
            _ = input(ex)

    def get_all_humans(self) -> str:
        text = ''
        for i, human in enumerate(self.human_list, 1):
            text += f"{i} - {self.getter.get_all_name(human=human)}\n"
        return text
