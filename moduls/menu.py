from colorama import Fore, Style
import os
from moduls.decorator import clear


@clear
def get_item_menu(menu: dict) -> int:
    """
    Выводит меню программы и возвращает выбранный пункт
    :param menu:
    :return:
    """
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        for key, value in menu.items():
            print(Fore.GREEN, key, Style.RESET_ALL, value)

        print()
        point = input(f'Выберите пункт меню: {Fore.GREEN}')
        print(Style.RESET_ALL, end='')

        if point.isnumeric():
            if point in menu.keys():
                return int(point)
            else:
                print(Fore.LIGHTRED_EX, '[ERROR 1] Такого пункта нет в меню', Style.RESET_ALL)
        else:
            print(Fore.LIGHTRED_EX, '[ERROR 2] Вы ввели не число', Style.RESET_ALL)