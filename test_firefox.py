from selenium import webdriver
import pytest
# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера

@pytest.fixture
def browser_firefox():
    print("\n start browser for test... ")
    browser = webdriver.Firefox()
    yield browser
    print ("\n quit browser ")
    browser.quit()


def test_firefox_open(browser_firefox):
    browser_firefox.get("https://stepik.org/lesson/25969/step/8")

