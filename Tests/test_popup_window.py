import allure
import pytest

from Pages.main_page import MainPage


class TestPopupWindow:

    @allure.title("По клику на игредиент появляется всплывающее окно с деталями")
    def test_click_ingredient_open_details_popup(self, drivers):
        with allure.step("Кликаем на ингредиент"):
            main_page = MainPage(drivers)
            main_page.wait_for_overlay_to_disappear_from_main_page()
            main_page.click_on_ingredient()

            assert "Детали ингредиента" in main_page.get_ingredient_popup_text()


    @allure.title("Всплывающее окно закрывается кликом по крестику")
    def test_close_popup_by_click(self, drivers):
        with allure.step("Кликаем на ингредиент"):
            main_page = MainPage(drivers)
            main_page.wait_for_overlay_to_disappear_from_main_page()
            main_page.click_on_ingredient()
        with allure.step("Закрываем всплывающее окно"):
            main_page.close_ingredient_popup_by_click()

            assert main_page.get_header_text() == 'Соберите бургер'