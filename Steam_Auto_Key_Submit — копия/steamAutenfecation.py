"""
Данный файл помогает автоматически входить в Steam аккаунты \n
Он создает столькоже сесий сколь в переменной names \n
При запуске файла он автоматиче открывает сайт Steam \n
При загрузки он сам вводит имя аккаунта из переменной names \n
А также пароль который есть в файле password.py в переменной password \n
После ввода имени и пароля он сам нажимает кнопку входа \n
Примечание! \n
На всех аккаунтах должен быть 1 пароль \n
В переменной names должен быть имена ваших аккаунтов Steam \n
Заключение: \n
После входа в ваши аккаунты Steam \n
Все COOKIE файлы будут сохранены для дальнейшего входа
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pickle
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from password import password
# переменная с именами аккаунтов
names = ['Акаунт 1', 'Акаунт 2', 'Акаунт 3', 'Акаунт 4']


def create_browser_cok():
    """ Создает браузер и переходит на сайт Steam """
    driver = webdriver.Chrome()
    driver.get('https://store.steampowered.com/login/?l=russian')
    return driver
#Создаем сесию
def start_process_cok():
    """ Создает массив сесий используя функцию create_browser_cok"""
    global drivers
    drivers = [create_browser_cok() for _ in names]
    
def login():
    """ Делает автоматический ввод данных аккаунта для входа в аккаунт """
    for i, driver in enumerate(drivers):
        log = driver.find_element(By.CLASS_NAME , "_2GBWeup5cttgbTw8FM3tfx")
        log.send_keys(names[i])
        passw = driver.find_element(By.XPATH, "//input[@type='password']")
        passw.send_keys(password)
        cleclog = driver.find_element(By.CLASS_NAME, 'DjSvCZoKKfoNSmarsEcTS').click()

def rewrite():
    """ Перезаписывает COOKKIE файлы если они есть \n
    и создает новый если нету
    """
    for i, drive in enumerate(drivers):
        pickle.dump(drive.get_cookies(), open(f'{names[i]}cookies', 'wb'))