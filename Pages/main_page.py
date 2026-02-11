import allure

from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Locators.main_page_locators import MainPageLocators
from Pages.base_page import BasePage
from urls import UrlsForTest


class MainPage(BasePage):

    @allure.step("Получаем тект заголовка страницы")
    def get_header_text(self):
        return self.get_text(MainPageLocators.HEADER_TEXT)

    @allure.step('Кликаем на раздел "Конструктор"')
    def click_on_constructor_section(self):
        self.click_on_the_element(MainPageLocators.CONSTRUCTOR_SECTION)
        return self.get_url()

    @allure.step('Кликаем на раздел "Лента заказов"')
    def click_on_feed_orders_section(self):
        self.click_on_the_element(MainPageLocators.FEED_SECTION)
        return self.get_url()

    @allure.step('Кликаем на ингредиент')
    def click_on_ingredient(self):
        self.click_on_the_element(MainPageLocators.BUN)

    @allure.step('Получаем текст карточки ингредиента')
    def get_ingredient_popup_text(self):
        return self.get_text(MainPageLocators.POPUP_INGREDIENT)

    @allure.step('Кликаем по крестику карточки ингредиента')
    def close_ingredient_popup_by_click(self):
        self.click_on_the_element(MainPageLocators.INGREDIENT_POPUP_CLOSE_BUTTON)

    @allure.step('Кликаем по крестику попапа с номером заказа')
    def close_order_popup_by_click(self):
        self.find_element(MainPageLocators.ORDER_NUMBER)
        self.click_on_the_element_by_js_script(MainPageLocators.ORDER_NUMBER_POPUP_CLOSE_BUTTON)
        self.wait_for_element_hide(MainPageLocators.OVERLAY)

    @allure.step('Получаем значение счетчика ингредиента')
    def get_counter_value(self, counter_locator):
        return self.get_text(counter_locator)

    @allure.step('Перетаскиваем ингредиент в корзину')
    def drag_and_drop_ingredient(self, ingredient_locator):
        ingredient = self.find_element(ingredient_locator)
        basket = self.find_element(MainPageLocators.CONSTRUCTOR_BASKET)
        self.drag_and_drop(ingredient, basket)

    @allure.step('Кликаем по кнопке Оформить заказ')
    def click_on_order_button(self):
        self.wait_for_element_hide(MainPageLocators.OVERLAY)
        self.click_on_the_element(MainPageLocators.ORDER_BUTTON)

    @allure.step('Кликаем по кнопке Войти в аккаунт')
    def click_on_login_button(self):
        self.click_on_the_element(MainPageLocators.LOGIN_BUTTON)

    @allure.step('Получаем номер заказа')
    def get_order_number(self):
        self.check_displayed_element(MainPageLocators.SUCCESSFUL_ORDER_POPUP)
        self.wait_for_element_hide(MainPageLocators.OVERLAY)
        return self.get_text(MainPageLocators.ORDER_NUMBER)

    @allure.step("Ждем появления overlay")
    def wait_for_overlay(self):
        self.wait_for_element_visible(MainPageLocators.OVERLAY)

    @allure.step("Ждем исчезновения overlay")
    def wait_for_overlay_to_disappear_from_main_page(self):
        self.wait_for_element_hide(MainPageLocators.OVERLAY)
