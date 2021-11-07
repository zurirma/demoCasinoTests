import time

import pytest
from selenium import webdriver
from helpers.page_registration import PageRegistration


class TestsRegistration:
    """Esta clase define la ruta del chromedriver, asi com la url a acceder para que corran las pruebas """

    def setup_class(self):
        self.driver = webdriver.Chrome(
            executable_path=r'C:\Users\llope\PycharmProjects\demoCasinoTests\drivers\chromedriver.exe')
        self.driver.maximize_window()  # maximiza la ventana del browser
        self.driver.implicitly_wait(10)
        self.driver.get('https://demo.casino/')
        self.page_registration = PageRegistration(self.driver)

    @pytest.fixture()  # la fixture es aquel metodo o funcion que debe correr como precondicion antes de que se corra el test que lo invoca
    def access_to_registration_page(self):
        self.page_registration.select_registration()

    def test_succesful_registration_with_email(self, access_to_registration_page):
        self.page_registration.complete_registration_with_email()
        time.sleep(5)
        succesful_registration = self.driver.find_element_by_class_name('page__title').text
        assert succesful_registration == 'Congratulations!'

    """En las pruebas de la pagina registration nos encontramos con que hay un captcha, el cual no se puede automatizar.  La idea 
    de que exista un captcha es de que el mismo no pueda ser descifrado por una maquina.  Usualmente ante esto se le solicita al equipo de devs que en el
    ambiente de pruebas esta validacion no exista.  Por lo anteriormente expuesto, en este environment los tests de registro no pueden ser 
    completados exitosamente"""

    def test_validate_registration_with_phone_captcha_field_empty_cannot_be_succesful(self, access_to_registration_page):
        self.page_registration.complete_registration_with_phone()
        uncompleted_registration = self.driver.find_element_by_class_name('page__title').text
        assert uncompleted_registration == 'SIGN UP'
    """Aqui se realizo una prueba usando numero de telefono para registro, en el que se verifica que no permite culminar el
    proceso por no colocar el captcha mandatorio"""

    def teardown(self):
        self.driver.close()
        self.driver.quit()
