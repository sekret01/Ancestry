from ancestry_pack import Ancestry
from ancestry_pack import Loader
from ancestry_pack import Saver
from ancestry_pack import Human
from ancestry_pack import HumanGetter
from ancestry_pack import HumanEditor
from menu import Menu
from typing import Any
import os

getter = HumanGetter()
editor = HumanEditor()


def clear():
    os.system('cls')



# VIEW MENU FUNCTIONS
def show_all_people(anc: Ancestry):
    clear()
    all_people = anc.get_all_humans()
    print(all_people)
    _ = input()


def show_one_human(anc: Ancestry, ind: int) -> None:
    if ind < 0 or ind > len(anc.human_list)-1:
        input(f"Не существует человека под номером [{ind+1}]")
        return
    human: Human = anc.human_list[ind]
    info = getter.get_human_info(human)
    biography = getter.get_biography(human)

    add_biography = '2'

    while add_biography in ['1', '2']:
        clear()
        if add_biography == '2':
            print(info)
            add_biography = input("\n[1 - показать биографию]\n\n# ")
        if add_biography == '1':
            print(info, end='\n\n')
            print(biography, )
            add_biography = input("\n[2 - скрыть биографию]\n\n# ")


def get_info_about_human(anc: Ancestry):
    input_text = ''
    clear()
    try:
        input_text = input("Введите номер человека в списке\n     ]\r[")
        ind = int(input_text)
        show_one_human(anc, ind-1)
    except ValueError:
        input(f"Ошибка ввода: [{input_text}] не является числом")
        return


def search_people(anc: Ancestry, human_info: list[str]) -> list[tuple[int, str]]:
    result_human_info = []
    for item in human_info:
        if item:
            result_human_info.append(item)

    search_list = []
    for human in anc.human_list:
        add = 1
        all_name = getter.get_all_name(human=human)
        for item in result_human_info:
            if item not in all_name: add = 0
        if add:
            search_list.append((anc.human_list.index(human)+1, all_name))
    return search_list


def setting_search_people(anc: Ancestry):
    clear()
    print("Введите данные, по которым будет проводиться поиск\n(Пропуск - любое значение)\n")
    name = input("   имя: ")
    surname = input("   фамилия: ")
    lastname =input("   отчество: ")

    search_list = search_people(anc, [name, surname, lastname])

    clear()
    print(f"  Совпадения с [{name} {surname} {lastname}]\n")
    for el in search_list:
        print(f"{el[0]:>5} - {el[1]}")
    input()




# VIEW MENU
def commands_view_menu(anc: Ancestry, command: int) -> bool:
    if command == 1:
        show_all_people(anc)
    if command == 2:
        get_info_about_human(anc=anc)
    if command == 3:
        setting_search_people(anc=anc)
    if command == 4:
        return False
    return True


def view_menu(anc: Ancestry) -> None:

    menu_commands = ["Весь список людей", "Просмотр информации о человеке", "Поиск людей", "Назад"]
    menu = Menu(commands=menu_commands, left_indent=4, top_indent=1)
    loop = True

    while loop:
        com = menu.run()
        loop = commands_view_menu(anc, com)



# EDIT MENU FUNCTIONS



# EDIT MENU
def commands_edit_menu(anc: Ancestry, command: int) -> bool:
    if command == 1:
        ...
    if command == 2:
        ...
    if command == 3:
        return False
    return True


def edit_menu(anc: Ancestry) -> None:
    menu_commands = ["Добавить человека", "Редактировать данные человека", "Назад"]
    menu = Menu(commands=menu_commands, left_indent=4, top_indent=1)
    loop = True

    while loop:
        com = menu.run()
        loop = commands_edit_menu(anc=anc, command=com)



# MAIN LOOP
def commands_main_loop(anc: Ancestry, command: int) -> bool:
    if command == 1:
        view_menu(anc=anc)
    if command == 2:
        edit_menu(anc=anc)
    if command == 3:
        return False
    return True


def main_loop(anc: Ancestry):

    menu_commands = ["Просмотр людей", "Редактирование дерева", "Выход"]
    menu = Menu(commands=menu_commands, left_indent=4, top_indent=1)
    loop = True

    while loop:
        com = menu.run()
        loop = commands_main_loop(anc=anc, command=com)




# SAVE - LOAD DATA
def save_data(anc: Ancestry) -> None:
    saver = Saver()
    saver.save(anc)


def load_data() -> tuple[Any, str]:
    loader = Loader()
    try:
        anc = loader.load()
        if type(anc) is Ancestry:
            return anc, "Загрузка успешна"
        return Ancestry(), f"В файле {loader.path} отсутствуют данные.\nСоздана новая база хранения"

    except Exception as ex:
        return Ancestry(), f"{str(ex)}\nСоздана новая база хранения"


# MAIN
def main():
    clear()
    anc, message = load_data()
    _ = input(message)

    main_loop(anc)

    clear()
    print("Сохранение данных...")
    save_data(anc=anc)


if __name__ == '__main__':
    main()
