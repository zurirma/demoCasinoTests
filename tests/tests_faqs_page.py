import time

import pytest
from selenium import webdriver
from assertpy import assert_that


class TestsFaqsPage:
    """Esta clase define la ruta del chromedriver, asi com la url a acceder para que corran las pruebas """

    def setup_class(self):
        self.driver = webdriver.Chrome(
            executable_path=r'C:\Users\llope\PycharmProjects\demoCasinoTests\drivers\chromedriver.exe')
        self.driver.maximize_window()  # maximiza la ventana del browser
        self.driver.implicitly_wait(10)
        self.driver.get('https://demo.casino/')

    def test_access_to_all_faqs(self):
        self.driver.find_element_by_xpath('/html/body/div[1]/header/div/div[2]/div[1]/ul/li[1]/span').click()
        self.driver.find_element_by_xpath('/html/body/div[1]/header/div/div[2]/div[1]/ul/li[1]/ul/li[2]/a').click()
        self.driver.find_element_by_xpath('/html/body/div[1]/main/div/div/header/div/div/div[3]/div/ul/li[1]').click()
        self.driver.find_element_by_xpath('/html/body/div[1]/main/div/div/div/div[1]/ul/li[4]/div[1]').click()
        question_four = self.driver.find_element_by_xpath('/html/body/div[1]/main/div/div/div/div[1]/ul/li[4]/div[1]').text
        time.sleep(2)
        answer = self.driver.find_element_by_xpath('/html/body/div[1]/main/div/div/div/div[1]/ul/li[4]/div[2]').text
        time.sleep(3)
        assert_that(question_four).contains('Clear cache')
        assert_that(answer).contains('click the "Clear Now" button')

    def test_verify_access_to_others_faqs(self):
        self.driver.find_element_by_xpath('/html/body/div[1]/header/div/div[2]/div[1]/ul/li[1]/span').click()
        self.driver.find_element_by_xpath('/html/body/div[1]/header/div/div[2]/div[1]/ul/li[1]/ul/li[2]/a').click()
        self.driver.find_element_by_xpath('/html/body/div[1]/main/div/div/header/div/div/div[3]/div/ul/li[2]').click()
        self.driver.find_element_by_xpath('/html/body/div[1]/main/div/div/div/div[2]/ul/li[2]/div[1]').click()
        question_two = self.driver.find_element_by_xpath('/html/body/div[1]/main/div/div/div/div[2]/ul/li[2]/div[1]').text
        time.sleep(2)
        answer_to_others = self.driver.find_element_by_xpath('/html/body/div[1]/main/div/div/div/div[2]/ul/li[2]/div[2]').text
        assert_that(question_two).contains('Internet')
        assert_that(answer_to_others).contains('Reboot the router')

    def test_verify_access_to_payments_faqs(self):
        self.driver.find_element_by_xpath('/html/body/div[1]/header/div/div[2]/div[1]/ul/li[1]/span').click()
        self.driver.find_element_by_xpath('/html/body/div[1]/header/div/div[2]/div[1]/ul/li[1]/ul/li[2]/a').click()
        self.driver.find_element_by_xpath('/html/body/div[1]/main/div/div/header/div/div/div[3]/div/ul/li[3]').click()
        self.driver.find_element_by_xpath('/html/body/div[1]/main/div/div/div/div[3]/ul/li/div[1]').click()
        question = self.driver.find_element_by_xpath('/html/body/div[1]/main/div/div/div/div[3]/ul/li/div[1]').text
        time.sleep(2)
        answer_to_question = self.driver.find_element_by_xpath('/html/body/div[1]/main/div/div/div/div[3]/ul/li/div[2]').text
        assert_that(question).contains('Why upload documents')
        assert_that(answer_to_question).contains('Uploading documents')

    def test_verify_access_to_games_faqs(self):
        self.driver.find_element_by_xpath('/html/body/div[1]/header/div/div[2]/div[1]/ul/li[1]/span').click()
        self.driver.find_element_by_xpath('/html/body/div[1]/header/div/div[2]/div[1]/ul/li[1]/ul/li[2]/a').click()
        self.driver.find_element_by_xpath('/html/body/div[1]/main/div/div/header/div/div/div[3]/div/ul/li[4]').click()
        self.driver.find_element_by_xpath('/html/body/div[1]/main/div/div/div/div[4]/ul/li[2]/div[1]').click()
        last_question = self.driver.find_element_by_xpath('/html/body/div[1]/main/div/div/div/div[4]/ul/li[2]/div[1]').text
        time.sleep(2)
        answer = self.driver.find_element_by_xpath('/html/body/div[1]/main/div/div/div/div[4]/ul/li[2]/div[2]').text
        assert last_question == 'I can not enter the game'
        assert_that(answer).contains('Google Chrome and Mozilla Firefox')



    def teardown(self):
        self.driver.close()
        self.driver.quit()


