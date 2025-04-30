"""Данный модуль написан на языке Python. \n
Данный модуль работает с возрастом пользоватя. \n
Основные функции модуля: \n 
age_100: Выводит через сколько лет исполнится 100 лет \n 
age_find_date: Выводит в каком году вы родились \n 
age_to_age: Сколько вам нужно лет чтобы достичь определенного возраста \n
"""

def age_100(name = "Incognito",age = None):
    """Docstring для age_100
    
    :param name: Имя человека
    :type name: str
    :param age: Его возраст
    :type age: int
    Данная функция скажет когда вам исполнится 100 лет
    """
    if age == None:
        age = input("Введите ваш возраст: ")
    while True:
        try:
            age = int(age)
            if age <= 0:
                if age == 0:
                    return f"{name} вам меньше года"
                else:
                    return f"Вы родитесь через лет так {-age} {name}"
            elif age >= 100:
                if age == 100:
                    return f"Поздравляем вас {name}, вам 100 лет"
                else:
                    return f"{name} ваш сотый день рождения был {age-100} года назат"
            else:
                return f"{name} вам исполнится 100 лет через {100 - age} лет"
        except ValueError:
            print("Вы ввели не правильное значение в аргумент age, аргумент age должен быть значения int.")
            age=input("Введите коректный возраст: ")
        except:
            raise ("Неизвестная ошибка")

def age_find_date(age, date):
    """Docstring для age_find_date
    
    :param age: Ваш возраст
    :type age: int
    :param date: Какой сейчас год 2025
    :type date: int 
    Данная функция определит когда вы роделись по вашему возрасту и сегодняшнему году"""
    try:
        age = int(age)
        if age <= 0:
            return f"Вы родитесь через лет так {-age}"
        else:
            if date - age >= 1:
                return f"Вы роделись в {date - age} году"
            else:
                return f"Вы роделись в {-(date - age)} году до нашей эры"
    except ValueError:
        raise ValueError("Вы ввели не правильное значение в аргумент age, аргумент age должен быть значения int.")
    except:
        raise ("Неизвестная ошибка")

def age_to_age(age, to_age):
    """Docstring для age_to_age
    
    :param age: Ваш возраст
    :type age: int
    :param to_age: Возраст который хотите достич
    :type to_age: int
    Данная функция вычисляет кода вам исполнится определенный возраст.
    """
    try:
        age = int(age)
        if to_age >= age:
            pass
        else:
            return ("Возраст который вы хотите достичь отрицательный")
        if age <= 0:
            return f"Вы родитесь через лет так {-age}"
        elif age >= to_age:
            if age == to_age:
                return f"Поздравляем вам {to_age} лет"
            else:
                return f"Ваш сотый день рождения был {age-to_age} года назат"
        else:
            return f"Вам исполнится {to_age} лет через {to_age - age}"
    except ValueError:
        raise ValueError("Вы ввели не правильное значение в аргумент age, аргумент age должен быть значения int.")
    except:
        raise ("Неизвестная ошибка")\

def test():
    print(age_100('Aza', 100))
    print(age_100('Aza', 123))
    print(age_100('Aza', 11))
    print(age_100('Aza', "f11"))
    print(age_100('Aza'))
    print()
    print(age_find_date(-2,2025))
    print(age_find_date(2,2025))
    print(age_find_date(2026,2025))
    print(age_find_date(0,2025))
    print()
    print(age_to_age(12,100))
    print(age_to_age(-12,100))
    print(age_to_age(12,-100))

test()