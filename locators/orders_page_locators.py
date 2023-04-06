from selenium.webdriver.common.by import By


class OrdersPageLocators:
    # A class for order page locators. All order page locators should come here
    pop_up_agreement_cookies = [By.ID, 'rcc-confirm-button']
    order_button = [By.XPATH, "//div[contains(@class, 'Order_Buttons')]//button[contains(text(),'Заказать')]"]
    start_order_button = [By.XPATH, "//div[contains(@class, 'Home_FinishButton')]//button[contains(text(),'Заказать')]"]
    start_order_button_header = [By.XPATH, "//div[contains(@class, 'Header_Nav')]//button[contains(text(),'Заказать')]"]
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
    yes_button = [By.XPATH, "//div[contains(@class, 'Order_Buttons')]//button[contains(text(),'Да')]"]
    order_processed = [By.XPATH, "//div[contains(@class, 'Order_Modal')]"]
    status_view = [By.XPATH, "//div[contains(@class, 'Order_ModalHeader')]"]
    logo_yandex = [By.XPATH, "//a[contains(@class,'Header_LogoYandex')]"]
    logo_scooter = [By.XPATH, "//a[contains(@class,'Header_LogoScooter')]"]
    redirect_yandex_ru = 'https://dzen.ru/?yredirect=true'
    dzen_content_div = [By.CLASS_NAME, 'content']
