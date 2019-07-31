from selenium import webdriver
import os
import time
browser=webdriver.Chrome('./chromedriver')
browser.get('http://suninjuly.github.io/file_input.html')

browser.find_element_by_xpath("//input[@name='firstname']").send_keys('Ivan')
browser.find_element_by_xpath("//input[@name='lastname']").send_keys('Ivanov')
browser.find_element_by_xpath("//input[@name='email']").send_keys('local@local.com')


current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
file_path = os.path.join(current_dir, 'upload.txt') # добавляем к этому пути имя файла 
print(file_path)
browser.find_element_by_css_selector('#file').send_keys(file_path)
    
browser.find_element_by_css_selector('button.btn').click()

time.sleep(5)
browser.quit()