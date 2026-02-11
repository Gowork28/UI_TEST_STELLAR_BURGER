import allure
import pytest

from Locators.main_page_locators import MainPageLocators
from Pages.main_page import MainPage


class TestIngredientCounter:

    @pytest.mark.parametrize("locator,counter, value", [
                             (MainPageLocators.BUN, MainPageLocators.BUN_COUNTER, '2'),
                             (MainPageLocators.SAUCE, MainPageLocators.SAUCE_COUNTER, '1'),
                             (MainPageLocators.FILLING, MainPageLocators.FILLING_COUNTER, '1')])
    @allure.title("При добавлении ингредиента в заказ его счётчик увеличивается")
    def test_ingredient_counter_increases(self, drivers, locator, counter, value):
        with allure.step("Проверяем начальное значение счетчика"):
            main_page = MainPage(drivers)
            main_page.wait_for_overlay_to_disappear_from_main_page()
            counter_value_before = main_page.get_counter_value(counter)
        with allure.step("Добавляем ингредиенты"):
            main_page.drag_and_drop_ingredient(locator)
        with allure.step("Проверяем, что значение счетчика изменилось"):
            counter_value_after = main_page.get_counter_value(counter)

            assert counter_value_before == '0' and counter_value_after == value