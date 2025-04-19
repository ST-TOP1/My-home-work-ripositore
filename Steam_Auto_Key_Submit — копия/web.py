"""
Основной файл отвечаюший за: \n
Создания сессий \n
Ввода ключей \n
Мульти задачность: \n
Для работы всех сесий одновременно использованиме модуля concurrent.futures
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import pickle
import time
from vk import *
import concurrent.futures
# Тут хранится назвыния всех COOKIE файлов для их добавления в сесию
COOKIE_FILES = ["A1cookies", "A2cookies", "A3cookies", "A4cookies"]


#Создает браузер
def create_browser():
    "Функция создает браузер"
    driver = webdriver.Chrome()
    return driver
#Создаем сесию
def start_process():
    """Функция создает сесии по количеству Cookie файлов \n
    И сохраняет каждую сесию в drivers мвссив"""
    global drivers
    drivers = [create_browser() for _ in COOKIE_FILES]
    # Open Steam pages with cookies
    for i, driver in enumerate(drivers):
        load_cookies(driver, COOKIE_FILES[i])

def load_cookies(driver, cookie_file):
    """
    Функция загружает COOKIE в сессию
    """
    driver.get("https://store.steampowered.com/account/registerkey")
    with open(cookie_file, "rb") as file:
        cookies = pickle.load(file)
        for cookie in cookies:
            driver.add_cookie(cookie)
    driver.refresh()

# переменная для контроля ввода возможных ключей
maskey = [
    [0,10],
    [10,20],
    [20,30],
    [30,40]
]
# Функции для авто ввода ключей
def aza1():
    """ Авто ввод ключей на сайте """
    key = key_string()
    butall = drivers[0].find_element(By.ID, "accept_ssa").click()
    for i in range(0,10):
        product_key_input = drivers[0].find_element(By.ID, "product_key")
        product_key_input.clear()
        product_key_input.send_keys(key[i])
        register_button = drivers[0].find_element(By.ID, "register_btn")
        register_button.click()
        time.sleep(1)
def aza2():
    """ Авто ввод ключей на сайте """
    key = key_string()
    butall = drivers[1].find_element(By.ID, "accept_ssa").click()
    for i in range(10,20):
        product_key_input = drivers[1].find_element(By.ID, "product_key")
        product_key_input.clear()
        product_key_input.send_keys(key[i])
        register_button = drivers[1].find_element(By.ID, "register_btn")
        register_button.click()
        time.sleep(1)
def aza3():
    """ Авто ввод ключей на сайте """
    key = key_string()
    butall = drivers[2].find_element(By.ID, "accept_ssa").click()
    for i in range(20,30):
        product_key_input = drivers[2].find_element(By.ID, "product_key")
        product_key_input.clear()
        product_key_input.send_keys(key[i])
        register_button = drivers[2].find_element(By.ID, "register_btn")
        register_button.click()
        time.sleep(1)
def aza4():
    """ Авто ввод ключей на сайте """
    butall = drivers[3].find_element(By.ID, "accept_ssa").click()
    key = key_string()
    for i in range(30,40):
        product_key_input = drivers[3].find_element(By.ID, "product_key")
        product_key_input.clear()
        product_key_input.send_keys(key[i])
        register_button = drivers[3].find_element(By.ID, "register_btn")
        register_button.click()
        time.sleep(1)

def process_keys():
    """ Переменная для работы всех переменных разом """
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(func) for func in (aza1, aza2, aza3, aza4)]