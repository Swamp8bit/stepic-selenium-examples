from selenium import webdriver

site1="http://suninjuly.github.io/selects1.html"
site2="http://suninjuly.github.io/selects2.html"

browser=webdriver.Chrome('./chromedriver')
browser.get(site1)

num1=browser.find_element_by_css_selector("#num1").text
num2=browser.find_element_by_css_selector("#num2").text
sum=str(int(num1)+int(num2))

from selenium.webdriver.support.ui import Select
select = Select(browser.find_element_by_tag_name("select"))
select.select_by_value(sum)
browser.find_element_by_css_selector("button.btn").click()
print(sum)