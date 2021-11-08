import time

import pytest
from selenium import webdriver
from assertpy import assert_that
from helpers.page_faqs import PageFaqs


class TestsFaqsPage:
    """Esta clase define la ruta del chromedriver, asi com la url a acceder para que corran las pruebas """

    def setup_class(self):
        self.driver = webdriver.Chrome(
            executable_path=r'C:\Users\llope\PycharmProjects\demoCasinoTests\drivers\chromedriver.exe')
        self.driver.maximize_window()  # maximiza la ventana del browser
        self.driver.implicitly_wait(10)
        self.driver.get('https://demo.casino/')
        self.page_faqs = PageFaqs(self.driver)
        self.clear_cache_answer = '/html/body/div[1]/main/div/div/div/div[1]/ul/li[4]/div[2]'
        self.internet_answer = '/html/body/div[1]/main/div/div/div/div[2]/ul/li[2]/div[2]'

    @pytest.fixture()
    def access_to_registration_page(self):
        self.page_faqs.select_faq_section()
    """Este test valida que se pueda entrar a la seccion en la que aparecen todas las preguntas cargadas"""
    def test_access_to_all_faqs(self, access_to_registration_page):
        self.page_faqs.go_to_all_faqs_section()
        answer = self.driver.find_element_by_xpath(self.clear_cache_answer).text
        assert_that(answer).contains('click the "Clear Now" button')
    """Este test valida que se pueda entrar y ver las respuestas de las preguntas miscelaneas"""
    def test_verify_access_to_others_faqs(self, access_to_registration_page):
        self.page_faqs.go_to_others_section()
        answer_to_others = self.driver.find_element_by_xpath(self.internet_answer).text
        assert_that(answer_to_others).contains('Reboot the router')
    """Este test valida que se pueda entrar y ver las respuestas de las preguntas que tienen que ver con payments"""
    def test_verify_access_to_payments_faqs(self):
        self.page_faqs.go_to_payments_faq_section()
        answer_to_question = self.driver.find_element_by_xpath('/html/body/div[1]/main/div/div/div/div[3]/ul/li/div[2]').text
        assert_that(answer_to_question).contains('Uploading documents')
    """Este test valida que se pueda entrar y ver las respuestas de las preguntas que tienen que ver con games"""
    def test_verify_access_to_games_faqs(self):
        self.page_faqs.got_to_games_faq_section()
        answer = self.driver.find_element_by_xpath('/html/body/div[1]/main/div/div/div/div[4]/ul/li[2]/div[2]').text
        assert_that(answer).contains('Google Chrome and Mozilla Firefox')
    """Este metodo se asegura de cerrar el broser luego de cada ejecucion"""
    def teardown(self):
        self.driver.close()
        self.driver.quit()


