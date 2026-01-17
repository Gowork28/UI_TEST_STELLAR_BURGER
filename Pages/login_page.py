import allure

from Locators.login_page_locators import LoginPageLocators
from Pages.base_page import BasePage


class LoginPage(BasePage):

    @allure.step("Вводим данные в поле ввода Email")
    def input_email(self, email):
        self.type_text(LoginPageLocators.EMAIL_FIELD, email)

    @allure.step("Вводим данные в поле ввода Пароль")
    def input_password(self, password):
        self.type_text(LoginPageLocators.PASSWORD_FIELD, password)

    @allure.step("Кликаем по кнопке Войти")
    def click_login_button(self):
        self.click_on_the_element_by_js_script(LoginPageLocators.LOGIN_BUTTON)

    @allure.step("Ждем исчезновения overlay")
    def wait_for_overlay_to_disappear_from_login_page(self):
        self.wait_for_element_hide(LoginPageLocators.OVERLAY)
