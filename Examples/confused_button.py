from Examples.fast_test import fill_form
from selenium import webdriver
where_to_click='//button[@type="submit"]'
site="http://suninjuly.github.io/find_xpath_form"
browser = webdriver.Chrome('./chromedriver')
browser.get(site)
fill_form(browser,where_to_click)
