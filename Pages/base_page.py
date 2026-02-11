import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from seletools.actions import drag_and_drop


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)

    @allure.step('Находим нужный элемент')
    def find_element(self, locator):
        return WebDriverWait(self.driver, 15).until(EC.presence_of_element_located(locator),
                                                    message=f'Не найден элемент {locator} ')

    @allure.step("Ждём, пока элемент станет невидимым")
    def wait_for_element_hide(self, locator, timeout=20):
        WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    @allure.step("Ждём, пока элемент станет видимым")
    def wait_for_element_visible(self, locator, timeout=20):
        WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    @allure.step('Получаем видимость элемента')
    def check_displayed_element(self, locator):
        return self.driver.find_element(*locator).is_displayed()

    @allure.step('Получаем текущий URL')
    def get_url(self):
        return self.driver.current_url

    @allure.step('Кликаем на элемент')
    def click_on_the_element(self, locator):
        element = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(locator))
        element.click()
        return element

    @allure.step('Вводим текст')
    def type_text(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
        return element

    @allure.step('Получаем текст элемента')
    def get_text(self, locator, timeout=20):
        element = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        return element.text

    @allure.step('Кликаем по элементу через JS скрипт')
    def click_on_the_element_by_js_script(self, locator, timeout=15):
        element = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].click();", element)
        return element

    @allure.step('Перетаскиваем элемент')
    def drag_and_drop(self, source_locator, target_locator):
        drag_and_drop(self.driver, source_locator, target_locator)




