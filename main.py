
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

ans_t = ' '

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    print("\nquit browser..")
    # time.sleep(3)
    browser.quit()

@pytest.mark.parametrize('link_s', ["https://stepik.org/lesson/236895/step/1", "https://stepik.org/lesson/236896/step/1", "https://stepik.org/lesson/236897/step/1", "https://stepik.org/lesson/236898/step/1",
"https://stepik.org/lesson/236899/step/1", "https://stepik.org/lesson/236903/step/1", "https://stepik.org/lesson/236904/step/1", "https://stepik.org/lesson/236905/step/1"])
class TestLink:
    def test_guest_should_see_login_link(self, browser, link_s):
        num_b = str(math.log(int(time.time() + 2)))
        link = link_s
        browser.get(link)
        n = browser.find_element(By.CSS_SELECTOR, '.textarea')
        n.send_keys(num_b)

        button = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.submit-submission")))
        button.click()

        # находим элемент, содержащий текст
        text_elt = browser.find_element(By.CSS_SELECTOR, 'p.smart-hints__hint')
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        w_text = text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Correct!" == w_text

        print(w_text)
        if w_text != "Correct!":
            ans_t += w_text
            print(ans_t)


if __name__ == "__main__":
    pytest.main()

print(ans_t)