from selenium import webdriver
import math
from time import sleep
from Examples.fast_test import fill_form
driver = webdriver.Chrome("./chromedriver")
driver.get('http://suninjuly.github.io/find_link_text')
window_after = driver.window_handles[0]
what_to_find=str(math.ceil(math.pow(math.pi, math.e)*10000))
link=driver.find_element_by_link_text(what_to_find)
sleep(2)
link.click()
#window_after = driver.window_handles[1]
#driver.switch_to.window(window_after)
fill_form(driver)

#print(what_to_find)
#driver.quit()