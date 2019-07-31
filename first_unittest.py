from selenium import webdriver
import pytest
import time
from unittest import TestCase
from selenium.webdriver.chrome.options import Options
class TestSeleniumFirst(TestCase):
    def setUp(self):       

        link1 = "http://suninjuly.github.io/registration1.html"
        link2 = "http://suninjuly.github.io/registration2.html"

        options = Options()
        options.binary_location = "/Applications/Google Chrome 2.app/Contents/MacOS/Google Chrome"


        self.browser1 = webdriver.Chrome(options=options, executable_path="./chromedriver")
        self.browser1.get(link1)
        self.browser2 = webdriver.Chrome(options=options, executable_path="./chromedriver")
        self.browser2.get(link2)

    def test_registration1(self):

        browser=self.browser1
        # Ваш код, который заполняет обязательные поля
        name=browser.find_element_by_css_selector('.first_block > .first_class > input.first')
        name.send_keys("Иван")
        surname=browser.find_element_by_css_selector('.first_block > .second_class > input.second')
        surname.send_keys("Иванов")
        email=browser.find_element_by_css_selector('.first_block > .third_class > input.third')
        email.send_keys("local@local.local")


    # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Поздравляем! Вы успешно зарегистировались!" == welcome_text
        self.assertEqual(welcome_text, "Поздравляем! Вы успешно зарегистировались!")

    def test_registration2(self):
        # Ваш код, который заполняет обязательные поля
        browser=self.browser2
        name=browser.find_element_by_css_selector('.first_block > .first_class > input.first')
        name.send_keys("Иван")
        surname=browser.find_element_by_css_selector('.first_block > .second_class > input.second')
        surname.send_keys("Иванов")
        email=browser.find_element_by_css_selector('.first_block > .third_class > input.third')
        email.send_keys("local@local.local")


    # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Поздравляем! Вы успешно зарегистировались!" == welcome_text
        self.assertEqual(welcome_text, "Поздравляем! Вы успешно зарегистировались!")

