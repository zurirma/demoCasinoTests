import time


class PageFaqs:
    def __init__(self, driver):
        self.driver = driver
        self.more_button = '/html/body/div[1]/header/div/div[2]/div[1]/ul/li[1]/span'
        self.faq = '/html/body/div[1]/header/div/div[2]/div[1]/ul/li[1]/ul/li[2]/a'
        self.all_faq_section = '/html/body/div[1]/main/div/div/header/div/div/div[3]/div/ul/li[1]'
        self.others_faq_section = '/html/body/div[1]/main/div/div/header/div/div/div[3]/div/ul/li[2]'
        self.payments_faq_section = '/html/body/div[1]/main/div/div/header/div/div/div[3]/div/ul/li[3]'
        self.games_faq_section = '/html/body/div[1]/main/div/div/header/div/div/div[3]/div/ul/li[4]'
        self.clear_cache_question = '/html/body/div[1]/main/div/div/div/div[1]/ul/li[4]/div[1]'
        self.internet_connection_question = '/html/body/div[1]/main/div/div/div/div[2]/ul/li[2]/div[1]'
        self.payments_question = '/html/body/div[1]/main/div/div/div/div[3]/ul/li/div[1]'
        self.game_question = '/html/body/div[1]/main/div/div/div/div[4]/ul/li[2]/div[1]'
        self.clear_cache_answer = '/html/body/div[1]/main/div/div/div/div[1]/ul/li[4]/div[2]'

    def select_faq_section(self):
        self.driver.find_element_by_xpath(self.more_button).click()
        faq_section = self.driver.find_element_by_xpath(self.faq).click()
        return faq_section

    def go_to_all_faqs_section(self):
        self.driver.find_element_by_xpath(self.all_faq_section).click()
        self.driver.find_element_by_xpath(self.clear_cache_question).click()
        question = self.driver.find_element_by_xpath(
            self.clear_cache_question).text
        time.sleep(2)
        return question

    def go_to_others_section(self):
        self.driver.find_element_by_xpath(self.others_faq_section).click()
        self.driver.find_element_by_xpath(self.internet_connection_question).click()
        question_two = self.driver.find_element_by_xpath(
            self.internet_connection_question).text
        time.sleep(2)
        return question_two

    def go_to_payments_faq_section(self):
        self.driver.find_element_by_xpath(self.payments_faq_section).click()
        self.driver.find_element_by_xpath(self.payments_question).click()
        question = self.driver.find_element_by_xpath('/html/body/div[1]/main/div/div/div/div[3]/ul/li/div[1]').text
        time.sleep(2)
        return question

    def got_to_games_faq_section(self):
        self.driver.find_element_by_xpath(self.games_faq_section).click()
        self.driver.find_element_by_xpath(self.game_question).click()
        last_question = self.driver.find_element_by_xpath(
            '/html/body/div[1]/main/div/div/div/div[4]/ul/li[2]/div[1]').text
        time.sleep(2)
        return last_question
