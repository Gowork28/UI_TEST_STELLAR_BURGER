import allure

from Locators.feed_of_orders_locators import FeedOrdersLocators
from Locators.main_page_locators import MainPageLocators
from Pages.base_page import BasePage


class FeedOfOrdersPage(BasePage):

    @allure.step("Получаем номер заказа счетчика Выполнено за все время")
    def find_order_number_all_the_time(self):
        return self.get_text(FeedOrdersLocators.ALL_THE_TIME_COUNTER_NUMBERS)

    @allure.step("Получаем номер заказа счетчика Выполнено за сегодня")
    def find_order_number_today(self):
        return self.get_text(FeedOrdersLocators.DAY_COUNTER_NUMBERS)

    @allure.step("Получаем номер заказа в разделе В работе")
    def find_order_number_in_work(self, order_number):
        self.find_element(FeedOrdersLocators.in_work_numbers(order_number))
        return self.check_displayed_element(FeedOrdersLocators.in_work_numbers(order_number))