import pytest
from selenium import webdriver
chrome_path="../chromedriver"
from selenium.webdriver.chrome.options import Options
link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture
def browser():
    print("\nstart browser for test..")
    options = Options()
    options.binary_location = "/Applications/Google Chrome 2.app/Contents/MacOS/Google Chrome"
    browser = webdriver.Chrome(options=options, executable_path=chrome_path)
    return browser

@pytest.fixture(scope="class")
def prepare_faces():
    print("^_^", "\n")
    yield
    print(":3", "\n")


@pytest.fixture()
def very_important_fixture():
    print(":)", "\n")


@pytest.fixture(autouse=True)
def print_smiling_faces():
    print(":-Р", "\n")

class TestMainPage1(object):
    # вызываем фикстуру в тесте, передав ее как параметр
    def test_guest_should_see_login_link(self, browser, prepare_faces, very_important_fixture):
        prepare_faces
        very_important_fixture
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser, prepare_faces):
        prepare_faces
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")