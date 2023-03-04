import allure
from selenium import webdriver
from pages.orders_page import OrdersPage


class TestHeaderOrder:
    driver: webdriver

    @allure.title('Проверяем правильно оформленный заказ через кнопку "Заказать" в хедере')
    @allure.description('Последовательные выполнения действий для заказа самоката')
    def test_header_order(self, driver):
        driver.get('https://qa-scooter.praktikum-services.ru/')
        order_page = OrdersPage(driver)
        order_page.checkout_process(order_page.order_button_header, 'Алина', 'Татьянчикова', 'Ломоносовский проспект 33', '79137284647')

        assert order_page.order_text_pattern == order_page.order_get_text()

    @allure.title('Проверяем правильно оформленный заказ через кнопку "Заказать" в теле страницы')
    @allure.description('Последовательные выполнения действий для заказа самоката')
    def test_button_order(self, driver):
        driver.get('https://qa-scooter.praktikum-services.ru/')
        order_page = OrdersPage(driver)
        order_page.checkout_process(order_page.order_button_not_header, 'Евгений', 'Татьянчиков', 'Ленинский проспект 44', '79036266152')

        assert order_page.order_text_pattern == order_page.order_get_text()

    @allure.title('Проверяем что при нажатии на логотип Яндекса открывается редирект')
    @allure.description('Последовательные выполнения действий для проверки открытия главной страницы Яндекса')
    def test_link_yandex_logo(self, driver):
        driver.get('https://qa-scooter.praktikum-services.ru/')
        order_page = OrdersPage(driver)
        order_page.accept_cookie()
        order_page.click_on_yandex_logo()
        order_page.driver.switch_to.window(order_page.driver.window_handles[1])
        order_page.wait_to_open_dzen_window()

        assert order_page.current_url() == 'https://dzen.ru/?yredirect=true'

    @allure.title('Проверяем что при нажатии на логотип Самоката, открывается главная страница Самоката')
    @allure.description('Последовательные выполнения действий для проверки открытия главной страницы Самоката')
    def test_link_scooter_logo(self, driver):
        driver.get('https://qa-scooter.praktikum-services.ru/')
        order_page = OrdersPage(driver)
        order_page.open(order_page.order_button_header)
        order_page.click_on_logo_scooter()

        assert order_page.current_url() == 'https://qa-scooter.praktikum-services.ru/'
