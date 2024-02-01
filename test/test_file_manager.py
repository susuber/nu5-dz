import shutil
import os

from colorama import Fore, Style

from moduls.file_manager import FileManager, get_dirs, get_files


def test_get_home_dir():
    manager = FileManager()
    assert manager.get_home_dir() == os.getcwd()


def test_new_folder():
    manager = FileManager()
    new_folder("test_folder")
    assert os.path.isdir(f'{os.getcwd()}/test_folder')
    shutil.rmtree(f'{os.getcwd()}/test_folder')


def test_coping_file():
    manager = FileManager()
    with open("test.txt", "w") as file:
        file.write("test")
    manager.copying(name='test.txt', path='test_folder/test.txt')
    assert os.path.isfile(f'{os.getcwd()}/test_folder/test.txt')
    shutil.rmtree(f'{os.getcwd()}/test_folder')
    os.remove('test.txt')


def test_coping_dir():
    manager = FileManager()
    os.mkdir('test_folder')
    with open("test_folder/test.txt", "w") as file:
        file.write("test")

    manager.copying(name='test_folder', path='test_folder1')
    assert os.path.isdir('test_folder1')
    shutil.rmtree('test_folder')
    shutil.rmtree('test_folder1')


def test_rm_file():
    manager = FileManager()
    with open("test.txt", "w") as file:
        file.write("test")
    manager.rm('test.txt')
    assert os.path.isfile(f'{os.getcwd()}/test.txt') == False


def test_rm_dir():
    manager = FileManager()
    os.mkdir('test_folder')
    manager.rm('test_folder')
    assert os.path.isdir(f'{os.getcwd()}/test_folder') == False


def test_author():
    manager = FileManager()
    assert manager.author() == "Автор программы\nИмя: Kuklin Alexandr\nПочта: sir.kuklin2014@yandex.ru"


def test_get_dir():
    assert isinstance(get_dirs(), list)


def test_get_files():
    assert isinstance(get_files(), list)


def test_change_directory():
    manager = FileManager()
    path = os.getcwd()
    os.mkdir('test_folder')
    manager.change_directory("test_folder")
    assert os.getcwd() == path + "/test_folder"
    os.chdir('..')
    shutil.rmtree('test_folder')
