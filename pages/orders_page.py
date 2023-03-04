import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

order_button_header = [By.CLASS_NAME, 'Button_Button__ra12g']
order_button_not_header = [By.XPATH,
                           "//div[contains(@class, 'Home_FinishButton')]//button[contains(text(),'Заказать')]"]


class OrdersPage:
    driver = None

    pop_up_agreement_cookies = [By.ID, 'rcc-confirm-button']
    order_button_header = [By.CLASS_NAME, 'Button_Button__ra12g']
    input_name = [By.XPATH, "//input[@placeholder='* Имя']"]
    input_surname = [By.XPATH, "//input[@placeholder='* Фамилия']"]
    input_address = [By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']"]
    choose_station_metro = [By.XPATH, "//input[@placeholder='* Станция метро']"]
    station_metro = [By.CLASS_NAME, "select-search__option"]
    input_phone_number = [By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']"]
    next_button = [By.XPATH, "//button[contains(text(),'Далее')]"]
    when_to_bring_scooter = [By.XPATH, "//input[@placeholder='* Когда привезти самокат']"]
    input_when_to_bring_scooter = [By.CLASS_NAME, 'react-datepicker__day--008']
    rental_period = [By.CLASS_NAME, 'Dropdown-control']
    input_rental_period = [By.CLASS_NAME, 'Dropdown-option']
    color_of_scooter = [By.XPATH, '//*[@id="black"]']
    order_button = [By.XPATH, "//div[contains(@class, 'Order_Buttons')]//button[contains(text(),'Заказать')]"]
    yes_button = [By.XPATH, "//div[contains(@class, 'Order_Buttons')]//button[contains(text(),'Да')]"]
    order_processed = [By.XPATH, "//div[contains(@class, 'Order_Modal')]"]
    order_processed_text = [By.XPATH, '/html/body/div/div/div[2]/div[5]/div[1]']
    logo_yandex = [By.CLASS_NAME, 'Header_LogoYandex__3TSOI']
    logo_scooter = [By.CLASS_NAME, 'Header_LogoScooter__3lsAR']
    redirect_yandex_ru = 'https://dzen.ru/?yredirect=true'
    dzen_content_div = [By.CLASS_NAME, 'content']
    order_text_pattern = 'Заказ оформлен\nНомер заказа: .  Запишите его:\nпригодится, чтобы отслеживать статус'

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Принимаем куки')
    def accept_cookie(self):
        self.driver.find_element(*self.pop_up_agreement_cookies).click()

    @allure.step('Нажимаем на логотип Яндекса')
    def click_on_yandex_logo(self):
        self.driver.find_element(*self.logo_yandex).click()

    @allure.step('Нажимаем на логотип Самоката')
    def click_on_logo_scooter(self):
        self.driver.find_element(*self.logo_scooter).click()

    @allure.step('Получаем текст заказа')
    def order_get_text(self):
        return self.driver.find_element(*self.order_processed_text).text

    @allure.step('Ждем загрузку дзена')
    def wait_to_open_dzen_window(self):
        WebDriverWait(self.driver, 20).until(
            expected_conditions.visibility_of_element_located(self.dzen_content_div))

    @allure.step('Получаем текущую ссылку')
    def current_url(self):
        return self.driver.current_url

    @allure.step('Выбираем кнопку для офррмления заказа')
    def open(self, button):
        self.driver.find_element(*button).click()

    @allure.step('Оформление заказа')
    def checkout_process(self, button):
        self.driver.find_element(*button).click()
        self.driver.find_element(*self.input_name).click()
        self.driver.find_element(*self.input_name).send_keys('Алина')
        self.driver.find_element(*self.input_surname).click()
        self.driver.find_element(*self.input_surname).send_keys('Татьянчикова')
        self.driver.find_element(*self.input_address).click()
        self.driver.find_element(*self.input_address).send_keys('Ломоносовский проспект 33')
        self.driver.find_element(*self.choose_station_metro).click()
        WebDriverWait(self.driver, 2).until(expected_conditions.visibility_of_element_located(self.station_metro))
        self.driver.find_element(*self.station_metro).click()
        self.driver.find_element(*self.input_phone_number).click()
        self.driver.find_element(*self.input_phone_number).send_keys('79137284647')
        self.driver.find_element(*self.next_button).click()
        self.driver.find_element(*self.when_to_bring_scooter).click()
        self.driver.find_element(*self.input_when_to_bring_scooter).click()
        self.driver.find_element(*self.rental_period).click()
        self.driver.find_element(*self.input_rental_period).click()
        self.driver.find_element(*self.color_of_scooter).click()
        self.driver.find_element(*self.order_button).click()
        self.driver.find_element(*self.yes_button).click()
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.order_processed))
