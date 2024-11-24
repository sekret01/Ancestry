from os import access

from ancestry_pack import Ancestry
from ancestry_pack import Loader
from ancestry_pack import Saver
from ancestry_pack import Human
from ancestry_pack import HumanGetter
from ancestry_pack import HumanEditor
from ancestry_pack import form
from ancestry_pack import valid_date
from menu import Menu
from typing import Any
import os

getter = HumanGetter()
editor = HumanEditor()


def clear():
    os.system('cls')


def get_human_index_in_list():
    input_text = ''
    try:
        input_text = input("Введите номер человека в списке\n     ]\r[")
        ind = int(input_text)
        return ind
    except ValueError:
        input(f"Ошибка ввода: [{input_text}] не является числом")
        return -1


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
        elif add_biography == '1':
            print(info, end='\n\n')
            print(biography, )
            add_biography = input("\n[2 - скрыть биографию]\n\n# ")


def get_info_about_human(anc: Ancestry):
    clear()
    ind = get_human_index_in_list()
    if ind != -1: show_one_human(anc, ind - 1)


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
def add_human(anc: Ancestry):
    clear()
    new_human = form()
    if new_human is None:
        return
    anc.add_human(new_human)
    clear()
    input("Человек был успешно добавлен")


def edit_name(human: Human):
    clear()
    new_name = input("Новое имя: ")
    editor.edit_name(human=human, name=new_name)
    input("Новое имя записано")


def edit_surname(human: Human):
    clear()
    new_surname = input("(При смене фамилии: [new <фамилия>])\n\nНовая фамилия: ")
    if len(new_surname.split(' ')) == 2 and new_surname.split(' ')[0] == "new":
        editor.edit_surname(human=human, surname=new_surname, new=True)
    else:
        editor.edit_surname(human=human, surname=new_surname)
    input("Новая фамилия записано")


def edit_lastname(human: Human):
    clear()
    new_lastname = input("Новое отчество: ")
    editor.edit_lastname(human=human, lastname=new_lastname)
    input("Новое отчество записано")


def edit_born_time(human: Human):
    new_born_time = input("Дата рождения: ")
    new_valid_born_time = valid_date(new_born_time)
    if new_valid_born_time != (0, 0, 0):
        editor.edit_born_time(human=human, born_time=new_valid_born_time)
        input("Дата рождения изменена")
        return
    input(f"Некорректная дата [{new_born_time}]")
    return


def edit_die_time(human: Human):
    new_die_time = input("Дата смерти: ")
    if new_die_time == "":
        editor.edit_die_time(human=human, die_time=None)
        input("Дата смерти сброшена")
        return
    new_valid_die_time = valid_date(new_die_time)
    if new_valid_die_time != (0, 0, 0):
        editor.edit_die_time(human=human, die_time=new_valid_die_time)
        input("Дата смерти изменена")
        return
    input(f"Некорректная дата [{new_die_time}]")
    return


def edit_parent(human: Human, anc: Ancestry):
    clear()
    print("Установка человека родителем")
    ind = get_human_index_in_list()
    if ind == -1: raise ValueError
    try:
        parent_human = anc.human_list[ind-1]
    except IndexError:
        input(f"Не существует человека с номером [{ind}]")
        return
    except ValueError:
        return

    print(f"Новый родитель:  [{getter.get_all_name(parent_human)}]\n")
    accept = input("1 - подтвердить\n# ")
    if accept == '1':
        editor.edit_parents(human=human, parent=parent_human)
        input("Родитель сохранен")
        return
    input("Отмена редактирования")


def edit_partner(human: Human, anc: Ancestry):
    clear()
    print("Настройка партнера")
    ind = get_human_index_in_list()
    if ind == -1: raise ValueError
    try:
        partner = anc.human_list[ind-1]
    except IndexError:
        input(f"Не существует человека с номером {ind}")
        return
    except ValueError:
        return

    print(f"Новый партнер: {getter.get_all_name(human=partner)}\n")
    accept = input("1 - подтвердить\n# ")
    if accept == '1':
        editor.edit_partner(human=human, partner=partner)
        input("Партнер установлен")
        return
    input("Отмена редактирования")


