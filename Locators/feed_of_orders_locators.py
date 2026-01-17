from selenium.webdriver.common.by import By

class FeedOrdersLocators:

    #  счетчик Выполнено за всё время
    ALL_THE_TIME_COUNTER_NUMBERS = (By.XPATH,
                    "//p[contains(@class,'OrderFeed_number__2MbrQ') and contains(@class,'text_type_digits-large')]")

    #  счетчик Выполнено за сегодня
    DAY_COUNTER_NUMBERS = (By.XPATH,
                    "//p[text()='Выполнено за сегодня:']/following-sibling::p[contains(@class,'OrderFeed_number__')]")

    #  раздел В работе
    IN_WORK_NUMBERS = (By.CSS_SELECTOR, "ul.OrderFeed_orderListReady__1YFem.OrderFeed_orderList__cBvyi")

    #  оверлэй
    OVERLAY = (By.XPATH, '//img[contains(@class, "loading")]/parent::div/div[contains(@class, "overlay")]')

    #  метод поиска локатора номера заказа
    @staticmethod
    def in_work_numbers(order_number):
        list_of_orders = f'//ul[contains(@class,"orderListReady")]/li[contains(., "{order_number}")]'
        locator = (By.XPATH, list_of_orders)
        return locator