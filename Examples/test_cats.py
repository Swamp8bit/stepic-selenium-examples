site='http://suninjuly.github.io/cats.html'
from selenium import webdriver
chrome_path='./chromedriver'
browser=webdriver.Chrome(chrome_path)
browser.get(site)
browser.find_element_by_id('button')