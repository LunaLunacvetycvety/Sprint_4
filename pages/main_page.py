import allure
from locators.main_page_locators import MainPageLocators as locators
from element.base_page import BasePage


class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.base_page = BasePage(driver)

    @allure.step('Принимаем куки')
    def click_popup_cookies(self):
        self.base_page.click_on_element(locators.pop_up_agreement_cookies)

    @allure.step('Получение ответа на вопрос')
    def get_accordion_text(self, button_id, text_id):
        self.base_page.wait_to_open(button_id, 10)
        self.base_page.click_on_element(button_id)
        return self.base_page.get_text(text_id)
