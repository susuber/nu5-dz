import os
import getch


def get_spaces(func):
    def wrapper(*args, **kwargs):
        print()
        print()
        spaces = func(*args, **kwargs)
        print()
        return spaces
    return wrapper


def pause(func):
    def wrapper(*args, **kwargs):
        spaces = func(*args, **kwargs)
        print("Нажмите любую клавишу...")
        getch.getch()
        return spaces
    return wrapper


def clear(func):
    def wrapper(*args, **kwargs):
        spaces = func(*args, **kwargs)
        os.system('cls' if os.name == 'nt' else 'clear')
        return spaces
    return wrapper
