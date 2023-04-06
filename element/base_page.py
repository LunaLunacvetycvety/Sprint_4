from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    # для поиска элемента
    def find_element(self, locator, time=20):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator))

    # для перехода на главную
    def go_to_site(self, url):
        self.driver.get(url)

    # ждем видимость элемента
    def wait_to_open(self, locator, time=20):
        WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator))

    # получаем текст
    def get_text(self, locator):
        return self.driver.find_element(*locator).text

    # кликаем по элементу
    def click_on_element(self, locator):
        self.driver.find_element(*locator).click()

    # получаем текущую ссылку
    def get_current_url(self):
        return self.driver.current_url

    # вводим в поле данные
    def input_value(self, locator, text):
        self.driver.find_element(*locator).send_keys(text)
