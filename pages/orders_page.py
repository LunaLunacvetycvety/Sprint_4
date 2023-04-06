import allure
from locators.orders_page_locators import OrdersPageLocators as locators
from element.base_page import BasePage


class OrdersPage:

    def __init__(self, driver):
        self.driver = driver
        self.base_page = BasePage(driver)

    @allure.step('Принимаем куки')
    def click_popup_cookies(self):
        self.base_page.click_on_element(locators.pop_up_agreement_cookies)

    @allure.step('Выбираем кнопку для офррмления заказа')
    def choose_order_button(self, button):
        self.base_page.click_on_element(button)

    @allure.step('Нажимаем кнопку "Заказать" в хедере ')
    def click_order_button_header(self):
        self.base_page.click_on_element(locators.start_order_button_header)

    @allure.step('Нажимаем на поле ввода имени')
    def find_element_and_click_input_name(self):
        self.base_page.click_on_element(locators.input_name)

    @allure.step('Вводим имя')
    def input_name_in(self):
        self.base_page.input_value(locators.input_name, 'Алина')

    @allure.step('Нажимаем на поле ввода фамилии')
    def find_element_and_click_input_surname(self):
        self.base_page.click_on_element(locators.input_surname)

    @allure.step('Вводим фамилию')
    def input_surname_in(self):
        self.base_page.input_value(locators.input_surname, text='Татьянчикова')

    @allure.step('Нажимаем на поле ввода адреса')
    def find_element_and_click_input_address(self):
        self.base_page.click_on_element(locators.input_address)

    @allure.step('Вводим адрес')
    def input_address_in(self):
        self.base_page.input_value(locators.input_address, text='Ломоносовский проспект 24')

    @allure.step('Нажимаем на выбор метро')
    def find_and_click_metro_station(self):
        self.base_page.click_on_element(locators.choose_station_metro)

    @allure.step('Ждем отображение списка станций метро')
    def wait_before_choose_station(self):
        self.base_page.wait_to_open(locators.station_metro, time=10)

    @allure.step('Выбираем станцию метро')
    def click_on_metro_station(self):
        self.base_page.click_on_element(locators.station_metro)

    @allure.step('Нажимаем на поле ввода номера телефона')
    def find_and_click_phone_number(self):
        self.base_page.click_on_element(locators.input_phone_number)

    @allure.step('Вводим номер телефона')
    def input_phone_number_in(self):
        self.base_page.input_value(locators.input_phone_number, text='79134562341')

    @allure.step('Нажимаем кнопку "Далее"')
    def click_next_button(self):
        self.base_page.click_on_element(locators.next_button)

    @allure.step('Нажимаем на выбор даты доставки')
    def find_and_click_when_to_bring_scooter(self):
        self.base_page.click_on_element(locators.when_to_bring_scooter)

    @allure.step('Выбираем дату доставки')
    def choose_when_to_bring_scooter(self):
        self.base_page.click_on_element(locators.input_when_to_bring_scooter)

    @allure.step('Нажимаем на выбор периода аренды')
    def find_and_click_rental_period(self):
        self.base_page.click_on_element(locators.rental_period)

    @allure.step('Выбираем период аренды')
    def choose_rental_period(self):
        self.base_page.click_on_element(locators.input_rental_period)

    @allure.step('Выбираем цвет самоката')
    def choose_color_of_scooter(self):
        self.base_page.click_on_element(locators.color_of_scooter)

    @allure.step('Нажимаем кнопку "Заказать"')
    def click_order_button(self):
        self.base_page.click_on_element(locators.order_button)

    @allure.step('Подтверждаем заказ')
    def click_yes_button(self):
        self.base_page.click_on_element(locators.yes_button)

    @allure.step('Ждем баннер с оповещением об успешном заказе')
    def wait_to_proceed_banner(self):
        self.base_page.wait_to_open(locators.order_processed, time=20)

    @allure.step('Получаем текст кнопки')
    def order_get_text(self):
        return self.base_page.get_text(locators.status_view)

    @allure.step('Нажимаем на логотип Яндекса')
    def click_on_yandex_logo(self):
        self.base_page.click_on_element(locators.logo_yandex)

    @allure.step('Нажимаем на логотип Самоката')
    def click_on_logo_scooter(self):
        self.base_page.click_on_element(locators.logo_scooter)

    @allure.step('Ждем загрузку дзена')
    def wait_to_open_dzen_window(self):
        self.base_page.wait_to_open(locators.dzen_content_div, time=20)

    @allure.step('Получаем текущую ссылку')
    def current_url(self):
        return self.base_page.get_current_url()
