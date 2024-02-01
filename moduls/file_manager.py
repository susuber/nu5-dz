# файловый менеджер
import shutil
import os

from colorama import Fore, Style
import platform
from moduls.decorator import get_spaces, pause


@pause
@get_spaces
def get_system_info():
    system = platform.uname()
    print(f"""
    Система: {Fore.GREEN}{system.system}{Style.RESET_ALL}
    Имя машины: {Fore.GREEN}{system.node}{Style.RESET_ALL}
    Релиз: {Fore.GREEN}{system.release}{Style.RESET_ALL}
    Версия: {Fore.GREEN}{system.version}{Style.RESET_ALL}
    Машина: {Fore.GREEN}{system.machine}{Style.RESET_ALL}
    Процессор: {Fore.GREEN}{system.processor}{Style.RESET_ALL}
    """)


@pause
@get_spaces
def get_dirs():
    """
    Печать файлов в папке
    """
    return [name for name in os.listdir() if os.path.isdir(name)]


@pause
@get_spaces
def get_files():
    """
    Печать директорий в папке
    """
    return [name for name in os.listdir() if os.path.isfile(os.path.join(name))]


@pause
@get_spaces
def get_content():
    """
    Возвращает все содержимое папки
    :return: список файлов и папок
    """
    return list(os.listdir())


@pause
@get_spaces
def new_folder(folder_name: str) -> None:
    """
    Создание новой папки
    :param folder_name: имя папки
    """
    try:
        os.mkdir(folder_name)
        print(f'{Fore.GREEN}Папка {folder_name} создана{Style.RESET_ALL}')
    except FileExistsError:
        print(f'{Fore.RED}Папка {folder_name} уже существует{Style.RESET_ALL}')


class FileManager:
    def __init__(self, name='Kuklin Alexandr', email='sir.kuklin2014@yandex.ru'):
        self.__path = os.getcwd()
        self.__email = email
        self.__name = name

    @pause
    @get_spaces
    def get_home_dir(self):
        """
        Печать текущего каталога
        """
        print(self.__path)

    @pause
    def copying(self, name: str, path: str) -> None:
        """
        Копирование папки/файла
        :param name: Имя файла
        :param path: Путь для копирования
        """
        path_split = path.split('/')
        if len(path_split) > 1:
            os.makedirs(f'{self.__path}/{"/".join(path_split[:-1])}')
        if os.path.exists(f'{self.__path}/{name}'):
            if os.path.isfile(f'{self.__path}/{name}'):
                shutil.copy(f'{self.__path}/{name}', f'{self.__path}/{path}')
                print(f'{Fore.GREEN}Файл {str(path_split[-1])} скопирован{Style.RESET_ALL}')
            elif os.path.isdir(f'{self.__path}/{name}'):
                shutil.copytree(f'{self.__path}/{name}', f'{self.__path}/{path}')
                print(f'{Fore.GREEN}Папка {str(path_split[-1])}  скопирована{Style.RESET_ALL}')
            else:
                print(f'{Fore.RED}[ERROR coping]Unknown error{Style.RESET_ALL}')
                os.system('pause')

    @pause
    @get_spaces
    def rm(self, name: str) -> None:
        """
        Удаление файла или папки
        :param name: Имя файла или папки
        """
        try:
            if os.path.isfile(f'{self.__path}/{name}'):
                os.remove(f'{self.__path}/{name}')
                print(f'{Fore.GREEN}Файл удален{Style.RESET_ALL}')
            elif os.path.isdir(f'{self.__path}/{name}'):
                shutil.rmtree(f'{self.__path}/{name}')
                print(f'{Fore.GREEN}Папка удалена{Style.RESET_ALL}')
            else:
                print(f'{Fore.RED}[ERROR]Нет такого файла или папки{Style.RESET_ALL}')
        except FileNotFoundError:
            print(f'{Fore.RED}[ERROR]Нет такого файла или папки{Style.RESET_ALL}')

    @pause
    @get_spaces
    def author(self):
        print (f"Автор программы\nИмя: {self.__name}\nПочта: {self.__email}")

    @pause
    @get_spaces
    def change_directory(self, directory: str) -> None:
        if os.path.isdir(f'{self.__path}/{directory}'):
            os.chdir(f'{self.__path}/{directory}')
            self.__path = os.getcwd()
            print(f'{Fore.GREEN}Новая директория:{Style.RESET_ALL}')
            print(self.__path)
        else:
            print(f'{Fore.RED}[ERROR]{directory} не найдена')
            os.system('pause')
