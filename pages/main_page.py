import allure
from element.base_page import BasePage


class MainPage(BasePage):

    @allure.step('Получение ответа на вопрос')
    def get_accordion_text(self, button_id, text_id):
        self.wait_to_open(button_id, 10)
        self.click_on_element(button_id)
        return self.get_text(text_id)
