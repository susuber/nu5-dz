from colorama import Fore, Style
import json

from moduls.file_manager import FileManager
from moduls.menu import get_item_menu
from moduls.victory import victory
from moduls.home_bank import bank_account


def main():
    with open('data/config.json') as file:
        menu = json.load(file)

    manager = FileManager()

    while True:
        num_menu = get_item_menu(menu['maneger'])
        print()
        if num_menu == 13:
            break
        elif num_menu == 1:
            folder = input(f'Введите имя папки: {Fore.GREEN}')
            print(Style.RESET_ALL, end='')
            manager.new_folder(folder_name=folder)
        elif num_menu == 2:
            name = input(f'Введите имя файла или папки: {Fore.GREEN}')
            manager.rm(name=name)
        elif num_menu == 3:
            name = input(f'Введите имя файла: {Fore.GREEN}')
            path = input(f'{Style.RESET_ALL}Введите путь: {Fore.GREEN}')
            print(Style.RESET_ALL, end='')
            manager.copying(name=name, path=path)
        elif num_menu == 4:
            for file in manager.get_content():
                print(file)
        elif num_menu == 5:
            for file in manager.get_dirs():
                print(file)
        elif num_menu == 6:
            for file in manager.get_files():
                print(file)
        elif num_menu == 7:
            print(manager.get_system_info())
        elif num_menu == 8:
            print(manager.author())
        elif num_menu == 9:
            victory()
        elif num_menu == 10:
            bank_account()
        elif num_menu == 11:
            directory = input(f'Введите нужную директорию: {Fore.GREEN}')
            manager.change_directory(directory=directory)
            print(Style.RESET_ALL)
        elif num_menu == 12:
            print(manager.get_home_dir())
        else:
            print(f'{Fore.BLUE}Функционал в процессе разработки{Style.RESET_ALL}')

        print()

if __name__ == '__main__':
    main()


