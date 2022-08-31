from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#lesson6_step4.py

try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element(By.CSS_SELECTOR, 'input.form-control.first')
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.CSS_SELECTOR, 'input.form-control.second')
    input2.send_keys("Petrov")
    input2 = browser.find_element(By.CSS_SELECTOR, 'input.form-control.third')
    input2.send_keys("PetVan@kuku.ru")
    input2 = browser.find_element(By.CSS_SELECTOR, 'input.form-control.first')
    input2.send_keys("+79216502452")
    input2 = browser.find_element(By.CSS_SELECTOR, 'input.form-control.second')
    input2.send_keys("Gorilovo")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(10)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
 #   assert "Congratulations! You have successfully registered!" == welcome_text

    if "Congratulations! You have successfully registered!" == welcome_text:
        print('OK!')
    else:
        print('WRONG!')





finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла