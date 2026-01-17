from selenium.webdriver.common.by import By

class LoginPageLocators:

    #  поля ввода
    EMAIL_FIELD = (By.XPATH, ".//label[text()='Email']//parent::*/input[@type='text' and @name='name']")
    PASSWORD_FIELD = (By.XPATH, ".//input[@type='password' and @name='Пароль']")

    #  кнопка Войти
    LOGIN_BUTTON = (By.XPATH, ".//button[text()='Войти']")

    #  оверлэй
    OVERLAY = (By.CSS_SELECTOR, ".Modal_modal_overlay__x2ZCr")