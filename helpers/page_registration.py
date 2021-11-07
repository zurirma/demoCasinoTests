
class PageRegistration:
    def __init__(self, driver):
        self.driver = driver
        self.registration_button = '/html/body/div[1]/header/div/div[2]/div[2]/a[2]'
        self.page_title = 'page__title'
        self.email = 'core__protected_modules_user_yiiForm_RegistrationForm_email'
        self.phone = 'core__protected_modules_user_yiiForm_RegistrationForm_phone'
        self.eur_currency = '//*[@id="registration_form_1"]/fieldset[2]/div[1]/div[1]/div[1]/label'
        self.usd_currency = '//*[@id="registration_form_1"]/fieldset[2]/div[1]/div[1]/div[1]/label'
        self.terms_and_conditions = '//*[@id="registration_form_1"]/fieldset[2]/div[2]/label'
        self.password = 'core__protected_modules_user_yiiForm_RegistrationForm_password'
        self.confirm_password = 'core__protected_modules_user_yiiForm_RegistrationForm_password_confirmation'
        self.finish_registration = '//*[@id="registration_form_1"]/fieldset[3]/button'

    def select_registration(self):
        page_registration = self.driver.find_element_by_xpath(self.registration_button).click()
        return page_registration

    def complete_registration_with_email(self):
        self.driver.find_element_by_id(self.email).send_keys('ujht@gmail.com')
        self.driver.find_element_by_xpath(self.eur_currency).click()
        self.driver.find_element_by_xpath(self.terms_and_conditions).click()
        self.driver.find_element_by_id(self.password).send_keys('Ktbspa2')
        self.driver.find_element_by_id(self.confirm_password).send_keys('Ktbspa2')
        self.driver.find_element_by_xpath(self.finish_registration).click()

    def complete_registration_with_phone(self):
        self.driver.find_element_by_id(self.phone).send_keys(1154186767)
        self.driver.find_element_by_xpath(self.usd_currency).click()
        self.driver.find_element_by_xpath(self.terms_and_conditions).click()
        self.driver.find_element_by_id(self.password).send_keys('Ktbspa2')
        self.driver.find_element_by_id(self.confirm_password).send_keys('Ktbspa2')
        self.driver.find_element_by_xpath(self.finish_registration).click()
