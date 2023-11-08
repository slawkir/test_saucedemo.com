from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.saucedemo.com/')

#чтобы страница после запуска резко не закрывалась
while(True):
    pass