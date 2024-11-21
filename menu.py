import os


class Menu:
    def __init__(self, commands: list[str],
                 left_indent: int = 0,
                 top_indent: int = 0) -> None:
        self.commands: list[str] = commands
        self.left_indent: int = left_indent
        self.top_indent: int = top_indent
        self.command: str = ''


    def format_print_list(self) -> None:
        print('\n' * self.top_indent, end='')
        for i, el in enumerate(self.commands):
            print(' ' * self.left_indent + f"{i + 1} - {el}")

    def is_valid_command(self) -> bool:
        if (self.command.isdigit()) and (0 <= int(self.command)-1 < len(self.commands)): return True
        return False

    def run(self) -> int:
        while True:
            os.system('cls')
            self.format_print_list()
            self.command = input("\n#> ")
            if self.is_valid_command(): return int(self.command)
