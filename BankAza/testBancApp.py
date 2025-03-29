import unittest
import json

try:
    with open('Bugalteria.json', 'r', encoding='UTF-8') as file:
        bank_bugalteria = json.load(file)
except:
    new_bugalteria = {
    "BankMoney": 0,
    "users": {
        "1": {
            "first_name": "dff",
            "last_name": "dfd",
            "balance": 1000
        }
    }
}
    with open('Bugalteria.json', 'w', encoding='UTF-8') as file:
        json.dump(new_bugalteria, file, indent=4, ensure_ascii=False)
        print("У банка нет Бугалтерии создаем новую")
    with open('Bugalteria.json', 'r', encoding='UTF-8') as file:
        bank_bugalteria = json.load(file)
        print("Создана новая бугалтерия")
else:
    new_bugalteria = {
    "BankMoney": 0,
    "users": {
        "1": {
            "first_name": "dff",
            "last_name": "dfd",
            "balance": 1000
        }
    }
}
    with open('Bugalteria.json', 'w', encoding='UTF-8') as file:
        json.dump(new_bugalteria, file, indent=4, ensure_ascii=False)
        print("У банка нет Бугалтерии создаем новую")
    with open('Bugalteria.json', 'r', encoding='UTF-8') as file:
        bank_bugalteria = json.load(file)
        print("Создана новая бугалтерия")
from BancApp import BankOperation as Banc

class TestBankOperation(unittest.TestCase):

    def test_withdraw(self):
        self.assertEqual(Banc.withdraw(1, 1000), "В банкомате нету данной суммы") #BankMoney = 0 и хоть у пользователя есть деньги банк не в состоянии предоставить средства
        self.assertEqual(Banc.withdraw(1, 0), 'Минимальная сумма вывода 1') 
    def test_create_users(self):
        self.assertEqual(Banc.create_users(133343), 'Пользователь создан')
        self.assertEqual(Banc.create_users(133343), 'Такой пользователь существует в системе')
        self.assertEqual(Banc.create_users(1), 'Такой пользователь существует в системе')
    def test_rewards(self):
        self.assertEqual(Banc.riwards(133343, 1000), 'Успех')
        self.assertEqual(Banc.riwards(133343, -1000), "Минимальная сумма вывода 1")
    def test_withdraw(self):
        self.assertEqual(Banc.withdraw(1, 1000), "Успех")
        self.assertEqual(Banc.withdraw(1, 0), "Минимальная сумма вывода 1") 

if __name__ == "__main__":
    unittest.main()