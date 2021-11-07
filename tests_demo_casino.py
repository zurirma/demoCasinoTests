import pytest
from selenium import webdriver

class TestsDemoCasino:

    def setup_class(self):
        self.driver = webdriver.Chrome(executable_path=r'C:\Users\llope\PycharmProjects\demoCasinoTests\drivers\chromedriver.exe')
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get('https://demo.casino/')

    def test_verify_access_to_registration_page(self):
        self.driver.find_element_by_xpath('/html/body/div[1]/header/div/div[2]/div[2]/a[2]').click()
        title = self.driver.find_element_by_class_name('page__title').text
        assert title == 'SIGN UP'

    def teardown(self):
        self.driver.close()
        self.driver.quit()


