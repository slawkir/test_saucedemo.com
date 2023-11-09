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


#чтобы страница после запуска резко не закрывалась
while(True):
    pass