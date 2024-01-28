import json
from typing import Dict

import yaml
from colorama import Fore, Style, init
import sqlite3

from moduls.menu import get_item_menu


def show_history(n=10):
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


class PersonaAccount():
    def __init__(self):
        with open('data/personal_account', 'r') as f:
            self.__balance = float(f.read())

        connection = sqlite3.connect('data/finance.db')
        cursor = connection.cursor()

        cursor.execute('''
                CREATE TABLE IF NOT EXISTS expense (
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                name_buy TEXT NOT NULL,
                finance REAL NOT NULL
                )
                ''')

        connection.commit()

        cursor.execute('''
                        CREATE TABLE IF NOT EXISTS income (
                        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                        name_add TEXT NOT NULL,
                        finance REAL NOT NULL
                        )
                        ''')

        connection.commit()
        connection.close()

    def add(self, action: dict):
        self.__balance += action["amount"]
        connection = sqlite3.connect('data/finance.db')
        transactions = connection.cursor()
        transactions.execute(f'INSERT INTO income(name_add, finance) VALUES (?, ?);',
                             (action["name"], action["amount"]))
        connection.commit()
        connection.close()

        with open('data/personal_account', 'w') as f:
            f.write(str(self.__balance))

    def buy(self, action: dict):
        self.__balance -= action["amount"]
        connection = sqlite3.connect('data/finance.db')
        transactions = connection.cursor()
        transactions.execute('INSERT INTO expense(name_buy, finance) VALUES (?, ?);',
                             (action["name"], action["amount"]))
        connection.commit()
        connection.close()

        with open('data/personal_account', 'w') as f:
            f.write(str(self.__balance))

    def amount_account(self):
        print()
        print(f'Сумма на счете: {Fore.GREEN}{self.__balance}{Style.RESET_ALL}', end="\n\n")


def input_sum(action) -> dict[str, str | float]:
    while True:
        name = input(f'Введите {"название покупки" if action == "expense" else "источник дохода"}: {Fore.LIGHTGREEN_EX}')
        print(Style.RESET_ALL, end='')
        try:
            num = float(input(f'Введите сумму: {Fore.LIGHTGREEN_EX}'))
            print(Style.RESET_ALL, end='')
        except ValueError:
            print(f'{Fore.RED}[ERROR 1] Ошибка ввода{Style.RESET_ALL}', end='\n\n')
        else:
            return {"name": name, "amount": num}


def bank_account():
    account = PersonaAccount()

    with open('etc/config.json') as file:
        menu = json.load(file)

    while True:
        num_menu = get_item_menu(menu['bank'])

        if num_menu == 1:
            account.add(input_sum("income"))
        elif num_menu == 2:
            account.buy(input_sum("expense"))
        elif num_menu == 3:
            show_history()
        elif num_menu == 4:
            account.amount_account()
        elif num_menu == 5:
            break
        else:
            print(f'{Fore.RED}[ERROR 3] Неизвестная ошибка{Style.RESET_ALL}', end='\n\n')
