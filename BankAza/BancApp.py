
import json
bank_bugalteria = None
try:
    with open('Bugalteria.json', 'r', encoding='UTF-8') as file:
        bank_bugalteria = json.load(file)
except:
    new_bugalteria = {
        'BankMoney': 0,
        'users': {

        }
    }
    with open('Bugalteria.json', 'w', encoding='UTF-8') as file:
        json.dump(new_bugalteria, file, indent=4, ensure_ascii=False)
        print("У банка нет Бугалтерии создаем новую")
    with open('Bugalteria.json', 'r', encoding='UTF-8') as file:
        bank_bugalteria = json.load(file)
        print("Создана новая бугалтерия")
else:
    print("Бугалтерия найдена")

class BankOperation:
    def riwards(iin, summa):
        iin = str(iin)
        if int(summa) >= 1:
            if iin in bank_bugalteria['users']:
                bank_bugalteria['users'][iin]['balance'] = int(bank_bugalteria['users'][iin]['balance']) + int(summa)
                bank_bugalteria['BankMoney'] = int(bank_bugalteria['BankMoney']) + int(summa)
                with open('Bugalteria.json', 'w', encoding='UTF-8') as file:
                    json.dump(bank_bugalteria, file, indent=4, ensure_ascii=False)
                return 'Успех'
            else:
                return 'Пользователь не найден'
        else:
            return "Минимальная сумма вывода 1"
    def withdraw(iin, summa):
        iin = str(iin)
        if int(summa) >= 1:
            if str(iin) in bank_bugalteria['users']:
                if int(bank_bugalteria['users'][iin]['balance']) - int(summa) >= 0:
                    if int(bank_bugalteria['BankMoney']) - int(summa) >= 0:
                        bank_bugalteria['users'][iin]['balance'] = int(bank_bugalteria['users'][iin]['balance']) - int(summa)
                        bank_bugalteria['BankMoney'] = int(bank_bugalteria['BankMoney']) - int(summa)
                        with open('Bugalteria.json', 'w', encoding='UTF-8') as file:
                            json.dump(bank_bugalteria, file, indent=4, ensure_ascii=False)
                        return 'Успех'
                    else:
                        return "В банкомате нету данной суммы"
                else:
                    return "Недостаточно средств на балансе"
            else:
                return 'Пользователь не найден'
        else:
            return 'Минимальная сумма вывода 1'
    def create_users(iin):
        iin = str(iin)
        if iin not in bank_bugalteria['users']:
            first_name = input('Ваше имя: ')
            last_name = input('Ваша фамилия: ')
            bank_bugalteria['users'][str(iin)] = {'first_name': str(first_name), 'last_name': str(last_name), 'balance': 0}
            with open('Bugalteria.json', 'w', encoding='UTF-8') as file:
                json.dump(bank_bugalteria, file, indent=4, ensure_ascii=False)
            return 'Пользователь создан'
        else:
            return 'Такой пользователь существует в системе'
    

# while True:
#     command = int(input('Введте команду: 1: Создать users, 2: Вывод средств, 3: Пополнение'))
#     if command == 1:
#         iin = int(input('Ваш ИИН'))
#         print(BankOperation.create_users(iin))
#     elif command == 2:
#         iin = int(input('Ваш ИИН'))
#         summa = int(input('Сумма вывода'))
#         print(BankOperation.withdraw(iin, summa))
#     elif command == 3:
#         iin = int(input('Ваш ИИН'))
#         summa = int(input('Сумма ввода'))
#         print(BankOperation.riwards(iin, summa))
