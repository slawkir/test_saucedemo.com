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



product_prices_webelements = driver.find_elements(By.CLASS_NAME, 'inventory_item_price')
product_prices_value_text = []
product_prices_value_number = []

for element in product_prices_webelements:
    product_prices_value_text.append(element.text.replace('$', ''))

print(product_prices_value_text)

for element in product_prices_value_text:
    product_prices_value_number.append(float(element))
print(product_prices_value_number)

product_prices_value_number_sort = sorted(product_prices_value_number, reverse=True)

if product_prices_value_number_sort == product_prices_value_number:
    print("Продукты отсортированы по убыванию  цены")
else:
    print("Ошибка сортировки")


time.sleep(5)
driver.close()