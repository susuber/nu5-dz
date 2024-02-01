import os.path

import getch
from colorama import Fore, Style
import json

from atexit import register

from moduls.file_manager import FileManager, get_content, get_dirs, get_files, get_system_info, new_folder
from moduls.menu import get_item_menu
from moduls.victory import victory
from moduls.home_bank import bank_account
from moduls.decorator import get_spaces, pause


@register
def terminate():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\n\n\n')
    print(f"{Fore.LIGHTMAGENTA_EX}До новых встреч!!!")
    getch.getch()
    os.system('cls' if os.name == 'nt' else 'clear')


@pause
@get_spaces
def print_iter(iterable: list) -> None:
    for i in iterable:
        print(i)


def main():
    with open('etc/config.json') as file:
        menu = json.load(file)

    manager = FileManager()
    selecting_menu_item(menu=menu, manager=manager)


def selecting_menu_item(menu, manager):
    while True:
        num_menu = get_item_menu(menu['manager'])
        match num_menu:
            case 1:
                folder = input(f'Введите имя папки: {Fore.GREEN}')
                print(Style.RESET_ALL, end='')
                new_folder(folder_name=folder)
            case 2:
                name = input(f'Введите имя файла или папки: {Fore.GREEN}')
                manager.rm(name=name)
            case 3:
                name = input(f'Введите имя файла или папки: {Fore.GREEN}')
                path = input(f'{Style.RESET_ALL}Введите путь: {Fore.GREEN}')
                print(Style.RESET_ALL, end='')
                manager.copying(name=name, path=path)
            case 4:
                print_iter(get_content())
            case 5:
                print_iter(get_dirs())
            case 6:
                print_iter(get_files())
            case 7:
                print(get_system_info())
            case 8:
                print(manager.author())
            case 9:
                victory()
            case 10:
                bank_account()
            case 11:
                directory = input(f'Введите нужную директорию: {Fore.GREEN}')
                manager.change_directory(directory=directory)
                print(Style.RESET_ALL)
            case 12:
                manager.get_home_dir()
            case 13:
                dirs = f'dirs: {", ".join(get_dirs())}'
                print(dirs)
                files = f'files: {", ".join(get_files())}'
                print(files)
                print("Нажмите любую клавишу...")
                getch.getch()
                if not os.path.isdir('output'):
                    os.mkdir('output')
                with open('output/listdir.txt', 'w') as file:
                    file.write(f'{files}\n{dirs}')
                print(f'{Fore.GREEN}Файл записан{Style.RESET_ALL}')
                print("Нажмите любую клавишу...")
                getch.getch()
            case 14:
                break
            case _:
                print(f'{Fore.BLUE}Функционал в процессе разработки{Style.RESET_ALL}')
                print("Нажмите любую клавишу...")
                getch.getch()


if __name__ == '__main__':
    main()
