import os.path

from colorama import Fore, Style
import json

from moduls.file_manager import FileManager, get_content, get_dirs, get_files, get_system_info
from moduls.menu import get_item_menu
from moduls.victory import victory
from moduls.home_bank import bank_account


def main():
    with open('etc/config.json') as file:
        menu = json.load(file)

    manager = FileManager()

    while True:
        num_menu = get_item_menu(menu['manager'])
        print()
        match num_menu:
            case 1:
                folder = input(f'Введите имя папки: {Fore.GREEN}')
                print(Style.RESET_ALL, end='')
                manager.new_folder(folder_name=folder)
            case 2:
                name = input(f'Введите имя файла или папки: {Fore.GREEN}')
                manager.rm(name=name)
            case 3:
                name = input(f'Введите имя файла: {Fore.GREEN}')
                path = input(f'{Style.RESET_ALL}Введите путь: {Fore.GREEN}')
                print(Style.RESET_ALL, end='')
                manager.copying(name=name, path=path)
            case 4:
                for file in get_content():
                    print(file)
            case 5:
                for file in get_dirs():
                    print(file)
            case 6:
                for file in get_files():
                    print(file)
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
                print(manager.get_home_dir())
            case 13:
                dirs = f'dirs: {", ".join(get_dirs())}'
                files = f'files: {", ".join(get_files())}'
                if not os.path.isdir('output'):
                    os.mkdir('output')
                with open('output/listdir.txt', 'w') as file:
                    file.write(f'{files}\n{dirs}')
            case 14:
                break
            case _:
                print(f'{Fore.BLUE}Функционал в процессе разработки{Style.RESET_ALL}')


if __name__ == '__main__':
    main()
