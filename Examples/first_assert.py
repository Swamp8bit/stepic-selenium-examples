from selenium import webdriver
import time

link1 = "http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"
browser = webdriver.Chrome('./chromedriver')
browser.get(link2)


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