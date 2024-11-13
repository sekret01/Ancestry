import os
from human import Human


def format(text: str, spec: str) -> str:
    if spec == 'p': padding = 5
    elif spec == 'h': padding = 10
    elif spec == 't': padding = 12
    else: raise ValueError(f"Разрешенные значение spec: 'p', 'h'; получено: {spec}")
    return " "*padding + text


def get_born_time() -> tuple[int, int, int]:
    while True:
        print(format("Дата рождения: ", 'p'), end='')
        born_time_str = input()

        born_time = tuple(valid_date(born_time_str))
        if born_time != (0, 0, 0): return born_time
        print(format(f"{' ':>35s}Некорректная дата: {born_time_str}", "p"), end='')
        print('\r', end='')


def get_die_time() -> tuple[int, int, int]:
    while True:
        print(format("Дата смерти: ", 'p'), end='')
        die_time_str = input()

        if die_time_str == "":
            die_time = None
        else:
            die_time = tuple(valid_date(die_time_str))
        if die_time != (0, 0, 0): return die_time
        print(format(f"{' ':>35s}Некорректная дата: {die_time}", "p"), end='')
        print('\r', end='')


def valid_date(date: str) -> tuple[int, int, int]:
    """"""
    try:
        if len(date.split('.')) == 3:
                d, m, y = date.split('.')
                year = valid_part_date(y, 'year')
                month = valid_part_date(m, 'month')
                day = valid_part_date(d, 'day')
                tuple_date = (year, month, day)
                return tuple_date

        else: raise ValueError("меньше длинна")

    except ValueError as ex:
        return 0, 0, 0


def valid_part_date(part: str, date_type: str):

    if date_type == "year": is_range = lambda x: 1 <= x <= 9999
    elif date_type == "month": is_range = lambda x: 1 <= x <= 12
    elif date_type == "day": is_range = lambda x: 1 <= x <= 31
    else: raise ValueError()

    if part.isdigit() and is_range(int(part)): return int(part)
    raise ValueError()


def form() -> Human:

    try:
        os.system('cls')
        print(format("Форма заполнения нового человека", 'h'))
        print("\n\n")
        name = input(format("Имя: ", 'p'))
        surname = input(format("Фамилия: ", 'p'))
        lastname = input(format("Отчество: ", 'p'))

        gender = input(format("Пол: ", 'p'))

        born_time = get_born_time()
        die_time = get_die_time()

        return Human(name=name, surname=surname, lastname=lastname,
                     born_time=born_time, die_time=die_time, gender=gender)

    except ValueError as ex:
        print(ex)
        _ = input("Заполнить еще раз...")
        form()
