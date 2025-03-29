from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pickle
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from password import password
names = ['Акаунт 1', 'Акаунт 2', 'Акаунт 3', 'Акаунт 4']


def create_browser_cok():
    driver = webdriver.Chrome()
    driver.get('https://store.steampowered.com/login/?l=russian')
    return driver
#Создаем сесию
def start_process_cok():
    global drivers
    drivers = [create_browser_cok() for _ in names]
    
def login():
    for i, driver in enumerate(drivers):
        log = driver.find_element(By.CLASS_NAME , "_2GBWeup5cttgbTw8FM3tfx")
        log.send_keys(names[i])
        passw = driver.find_element(By.XPATH, "//input[@type='password']")
        passw.send_keys(password)
        cleclog = driver.find_element(By.CLASS_NAME, 'DjSvCZoKKfoNSmarsEcTS').click()

def rewrite():
    for i, drive in enumerate(drivers):
        pickle.dump(drive.get_cookies(), open(f'{names[i]}cookies', 'wb'))