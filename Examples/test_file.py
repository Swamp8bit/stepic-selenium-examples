from selenium import webdriver
import time


def run(test_webdriver):
    test_webdriver.get('https://stepik.org/lesson/25969/step/8')
    time.sleep(5)
    textarea=test_webdriver.find_element_by_css_selector(".textarea")
    textarea.send_keys('get()')
    time.sleep(5)

    submit_button = test_webdriver.find_element_by_css_selector('button.submit-submission')
    submit_button.click()

    time.sleep(5)
    test_webdriver.quit()

if __name__ == "__main__":
    test_webdriver=webdriver.Chrome('./chromedriver')
    run(test_webdriver)