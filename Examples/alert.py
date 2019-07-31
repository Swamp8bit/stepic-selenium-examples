from selenium import webdriver
import time
browser = webdriver.Chrome('./chromedriver')
browser.execute_script("document.title='Script executing';alert('Robots at work');")
time.sleep(5)
