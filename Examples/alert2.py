
site='http://suninjuly.github.io/redirect_accept.html'
from selenium import webdriver
chrome_path='./chromedriver'
browser=webdriver.Chrome(chrome_path)
browser.get(site)

browser.find_element_by_css_selector('button.btn').click()
new_window=browser.window_handles[1]
old_windows=browser.window_handles[0]
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
browser.switch_to.window(new_window)
print(calculate_general(browser))
