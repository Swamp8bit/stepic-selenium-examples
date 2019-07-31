from selenium import webdriver
import math
browser=webdriver.Chrome('./chromedriver')
browser.get('http://suninjuly.github.io/get_attribute.html')
x_element=browser.find_element_by_tag_name('img')
x=x_element.get_attribute('valuex')
#print(x)
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
x_calc=calc(x)
input_x=browser.find_element_by_css_selector('#answer')
input_x.send_keys(x_calc)

browser.find_element_by_css_selector('#robotCheckbox').click()
browser.find_element_by_css_selector('#robotsRule').click()
browser.find_element_by_css_selector('button.btn').click()