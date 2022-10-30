
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC





@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('link_s', ["https://stepik.org/lesson/236895/step/1", "https://stepik.org/lesson/236896/step/1"])
class TestLink:
    def test_guest_should_see_login_link(self, browser, link_s):
        num_ber = answer = str(math.log(int(time.time())))
        link = link_s
        browser.get(link)
        input1 = browser.find_element(By.CSS_SELECTOR, '#ember110')
        input1.send_keys(num_ber)


        button = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.submit-submission")))
        button.click()

