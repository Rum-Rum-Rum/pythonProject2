from selenium import webdriver

# Указываем полный путь к geckodriver.exe на вашем ПК.
driver = webdriver.Firefox(executable_path=r'C:\geckodriver\geckodriver.exe')
driver.get("http://www.google.com")
