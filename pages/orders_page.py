import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class OrdersPage:
    driver = None

    pop_up_agreement_cookies = [By.ID, 'rcc-confirm-button']
    order_button_header = [By.CLASS_NAME, 'Button_Button__ra12g']
    input_name = [By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[1]/input']
    input_surname = [By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[2]/input']
    input_address = [By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[3]/input']
    choose_station_metro = [By.CLASS_NAME, 'select-search__value']
    station_metro = [By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[4]/div/div[2]/ul/li[3]/button']
    input_phone_number = [By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[5]/input']
    next_button = [By.XPATH, '//*[@id="root"]/div/div[2]/div[3]/button']
    when_to_bring_scooter = [By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[1]/div[1]/div/input']
    input_when_to_bring_scooter = [By.XPATH,
                                   '//*[@id="root"]/div/div[2]/div[2]/div[1]/div[2]/div[2]/div/div/div[2]/div[2]/div[3]/div[1]']
    rental_period = [By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[2]/div/div[1]']
    input_rental_period = [By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[2]/div[2]/div[2]']
    color_of_scooter = [By.XPATH, '//*[@id="black"]']
    order_button = [By.XPATH, '//*[@id="root"]/div/div[2]/div[3]/button[2]']
    yes_button = [By.XPATH, '//*[@id="root"]/div/div[2]/div[5]/div[2]/button[2]']
    order_processed = [By.CLASS_NAME, 'Order_Modal__YZ-d3']
    order_processed_text = [By.XPATH, '/html/body/div/div/div[2]/div[5]/div[1]']
    order_button_not_header = [By.XPATH, '//*[@id="root"]/div/div/div[4]/div[2]/div[5]/button']
    logo_yandex = [By.CLASS_NAME, 'Header_LogoYandex__3TSOI']
    logo_scooter = [By.CLASS_NAME, 'Header_LogoScooter__3lsAR']
    redirect_yandex_ru = 'https://dzen.ru/?yredirect=true'
    dzen_content_div = [By.CLASS_NAME, 'content']
    order_text_pattern_1 = ('Заказ оформлен\n'
    'Номер заказа: .  Запишите его:\n'
    'пригодится, чтобы отслеживать статус')

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Принимаем куки')
    def accept_cookie(self):
        self.driver.find_element(*self.pop_up_agreement_cookies).click()

    @allure.step('Нажимаем кнопку "Заказать" в хедере ')
    def click_order_button_header(self):
        self.driver.find_element(*self.order_button_header).click()

    @allure.step('Нажимаем на поле ввода имени')
    def find_element_and_click_input_name(self):
        self.driver.find_element(*self.input_name).click()

    @allure.step('Вводим имя')
    def input_name_in(self):
        self.driver.find_element(*self.input_name).send_keys("Алина")

    @allure.step('Нажимаем на поле ввода фамилии')
    def find_element_and_click_input_surname(self):
        self.driver.find_element(*self.input_surname).click()

    @allure.step('Вводим фамилию')
    def input_surname_in(self):
        self.driver.find_element(*self.input_surname).send_keys("Татьянчикова")

    @allure.step('Нажимаем на поле ввода адреса')
    def find_element_and_click_input_address(self):
        self.driver.find_element(*self.input_address).click()

    @allure.step('Вводим адрес')
    def input_address_in(self):
        self.driver.find_element(*self.input_address).send_keys("Ломоносовский проспект 24")

    @allure.step('Нажимаем на выбор метро')
    def find_and_click_metro_station(self):
        self.driver.find_element(*self.choose_station_metro).click()

    @allure.step('Ждем отображение списка станций метро')
    def wait_before_choose_station(self):
        WebDriverWait(self.driver, 2).until(expected_conditions.visibility_of_element_located(self.station_metro))

    @allure.step('Выбираем станцию метро')
    def click_on_metro_station(self):
        self.driver.find_element(*self.station_metro).click()

    @allure.step('Нажимаем на поле ввода номера телефона')
    def find_and_click_phone_number(self):
        self.driver.find_element(*self.input_phone_number).click()

    @allure.step('Вводим номер телефона')
    def input_phone_number_in(self):
        self.driver.find_element(*self.input_phone_number).send_keys("79137284647")

    @allure.step('Нажимаем кнопку "Далее"')
    def click_next_button(self):
        self.driver.find_element(*self.next_button).click()

    @allure.step('Нажимаем на выбор даты доставки')
    def find_and_click_when_to_bring_scooter(self):
        self.driver.find_element(*self.when_to_bring_scooter).click()

    @allure.step('Выбираем дату доставки')
    def choose_when_to_bring_scooter(self):
        self.driver.find_element(*self.input_when_to_bring_scooter).click()

    @allure.step('Нажимаем на выбор периода аренды')
    def find_and_click_rental_period(self):
        self.driver.find_element(*self.rental_period).click()

    @allure.step('Выбираем период аренды')
    def choose_rental_period(self):
        self.driver.find_element(*self.input_rental_period).click()

    @allure.step('Выбираем цвет самоката')
    def choose_color_of_scooter(self):
        self.driver.find_element(*self.color_of_scooter).click()

    @allure.step('Нажимаем кнопку "Заказать"')
    def click_order_button(self):
        self.driver.find_element(*self.order_button).click()

    @allure.step('Подтверждаем заказ')
    def click_yes_button(self):
        self.driver.find_element(*self.yes_button).click()

    @allure.step('Ждем баннер с оповещением об успешном заказе')
    def wait_to_proceed_banner(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.order_processed))

    @allure.step('Нажимаем на логотип Яндекса')
    def click_on_yandex_logo(self):
        self.driver.find_element(*self.logo_yandex).click()

    @allure.step('Нажимаем на логотип Самоката')
    def click_on_logo_scooter(self):
        self.driver.find_element(*self.logo_scooter).click()

    @allure.step('Получаем текст заказа')
    def order_get_text(self):
        return self.driver.find_element(*self.order_processed_text).text

    @allure.step('Нажимаем на кнопку "Заказать" в теле сайта')
    def click_on_button_order(self):
        self.driver.find_element(*self.order_button_not_header).click()

    @allure.step('Ждем загрузку дзена')
    def wait_to_open_dzen_window(self):
        WebDriverWait(self.driver, 20).until(
            expected_conditions.visibility_of_element_located(self.dzen_content_div))

    @allure.step('Получаем текущую ссылку')
    def current_url(self):
        return self.driver.current_url


