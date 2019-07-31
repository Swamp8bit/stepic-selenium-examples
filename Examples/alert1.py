
import time

site='http://suninjuly.github.io/alert_accept.html'
def initialize(site):
    from selenium import webdriver
    chrome_path='./chromedriver'
    driver=webdriver.Chrome(chrome_path)
    driver.get(site)
    return driver
browser=initialize(site)
browser.find_element_by_css_selector('button.btn').click()
alert=browser.switch_to.alert
alert.accept()

def calculate_general(browser):
    from math import log,sin
    def calc(x):
        return str(log(abs(sin(int(x))*12)))
    num = browser.find_element_by_css_selector('#input_value').text
    browser.find_element_by_css_selector('#answer').send_keys(calc(num))
    browser.find_element_by_css_selector("button.btn").click()
    raw_answer=browser.switch_to.alert
    answer=raw_answer.text.split(':')[-1]
    return answer

print(calculate_general(browser))
browser.quit()