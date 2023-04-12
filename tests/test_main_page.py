import allure
import pytest
from locators.main_page_locators import MainPageLocators as locators
from pages.main_page import MainPage


class TestMainPageFAQ:
    @allure.title('Проверка аккордеона')
    @allure.description('Последовательное выполнение шагов для проверки текста в выпадающем списке')
    @pytest.mark.parametrize("button_id, text_id, expected", [
        (locators.heading_button_0, locators.check_accordion_0, locators.text_accordion_0),
        (locators.heading_button_1, locators.check_accordion_1, locators.text_accordion_1),
        (locators.heading_button_2, locators.check_accordion_2, locators.text_accordion_2),
        (locators.heading_button_3, locators.check_accordion_3, locators.text_accordion_3),
        (locators.heading_button_4, locators.check_accordion_4, locators.text_accordion_4),
        (locators.heading_button_5, locators.check_accordion_5, locators.text_accordion_5),
        (locators.heading_button_6, locators.check_accordion_6, locators.text_accordion_6),
        (locators.heading_button_7, locators.check_accordion_7, locators.text_accordion_7),
    ])
    def test_click_accordion_heading_button(self, driver, button_id, text_id, expected):
        main_page = MainPage(driver)
        text = main_page.get_accordion_text(button_id, text_id)

        assert text == expected, 'Ответы на вопрос должны совпадать с полученными ответами со страницы'
