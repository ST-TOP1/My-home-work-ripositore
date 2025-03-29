from colorama import *
import time
import json
from colorama import Fore, Back, Style
status = True
my_notes = {}
try:
    with open('jsonaza.json', 'r', encoding='UTF-8') as file:
        my_notes = json.load(file)
except:
    with open('jsonaza.json', 'w', encoding='UTF-8') as file:
        my_notes['index'] = 0
        my_notes['Title'] = {}
        json.dump(my_notes, file, indent=4, ensure_ascii=False)
def notes():
    print(Fore.RED + """
    ______________________________
    \\                             |
     |  #Notes app            ^^^ |
     | -------------------------- |
     | 1. Добавить заметку        |
     | 2. Показать все заметки    |
     | 3. Выйти                   |
     | -------------------------- |
     | Введите число в консоль!!! |
     |____________________________|
    """)
    command = str(input('Ваше число: '))
    print('\n'* 100)
    if command == '1':
        add_notes()
    elif command == '2':
        read_notes()
    elif command == '3':
        return False
def add_notes():
    with open('jsonaza.json', 'r', encoding='UTF-8') as file:
        my_notes = json.load(file)
    b = ''
    a = input('Title: ')
    print('Enter создает новую строку, Введите в консоль Exit чтобы завершить текст\nText:')
    while True:
        b1 = str(input())
        if b1 in {'exit', 'Exit'}:
            break
        else:
            b = b + b1 + '\n    '
    v = [a, b]
    index = int(my_notes["index"]) + 1
    my_notes['index'] = index 
    my_notes["Title"][str(index)] = v
    with open('jsonaza.json', 'w', encoding='UTF-8') as file:
        json.dump(my_notes, file, indent=4, ensure_ascii=False)
    print('\n'*100)
    print(Fore.GREEN + f'''
    Ваша заметка создана
    ______________________________________________________________________________________________________________________________________________
    Title
    {a}
    ----------------------------------------------------------------------------------------------------------------------------------------------
    Text
    {b}
    ______________________________________________________________________________________________________________________________________________

    Exit
    ''')
    command = str(input('Введите что угодно чтобы выйти: '))
    print('\n'* 100)
def read_notes():
    with open('jsonaza.json', 'r', encoding='UTF-8') as file:
        my_notes = json.load(file)
    if len(my_notes["Title"]) > 0:
        for k,v in my_notes["Title"].items():
            print('    Заметка', k)
            if len(v[0]) > 25:
                print(f'    Title\n    {v[0][:25]+'...'}')
            else:
                print(f'    Title\n    {v[0]}')
            if len(v[1]) > 25:
                print(f'    Text:\n   {v[1][:25]}' + '...')
            else:
                print(f'    Text:\n   {v[1]}')
                print('\n'*2)
        command = str(input('''
    Введите: 1 чтобы прочитать определенную заметку
    Введите: 2 чтобы удалить определенную заметку
    Выйти: Введите что угодно кроме 1 и 2.
    Ввод: '''))
        if command == '1':
            command = int(input(Fore.GREEN +'Введите индекс заметки которую вы хотите прочитать: '))
            print('\n'*100)
            if str(command) in my_notes["Title"]:
                print(f'    Title\n    {my_notes["Title"][str(command)][0]}')
                print(f'    Text:\n   {my_notes["Title"][str(command)][1]}')
                command = str(input('Введите что угодно чтобы выйти из режима чтения:'))
                print('\n'*100)
            else:
                print('Такой заметки нет')
                time.sleep(5)
        if command == '2':
            command = int(input(Fore.GREEN +'Введите индекс заметки которую вы хотите удалить: '))
            print('\n'*100)
            if str(command) in my_notes["Title"]:
                del my_notes["Title"][str(command)]
                with open('jsonaza.json', 'w', encoding='UTF-8') as file:
                    json.dump(my_notes, file, indent=4, ensure_ascii=False)
                print(Fore.GREEN +'Заметка успешно удалена')
                command = str(input('Введите что угодно чтобы выйти:'))
                print('\n'*100)
            else:
                print('Такой заметки нет')
                time.sleep(5)
    else:
        print('У вас нет заметок')
        time.sleep(5)
        print('\n'* 100)

def start_app_notes(app_start):
    while status == True:
        if app_start == None:
            print('Запустить Notes', Fore.GREEN + '(y/n)?')
            app_start = input().lower()
            print('\n'* 100)
        if app_start in {'y', 'yes'}:
            a = notes()
            if a == False:
                break
        elif app_start in {'n', 'not', 'no'}:
            print('Пока')
            break
        else:
            print('Error: Не коректно введенные данные пользователя:\nПопытайтесь снова')
            app_start = None
            continue
    else:
        print('Пока')

start_app_notes(None)