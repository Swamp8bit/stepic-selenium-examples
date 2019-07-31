from selenium import webdriver
import math
browser=webdriver.Chrome('./chromedriver')
browser.get('http://suninjuly.github.io/math.html')
x_element=browser.find_element_by_css_selector('label:nth-child(1)>span#input_value ')
x=x_element.text
#print(x)
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
x_calc=calc(x)
input_x=browser.find_element_by_css_selector('#answer')
input_x.send_keys(x_calc)

browser.find_element_by_xpath('//label[@for="robotCheckbox"]').click()
browser.find_element_by_xpath('//label[@for="robotsRule"]').click()
browser.find_element_by_css_selector('button.btn').click()
#browser.quit()