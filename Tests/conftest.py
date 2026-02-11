import pytest
import allure

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Locators.main_page_locators import MainPageLocators
from Pages.main_page import MainPage
from Pages.login_page import LoginPage
from Pages.feed_of_orders import FeedOfOrdersPage

from data import MyTestData
from urls import UrlsForTest


#  фикстура инициализации драйверов
@pytest.fixture(params=["firefox", "chrome",])
def drivers(request):
    with allure.step(f"Инициализация драйвера: {request.param}"):
        if request.param == "firefox":
            web_driver = webdriver.Firefox()
        elif request.param == "chrome":
            web_driver = webdriver.Chrome()
        request.cls.driver = web_driver
        web_driver.maximize_window()
        web_driver.get(UrlsForTest.BASE_URL)
        yield web_driver
        web_driver.quit()


#  фикстура получения значения счетчика Выполнено за все время
@pytest.fixture
def all_time_number(drivers):
    drivers.get(UrlsForTest.FEED_ORDERS_URL)
    feed_order = FeedOfOrdersPage(drivers)
    all_time_number = feed_order.find_order_number_all_the_time()

    return all_time_number


#  фикстура получения значения счетчика Выполнено за сегодня
@pytest.fixture
def today_order_number(drivers):
    drivers.get(UrlsForTest.FEED_ORDERS_URL)
    feed_order = FeedOfOrdersPage(drivers)
    today_order_number = feed_order.find_order_number_today()

    return today_order_number


#  фикстура авторизации пользователя и создания заказа
@pytest.fixture
def auth_user_with_order(drivers):
    #  авторизация
    drivers.get(UrlsForTest.LOGIN_URL)
    login = LoginPage(drivers)
    login.wait_for_overlay_to_disappear_from_login_page()
    login.input_email(MyTestData.data['email'])
    login.input_password(MyTestData.data['password'])
    login.click_login_button()

    #  создание заказа
    order = MainPage(drivers)
    order.wait_for_overlay_to_disappear_from_main_page()
    order.drag_and_drop_ingredient(MainPageLocators.BUN)
    order.drag_and_drop_ingredient(MainPageLocators.SAUCE)
    order.drag_and_drop_ingredient(MainPageLocators.FILLING)
    order.click_on_order_button()
    order.wait_for_overlay()   #  дождаться появление оверлэя
    order.wait_for_overlay_to_disappear_from_main_page()  #  дождаться исчезновения оверлэя
    order_number = order.get_order_number()  #  получение номера заказа
    order.close_order_popup_by_click()  #  закрытие попапа с номером заказа

    drivers.get(UrlsForTest.FEED_ORDERS_URL)
    return order_number
