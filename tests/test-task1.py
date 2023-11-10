import time

import selenium
from selenium import webdriver
from selenium.common import NoSuchElementException

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get('https://www.saucedemo.com/')


# Шаг 1. Авторизация в приложении.
def auth_test():
    user_name = driver.find_element(By.ID, 'user-name')
    user_name.send_keys("performance_glitch_user")
    user_pass = driver.find_element(By.ID, 'password')
    user_pass.send_keys('secret_sauce')
    login_btn = driver.find_element(By.ID, 'login-button')
    login_btn.click()
    time.sleep(1)
    # обработка, если введен правильные/неправильные данные при авторизации (логин-пароль)
    while True:
        try:
            driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/span')
            print("Авторизация пройдена")
            break
        except:
            print("Неверные логин/пароль.")
            break

#Шаг 2. Добавить товар Sauce Labs Fleece Jacket в корзину (нажать кнопку ADD TO CART)
def add_to_cart_Sauce_Labs_Fleece():
    time.sleep(2) # чтобы визуально отследить добавление товара в корзину
    btn_add_to_cart_sauce_labs_fleece_jacket = driver.find_element(By.ID, 'add-to-cart-sauce-labs-fleece-jacket')
    btn_add_to_cart_sauce_labs_fleece_jacket.click()
    time.sleep(1)
    while True:
        try:
            driver.find_element(By.ID, 'remove-sauce-labs-fleece-jacket')
            print("Товар Sauce Labs Fleece Jacket добавлен в корзину")
            break
        except:
            print("Ошибка выбора товара")
            break

# Шаг 3. Перейти в корзину нажатием кнопки сверху в правом углу в виде корзины
def go_to_cart():
    shopping_cart = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a')
    shopping_cart.click()

    while True:
        try:
            driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/span')
            print("Переход в корзину")
            break
        except:
            print("Ошибка, переход в корзину не состоялся")
            break


# Шаг 4. Нажать кнопку CONTINUE SHOPPING
def continue_shoping():
    time.sleep(1)
    btn_continue_shopping = driver.find_element(By.ID, 'continue-shopping')
    btn_continue_shopping.click()
    while True:
        try:
            driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/span')
            print('Открытие главной страницы приложения с товарами')
            break
        except:
            print("Ошибка, переход главную страницу не состоялся")
            break

#Шаг 5.  Добавить товар Sauce Labs Bolt T-Shirt в корзину (нажать кнопку ADD TO CART)
def add_to_cart_tshirt():
    time.sleep(3)
    btn_add_to_cart_sauce_labs_bolt_t_shirt = driver.find_element(By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt')
    btn_add_to_cart_sauce_labs_bolt_t_shirt.click()

    while True:
        try:
            driver.find_element(By.ID, 'remove-sauce-labs-bolt-t-shirt')
            print('Товар Sauce Labs Bolt T-Shirt добавлен в корзину')
            break
        except:
            print("Ошибка, Товар Sauce Labs Bolt T-Shirt не добавлен в корзину")
            break

# Шаг 6.  Перейти в корзину нажатием кнопки сверху в правом углу в виде корзины



auth_test()
add_to_cart_Sauce_Labs_Fleece()
go_to_cart()
continue_shoping()
add_to_cart_tshirt()
go_to_cart()

time.sleep(5)
