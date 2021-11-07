import pytest
from selenium import webdriver

class TestsDemoCasino:

    def setup_class(self):
        self.driver = webdriver.Chrome(executable_path=r'C:\Users\llope\PycharmProjects\demoCasinoTests\drivers\chromedriver.exe')
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get('https://demo.casino/')

    def test_1(self):
        assert True

