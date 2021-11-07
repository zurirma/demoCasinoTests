import time

import pytest
from selenium import webdriver

class TestsDemoCasino:

    def setup_class(self):
        self.driver = webdriver.Chrome(executable_path=r'C:\Users\llope\PycharmProjects\demoCasinoTests\drivers\chromedriver.exe')
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get('https://demo.casino/')

    @pytest.fixture()
    def access_to_registration_page(self):
        self.driver.find_element_by_xpath('/html/body/div[1]/header/div/div[2]/div[2]/a[2]').click()
        title = self.driver.find_element_by_class_name('page__title').text
        assert title == 'SIGN UP'

    def test_succesful_registration_with_email(self, access_to_registration_page):
        self.driver.find_element_by_id('core__protected_modules_user_yiiForm_RegistrationForm_email').send_keys('ujht@gmail.com')
        self.driver.find_element_by_xpath('//*[@id="registration_form_1"]/fieldset[2]/div[1]/div[1]/div[1]/label').click()
        self.driver.find_element_by_xpath('//*[@id="registration_form_1"]/fieldset[2]/div[2]/label').click()
        self.driver.find_element_by_id('core__protected_modules_user_yiiForm_RegistrationForm_password').send_keys('Ktbspa2')
        self.driver.find_element_by_id('core__protected_modules_user_yiiForm_RegistrationForm_password_confirmation').send_keys('Ktbspa2')
        self.driver.find_element_by_xpath('//*[@id="registration_form_1"]/fieldset[3]/button').click()
        time.sleep(5)
        succesful_registration = self.driver.find_element_by_class_name('notification__title').text
        assert succesful_registration == 'Congratulations!'





    def teardown(self):
        self.driver.close()
        self.driver.quit()


