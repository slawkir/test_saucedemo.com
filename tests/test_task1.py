import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.saucedemo.com/')


# Шаг 1. Авторизация в приложении.

user_name = driver.find_element(By.ID, 'user-name')
user_name.send_keys("performance_glitch_user")

user_pass = driver.find_element(By.ID, 'password')
user_pass.send_keys('secret_sauce')

login_btn = driver.find_element(By.ID, 'login-button')
login_btn.click()

print('Авторизация')


# Шаг 2. Добавить товар Sauce Labs Fleece Jacket в корзину (нажать кнопку ADD TO CART)

time.sleep(2) # чтобы визуально отследить добавление товара в корзину

btn_add_to_cart = driver.find_element(By.ID, 'add-to-cart-sauce-labs-fleece-jacket')
btn_add_to_cart.click()

print('Добавление товара')


# Шаг 3. Перейти в корзину нажатием кнопки сверху в правом углу в виде корзины

time.sleep(2)

shopping_cart = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a')
shopping_cart.click()

print('Переход в корзину')

#чтобы страница после запуска резко не закрывалась
while(True):
    pass