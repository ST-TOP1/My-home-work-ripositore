from selenium import webdriver
from selenium.webdriver.common.by import By
import pickle
import time
from vk import *
import concurrent.futures
COOKIE_FILES = ["A1cookies", "A2cookies", "A3cookies", "A4cookies"]


#Создает браузер
def create_browser():
    driver = webdriver.Chrome()
    return driver
#Создаем сесию
def start_process():
    global drivers
    drivers = [create_browser() for _ in COOKIE_FILES]
    # Open Steam pages with cookies
    for i, driver in enumerate(drivers):
        load_cookies(driver, COOKIE_FILES[i])

def load_cookies(driver, cookie_file):
    driver.get("https://store.steampowered.com/account/registerkey")
    with open(cookie_file, "rb") as file:
        cookies = pickle.load(file)
        for cookie in cookies:
            driver.add_cookie(cookie)
    driver.refresh()

maskey = [
    [0,10],
    [10,20],
    [20,30],
    [30,40]
]

def aza1():
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
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(func) for func in (aza1, aza2, aza3, aza4)]