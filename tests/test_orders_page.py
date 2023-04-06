import re

import allure
import pytest
from locators.orders_page_locators import OrdersPageLocators as locators
from pages.orders_page import OrdersPage


class TestHeaderOrder:
    @pytest.mark.parametrize("order_button", [locators.start_order_button_header, locators.start_order_button])
    @allure.title('Проверяем правильно оформленный заказ через хедер и тело страницы')
    @allure.description('Последовательные выполнения действий для заказа самоката')
    def test_header_order(self, driver, order_button):
        orders_page = OrdersPage(driver)
        orders_page.click_popup_cookies()
        orders_page.choose_order_button(order_button)
        orders_page.find_element_and_click_input_name()
        orders_page.input_name_in()
        orders_page.find_element_and_click_input_surname()
        orders_page.input_surname_in()
        orders_page.find_element_and_click_input_address()
        orders_page.input_address_in()
        orders_page.find_and_click_metro_station()
        orders_page.wait_before_choose_station()
        orders_page.click_on_metro_station()
        orders_page.find_and_click_phone_number()
        orders_page.input_phone_number_in()
        orders_page.click_next_button()
        orders_page.find_and_click_when_to_bring_scooter()
        orders_page.choose_when_to_bring_scooter()
        orders_page.find_and_click_rental_period()
        orders_page.choose_rental_period()
        orders_page.choose_color_of_scooter()
        orders_page.click_order_button()
        orders_page.click_yes_button()
        orders_page.wait_to_proceed_banner()

        modal_text = orders_page.order_get_text()
        result = re.search(r"(.+)\n[\S\s]*", modal_text)
        modal_title = result.groups()[0]

        assert modal_title == "Заказ оформлен"

    @allure.title('Проверяем что при нажатии на логотип Яндекса открывается редирект')
    @allure.description('Последовательные выполнения действий для проверки открытия главной страницы Яндекса')
    def test_link_yandex_logo(self, driver):
        order_page = OrdersPage(driver)
        order_page.click_popup_cookies()
        order_page.click_on_yandex_logo()
        order_page.driver.switch_to.window(order_page.driver.window_handles[1])
        order_page.wait_to_open_dzen_window()

        assert order_page.current_url() == 'https://dzen.ru/?yredirect=true'

    @allure.title('Проверяем что при нажатии на логотип Самоката, открывается главная страница Самоката')
    @allure.description('Последовательные выполнения действий для проверки открытия главной страницы Самоката')
    def test_link_scooter_logo(self, driver):
        order_page = OrdersPage(driver)
        order_page.click_popup_cookies()
        order_page.click_order_button_header()
        order_page.click_on_logo_scooter()

        assert order_page.current_url() == 'https://qa-scooter.praktikum-services.ru/'
