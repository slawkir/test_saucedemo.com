# сортировка «High to low»

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
time.sleep(2)


#Шаг 2. Нажать на выпадающий список
product_sort_container = driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/div/span/select')
product_sort_container.click()
print('Клик по выпадающему списку')
time.sleep(5)

# Шаг 3. Клик по элементу "Price (high to low)"
option_high_low = driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/div/span/select/option[4]')
option_high_low.click()
print('Клик по элементу "Price (high to low)"')
time.sleep(5)