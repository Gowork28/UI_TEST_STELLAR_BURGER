import allure
import pytest
from Locators.main_page_locators import MainPageLocators
from Pages.feed_of_orders import FeedOfOrdersPage
from Pages.main_page import MainPage
from urls import UrlsForTest


class TestFeedOfOrders:

    @allure.title("При создании нового заказа счетчик Выполнено за все время увеличивается")
    def test_new_order_counter_all_the_time_increases(self, drivers, all_time_number, auth_user_with_order):
        with allure.step("Получаем начальное значение счетчика Выполнено за все время"):
            all_time_number_before = all_time_number
        with allure.step("Создаем заказ"):
            order_number = auth_user_with_order
        with allure.step("Получаем итоговое значение счетчика Выполнено за все время"):
            feed_order = FeedOfOrdersPage(drivers)
            all_time_number_after = feed_order.find_order_number_all_the_time()

            assert all_time_number_before < all_time_number_after


    @allure.title("При создании нового заказа счетчик Выполнено за сегодня увеличивается")
    def test_new_order_counter_today_counter_increases(self, drivers, today_order_number, auth_user_with_order):
        with allure.step("Получаем начальное значение счетчика Выполнено за сегодня"):
            today_number_before = today_order_number
        with allure.step("Создаем заказ"):
            order = auth_user_with_order
        with allure.step("Получаем итоговое значение счетчика Выполнено за сегодня"):
            feed_order = FeedOfOrdersPage(drivers)
            today_number_after = feed_order.find_order_number_today()

        assert today_number_before < today_number_after


    @allure.title("После оформления заказа его номер появляется в разделе В работе")
    def test_new_order_shows_in_work_section(self, drivers, auth_user_with_order):
        order_number = auth_user_with_order
        feed_order = FeedOfOrdersPage(drivers)

        assert feed_order.find_order_number_in_work(order_number)
