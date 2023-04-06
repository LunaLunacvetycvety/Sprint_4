import allure
import pytest
from selenium import webdriver
from locators.main_page_locators import MainPageLocators as locators
from pages.main_page import MainPage


class TestMainPageFAQ:
    @allure.title('Проверка аккордеона')
    @allure.description('Последовательное выполнение шагов для проверки текста в выпадающем списке')
    @pytest.mark.parametrize("button_id, text_id, expected", [
        (locators.accordion__heading_button_0, locators.check_accordion__heading_button_0_text, locators.text_accordion_heading_0),
        (locators.accordion__heading_button_1, locators.check_accordion__heading_button_1_text, locators.text_accordion_heading_1),
        (locators.accordion__heading_button_2, locators.check_accordion__heading_button_2_text, locators.text_accordion_heading_2),
        (locators.accordion__heading_button_3, locators.check_accordion__heading_button_3_text, locators.text_accordion_heading_3),
        (locators.accordion__heading_button_4, locators.check_accordion__heading_button_4_text, locators.text_accordion_heading_4),
        (locators.accordion__heading_button_5, locators.check_accordion__heading_button_5_text, locators.text_accordion_heading_5),
        (locators.accordion__heading_button_6, locators.check_accordion__heading_button_6_text, locators.text_accordion_heading_6),
        (locators.accordion__heading_button_7, locators.check_accordion__heading_button_7_text, locators.text_accordion_heading_7),
    ])
    def test_click_accordion_heading_button(self, driver, button_id, text_id, expected):
        main_page = MainPage(driver)
        main_page.click_popup_cookies()
        text = main_page.get_accordion_text(button_id, text_id)

        assert text == expected
