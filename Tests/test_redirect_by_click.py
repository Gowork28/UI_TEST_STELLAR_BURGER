import allure
import pytest

from Pages.main_page import MainPage
from urls import UrlsForTest


class TestRedirectByClick:

    @allure.title("Переход по клику на Конструктор")
    def test_click_constructor_open_constructor(self, drivers):
        with allure.step("Кликаем по кнопке авторизации"):
            main_page = MainPage(drivers)
            main_page.click_on_login_button()
        with allure.step("Кликаем по разделу Конструктор"):
            main_page.click_on_constructor_section()

            assert drivers.current_url == UrlsForTest.CONSTRUCTOR_URL


    @allure.title("Переход по клику на Лента Заказов")
    def test_click_feed_orders_open_feed_orders(self, drivers):
        with allure.step("Кликаем по разделу Лента Заказов"):
            main_page = MainPage(drivers)
            main_page.click_on_feed_orders_section()

            assert drivers.current_url == UrlsForTest.FEED_ORDERS_URL
