import allure
import pytest
from selenium import webdriver
import pages.main_page as page


class TestMainPageFAQ:
    driver: webdriver

    @allure.title('Проверка аккордеона')
    @allure.description('Последовательное выполнение шагов для проверки текста в выпадающем списке')
    @pytest.mark.parametrize("button_id, text_id, expected", [
        (page.accordion__heading_button_0, page.check_accordion__heading_button_0_text, page.text_accordion_heading_0),
        (page.accordion__heading_button_1, page.check_accordion__heading_button_1_text, page.text_accordion_heading_1),
        (page.accordion__heading_button_2, page.check_accordion__heading_button_2_text, page.text_accordion_heading_2),
        (page.accordion__heading_button_3, page.check_accordion__heading_button_3_text, page.text_accordion_heading_3),
        (page.accordion__heading_button_4, page.check_accordion__heading_button_4_text, page.text_accordion_heading_4),
        (page.accordion__heading_button_5, page.check_accordion__heading_button_5_text, page.text_accordion_heading_5),
        (page.accordion__heading_button_6, page.check_accordion__heading_button_6_text, page.text_accordion_heading_6),
        (page.accordion__heading_button_7, page.check_accordion__heading_button_7_text, page.text_accordion_heading_7),

    ])
    def test_click_accordion_heading_button(self, driver, button_id, text_id, expected):
        main_page = page.MainPage(driver)
        main_page.driver.get('https://qa-scooter.praktikum-services.ru/')
        main_page.click_popup_cookies()

        text = main_page.get_accordion_text(button_id, text_id)

        assert text == expected