def edit_children(human: Human, anc: Ancestry):
    clear()
    print("Настройка детей")
    ind = get_human_index_in_list()
    if ind == -1: raise ValueError
    try:
        child = anc.human_list[ind-1]
    except IndexError:
        input(f"Не существует человека с номером {ind}")
        return
    except ValueError:
        return

    if child in human.children:
        accept = input(f"Удалить ребенка: [{getter.get_all_name(child)}]\n"
                       f"1 - принять\n# ")
        if accept == '1':
            editor.delete_child(human=human, child=child)
            input("Ребенок исключен из списка")
            return
        input("Отмена редактирования")
    else:
        accept = input(f"Новый ребенок: [{getter.get_all_name(child)}]\n"
                       f"1 - принять\n# ")
        if accept == '1':
            editor.edit_children(human=human, child=child)
            input("ребенок добавлен")
            return
        input("Отмена редактирования")


def edit_biography(human: Human, new_biography: str, command: int):
    if command == 1:
        old_biography = getter.get_biography(human=human)
        editor.edit_biography(human=human, biography=old_biography + new_biography)
        input("Биография дополнена")
    elif command == 2:
        editor.edit_biography(human=human, biography=new_biography)
        input("Биография перезаписана")
    elif command == 3:
        input("Изменения отменены")
    return


def input_biography(human: Human):
    print("Редактирование биографии (<stop> для окончания)")
    print('+'*10 + '\n\n')
    print(getter.get_biography(human=human))
    print('+' * 10 + '\n\n')
    new_biography = ''
    while (row := input('> ')) != 'stop':
        new_biography += row + '\n'
    menu_commands = ["Добавить в конец", "Перезаписать", "Отменить"]
    menu = Menu(menu_commands)
    com = menu.run()
    edit_biography(human, new_biography, com)




def edit_human_functions_hub(anc: Ancestry, command: int, human: Human):
    if command == 1:
        edit_name(human=human)
    if command == 2:
        edit_surname(human=human)
    if command == 3:
        edit_lastname(human=human)
    if command == 4:
        edit_born_time(human=human)
    if command == 5:
        edit_die_time(human=human)
    if command == 6:
        edit_parent(human=human, anc=anc)
    if command == 7:
        edit_partner(human=human, anc=anc)
    if command == 8:
        edit_children(human=human, anc=anc)
    if command == 9:
        input_biography(human=human)

    if command == 10:
        return False
    return True



def prepare_to_edit_human(anc: Ancestry):
    clear()
    ind = get_human_index_in_list()
    if ind != -1:
        try:
            human = anc.human_list[ind-1]
        except IndexError:
            input(f"Не существует человека с номером [{ind}]")
            return

        text = f"{getter.get_human_info(human)}\n\n"
        menu_commands = ["Имя", "Фамилия", "Отчество", "Дата рождения", "Дата смерти", "Родители", "Партнер", "Дети", "Биография", "Назад"]
        menu = Menu(menu_commands, title=text)
        loop = True

        while loop:
            com = menu.run()
            loop = edit_human_functions_hub(anc=anc, command=com, human=human)
            menu.title = f"{getter.get_human_info(human)}\n\n"
    return


def delete_human(anc: Ancestry):
    clear()
    print("Удаление человека")
    ind = get_human_index_in_list()
    if ind == -1: raise ValueError
    try:
        human = anc.human_list[ind-1]
    except IndexError:
        input(f"Не существует человека с номером {ind}")
        return
    except ValueError:
        return

    accept = input(f"Удалить человека: [{getter.get_all_name(human)}]\n"
                   f"1 - принять\n\n# ")
    if accept == '1':
        anc.human_list.remove(human)
        input("Удаление завершено")
        return
    input("Отмена удаления")





# EDIT MENU
def commands_edit_menu(anc: Ancestry, command: int) -> bool:
    if command == 1:
        add_human(anc=anc)
    if command == 2:
        prepare_to_edit_human(anc=anc)
    if command == 3:
        delete_human(anc=anc)
    if command == 4:
        return False
    return True


def edit_menu(anc: Ancestry) -> None:
    menu_commands = ["Добавить человека", "Редактировать данные человека", "Удалить человека", "Назад"]
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

    try:
        main_loop(anc)
    except KeyboardInterrupt:
        save_data(anc=anc)
        return

    clear()
    print("Сохранение данных...")
    save_data(anc=anc)


if __name__ == '__main__':

    main()

