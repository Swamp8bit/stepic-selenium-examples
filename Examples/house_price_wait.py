from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
options = webdriver.ChromeOptions()

options.add_experimental_option('w3c', False)


browser = webdriver.Chrome( executable_path='./chromedriver',options=options)

browser.get("http://suninjuly.github.io/explicit_wait2.html")

WebDriverWait(browser, 120).until(EC.text_to_be_present_in_element((By.ID, "price"), "10000 RUR"))
browser.find_element_by_id("book").click()
#def calculate_general(browser):
from math import log,sin
def calc(x):
    return str(log(abs(sin(int(x))*12)))
num = browser.find_element_by_css_selector('#input_value').text
browser.find_element_by_css_selector('#answer').send_keys(calc(num))
browser.find_element_by_id("solve").click()
raw_answer=browser.switch_to.alert
answer=raw_answer.text.split(':')[-1]
    #return answer
print (answer)
#calculate_general(browser)
# time.sleep(3)
# browser.quit()