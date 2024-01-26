import json

from colorama import Fore, Style, init
import sqlite3

from moduls.menu import get_item_menu


class Personal_account():
    def __init__(self):
        with open('data/personal_account', 'r') as f:
            self.__balance = float(f.read())

        connection = sqlite3.connect('data/finance.db')
        cursor = connection.cursor()

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS Expense (
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        finance REAL NOT NULL
        )
        ''')

        connection.commit()

        cursor.execute('''
                CREATE TABLE IF NOT EXISTS Income (
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                finance REAL NOT NULL
                )
                ''')

        connection.commit()
        connection.close()

    def add(self, num):
        self.__balance += num
        connection = sqlite3.connect('data/finance.db')
        transactions = connection.cursor()
        transactions.execute(f"INSERT INTO Income(finance) VALUES ({float(num)})")
        connection.commit()
        connection.close()

        with open('data/personal_account', 'w') as f:
            f.write(str(self.__balance))

    def buy(self, num):
        self.__balance -= num
        connection = sqlite3.connect('data/finance.db')
        transactions = connection.cursor()
        transactions.execute(f"INSERT INTO Expense(finance) VALUES ({float(num)})")
        connection.commit()
        connection.close()

        with open('data/personal_account', 'w') as f:
            f.write(str(self.__balance))

    def show_history(self, n=10):
        connection = sqlite3.connect('data/finance.db')
        transactions = connection.cursor()
        transactions.execute(f'SELECT * FROM Income ORDER BY id DESC LIMIT {n}')
        income = transactions.fetchall()
        transactions.execute(f'SELECT * FROM Expense ORDER BY id DESC LIMIT {n}')
        expense = transactions.fetchall()
        connection.commit()
        connection.close()

        print(f"{Fore.GREEN}Последние {n} доходов: {Style.RESET_ALL}")
        for i in income:
            print(i)
        print()

        print(f"{Fore.RED}Последние {n} расходы: {Style.RESET_ALL}")
        for i in expense:
            print(i)
        print()

    def amount_account(self):
        print()
        print(f'Сумма на счете: {Fore.GREEN}{self.__balance}{Style.RESET_ALL}', end="\n\n")


def input_sum() -> float:
    while True:
        try:
            num = float(input(f'Введите сумму: {Fore.LIGHTGREEN_EX}'))
            print(Style.RESET_ALL, end='')
        except ValueError:
            print(f'{Fore.RED}[ERROR 1] Ошибка ввода{Style.RESET_ALL}', end='\n\n')
        else:
            return num


def bank_account():
    account = Personal_account()

    with open('data/config.json') as file:
        menu = json.load(file)

    while True:
        num_menu = get_item_menu(menu['bank'])

        if num_menu == 1:
            account.add(input_sum())
        elif num_menu == 2:
            account.buy(input_sum())
        elif num_menu == 3:
            account.show_history()
        elif num_menu == 4:
            account.amount_account()
        elif num_menu == 5:
            break
        else:
            print(f'{Fore.RED}[ERROR 3] Неизвестная ошибка{Style.RESET_ALL}', end='\n\n')
