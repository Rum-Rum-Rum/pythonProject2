
import unittest

class TestLesson(unittest.TestCase):
    def test_les_1(self):

        from selenium import webdriver
        from selenium.webdriver.common.by import By
        import time

        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element(By.CSS_SELECTOR, '.form-group.first_class input.form-control.first[required]')
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.CSS_SELECTOR, '.form-group.second_class input.form-control.second[required]')
        input2.send_keys("Petrov")
        input2 = browser.find_element(By.CSS_SELECTOR, '.form-group.third_class input.form-control.third[required]')
        input2.send_keys("PetVan@kuku.ru")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Ahtung ! Not work")

        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()

    def test_les_2(self):
        

if __name__ == "__main__":
    unittest.main()