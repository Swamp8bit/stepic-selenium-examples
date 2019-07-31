from selenium import webdriver
from  math import log,  sin
import time
browser=webdriver.Chrome('./chromedriver')
browser.get('https://suninjuly.github.io/execute_script.html')
def calc(x):
    return str(log(abs(sin(int(x))*12)))
num = browser.find_element_by_css_selector('#input_value').text
browser.find_element_by_css_selector('#answer').send_keys(calc(num))
browser.find_element_by_xpath("//label[@for='robotCheckbox']").click()
#browser.execute_script("button = document.getElementsByTagName('button')[0];button.scrollIntoView();")

browser.execute_script("window.scrollBy(0, 200);")
browser.find_element_by_xpath("//label[@for='robotsRule']").click()

browser.find_element_by_css_selector("button.btn").click()
#browser.execute_script("window.scrollBy(0, 100);")

time.sleep(10)
browser.quit()
