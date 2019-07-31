import time
import math
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def browser():
    print("\n start browser for test... ")
    options = Options()
    options.binary_location = "/Applications/Google Chrome 2.app/Contents/MacOS/Google Chrome"
    browser = webdriver.Chrome(options=options, executable_path="../chromedriver")
    yield browser
    print ("\n quit browser ")
    browser.quit()



LINKS = ["https://stepik.org/lesson/236896/step/1",
        "https://stepik.org/lesson/236897/step/1",
        "https://stepik.org/lesson/236898/step/1",
        "https://stepik.org/lesson/236895/step/1",
        "https://stepik.org/lesson/236899/step/1",
        "https://stepik.org/lesson/236903/step/1",
        "https://stepik.org/lesson/236904/step/1",
        "https://stepik.org/lesson/236905/step/1"]


@pytest.mark.parametrize('link', LINKS)
#@pytest.mark.xfail(strict=True)
class TestUFOLinks(object):
    sentence = ""
    def test_check_notes(self, browser, link):

        link=link
        browser.get(link)
        ANSWER = math.log(int(time.time()))
        answer=str(ANSWER)
        print(f"the answer {answer} is going to be entered in link {link}")
        text_area=WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "textarea.textarea"))
        )
        text_area.send_keys(answer)
        button = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission"))
        )
        button.click()
        hint=WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "smart-hints__hint"))
        )
        hint=hint.text

        if hint != "Correct!":
            self.sentence+=hint
        print(f"The sentence is {self.sentence}")
        assert hint=="Correct!"
