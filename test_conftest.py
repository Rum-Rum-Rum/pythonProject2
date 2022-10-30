
from selenium.webdriver.common.by import By

link = "https://stepik.org/lesson/236895/step/1"

def test_guest_should_see_login_link(browser):
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#login_link")
