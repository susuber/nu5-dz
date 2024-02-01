# файловый менеджер
import shutil
import os
import sys
import tempfile
from colorama import Fore, Style
import platform


def get_system_info():
    system = platform.uname()
    return f"""
    Система: {Fore.GREEN}{system.system}{Style.RESET_ALL}
    Имя машины: {Fore.GREEN}{system.node}{Style.RESET_ALL}
    Релиз: {Fore.GREEN}{system.release}{Style.RESET_ALL}
    Версия: {Fore.GREEN}{system.version}{Style.RESET_ALL}
    Машина: {Fore.GREEN}{system.machine}{Style.RESET_ALL}
    Процессор: {Fore.GREEN}{system.processor}{Style.RESET_ALL}
    """


def get_dirs():
    """
    Печать файлов в папке
    """
    return [name for name in os.listdir() if os.path.isdir(name)]


def get_files():
    """
    Печать директорий в папке
    """
    return [name for name in os.listdir() if os.path.isfile(os.path.join(name))]


def get_content():
   """
   Возвращает все содержимое папки
   :return: список файлов и папок
   """
   return list(os.listdir())


class FileManager:
    def __init__(self, name='Kuklin Alexandr', email='sir.kuklin2014@yandex.ru'):
        self.__path = os.getcwd()
        self.__email = email
        self.__name = name

    def get_home_dir(self):
        """
        Печать текущего каталога
        """
        return self.__path

    def new_folder(self, folder_name: str) -> None:
        """
        Создание новой папки
        :param folder_name: имя папки
        """
        if not os.path.exists(f'{self.__path}/{folder_name}'):
            os.mkdir(folder_name)

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
            elif os.path.isdir(f'{self.__path}/{name}'):
                shutil.copytree(f'{self.__path}/{name}', f'{self.__path}/{path}')
            else:
                print(f'{Fore.RED}[ERROR coping]Unknown error{Style.RESET_ALL}')

    def rm(self, name: str) -> None:
        """
        Удаление файла или папки
        :param name: Имя файла или папки
        """
        if os.path.exists(f'{self.__path}/{name}'):
            if os.path.isfile(f'{self.__path}/{name}'):
                os.remove(f'{self.__path}/{name}')
            elif os.path.isdir(f'{self.__path}/{name}'):
                shutil.rmtree(f'{self.__path}/{name}')
            else:
                print(f'{Fore.RED}[ERROR coping]Unknown error{Style.RESET_ALL}')

    def author(self):
        return f"Автор программы\nИмя: {self.__name}\nПочта: {self.__email}"

    def change_directory(self, directory: str) -> None:
        if os.path.isdir(f'{self.__path}/{directory}'):
            os.chdir(f'{self.__path}/{directory}')
            self.__path = os.getcwd()
        else:
            print(f'{Fore.RED}[ERROR]{directory} не найдена')


