from selenium.webdriver.common.by import By

class MainPageLocators:

    #  заголовок страницы
    HEADER_TEXT = (By.XPATH, ".//h1[text()='Соберите бургер']")

    #  разделы
    FEED_SECTION = (By.XPATH, ".//p[text()='Лента Заказов']")
    CONSTRUCTOR_SECTION = (By.XPATH, ".//p[text()='Конструктор']")

    #  ингредиенты
    BUN = (By.CSS_SELECTOR, "a[href='/ingredient/61c0c5a71d1f82001bdaaa6c']")
    SAUCE = (By.CSS_SELECTOR, "a[href='/ingredient/61c0c5a71d1f82001bdaaa72']")
    FILLING = (By.CSS_SELECTOR, "a[href='/ingredient/61c0c5a71d1f82001bdaaa6f']")

    #  счетчики ингредиентов
    BUN_COUNTER = (By.XPATH, "//a[@href='/ingredient/61c0c5a71d1f82001bdaaa6c']//p[@class='counter_counter__num__3nue1']")
    SAUCE_COUNTER = (By.XPATH, "//a[@href='/ingredient/61c0c5a71d1f82001bdaaa72']//p[@class='counter_counter__num__3nue1']")
    FILLING_COUNTER = (By.XPATH, "//a[@href='/ingredient/61c0c5a71d1f82001bdaaa6f']//p[@class='counter_counter__num__3nue1']")

    #  корзина
    CONSTRUCTOR_BASKET = (By.CSS_SELECTOR, "ul.BurgerConstructor_basket__list__l9dp_")

    #  кнопки страницы
    LOGIN_BUTTON = (By.XPATH, ".//button[text()='Войти в аккаунт']")
    ORDER_BUTTON = (By.XPATH, ".//button[text()='Оформить заказ']")

    #  попап ингредиента
    POPUP_INGREDIENT = (By.XPATH,
                        "//h2[text()='Детали ингредиента']/ancestor::div[contains(@class,'Modal_modal__container')]")
    INGREDIENT_POPUP_CLOSE_BUTTON = (By.CSS_SELECTOR, "button.Modal_modal__close_modified__3V5XS.Modal_modal__close__TnseK")

    #  попап с номером заказа
    SUCCESSFUL_ORDER_POPUP = (By.XPATH,
                        "//div[contains(@class,'Modal_modal__container') and .//p[contains(text(),'заказ')]]")
    ORDER_NUMBER = (By.XPATH,
                    "//h2[contains(@class,'Modal_modal__title__') and contains(@class,'text_type_digits-large')]")
    ORDER_NUMBER_POPUP_CLOSE_BUTTON = (By.CSS_SELECTOR, "button.Modal_modal__close__TnseK.Modal_modal__close_modified__3V5XS")

    #  оверлэй
    OVERLAY = (By.XPATH, '//img[contains(@class, "loading")]/parent::div')
