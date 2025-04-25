from random import randint
bugalteria = {
    "valut_Kurs": 100,
    "procent_stavka": 100,
    "price_birga": 100
    }
class Logik:
    def __init__(self, year):
        self.year = year

    def otchet(self):
        for i in range(1, self.year + 1):
            if bugalteria['valut_Kurs'] != 'Обвал':
                self.kurs_valut()
            else:
                break
        self.result()
    def kurs_valut(self):
        global kurs_random
        kurs_random = randint(0, 100000)
        kurs_napr = randint(1,2)
        self.kurs_obval_rost()
        if  kurs_napr == 1:
            self.obval_rost(['-','+'])
        else:
            self.obval_rost(['+','-'])
    def kurs_obval_rost(self):
        global kurs_obval_rost
        if kurs_random >= 98000:
            kurs_obval_rost = randint(55,60)
        elif kurs_random >= 95000:
            kurs_obval_rost = randint(40,54)
        elif kurs_random >= 90000:
            kurs_obval_rost = randint(35,39)
        elif kurs_random >= 85000:
            kurs_obval_rost = randint(20,34)
        elif kurs_random >= 70000:
            kurs_obval_rost = randint(15,19)
        elif kurs_random >= 50000:
            kurs_obval_rost = randint(10,14)
        else:
            kurs_obval_rost = randint(0,9)
    def obval_rost(self, char):
        if bugalteria['price_birga'] != 'Обвал' and bugalteria['procent_stavka'] != 'Обвал':
            if bugalteria['price_birga'] >= 1:
                bugalteria["price_birga"] = eval(f"bugalteria[\"price_birga\"] {char[0]} kurs_obval_rost")
            else:
                bugalteria["price_birga"] = 'Обвал'
        if bugalteria["procent_stavka"] != 'Обвал' and bugalteria['valut_Kurs'] != 'Обвал':
            if bugalteria['procent_stavka'] >=1:
                bugalteria["procent_stavka"] = eval(f"bugalteria[\"procent_stavka\"] {char[1]} kurs_obval_rost")
            else:
                bugalteria["procent_stavka"] = 'Обвал'
        if bugalteria['valut_Kurs'] != 'Обвал':
            if bugalteria['valut_Kurs'] >=1:
                bugalteria["valut_Kurs"] = eval(f"bugalteria[\"valut_Kurs\"] {char[0]} kurs_obval_rost")
            else:
                bugalteria["valut_Kurs"] = 'Обвал'
        # Добавьте чтобы  проверить работу кода
        print(bugalteria["valut_Kurs"], bugalteria["procent_stavka"], bugalteria["price_birga"], kurs_obval_rost )
    def result(self):
        if bugalteria['procent_stavka'] != 'Обвал' and bugalteria ['procent_stavka'] >=1:
            bugalteria['procent_stavka'] = str(bugalteria['procent_stavka']/10) + "%"
        result = f"""
Курс валюты: {bugalteria['valut_Kurs']}
Процентная ставка: {bugalteria['procent_stavka']}
Цены на бирже: {bugalteria['price_birga']}
""" 
        print(result)
otc = Logik(3000)
otc.otchet()
print(bugalteria)