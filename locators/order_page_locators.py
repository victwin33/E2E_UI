from selenium.webdriver.common.by import By


class OrderPageLocators:
    INPUT_FIRST_NAME = By.ID, "first-name"  # поле для ввода имени
    INPUT_LAST_NAME = By.ID, "last-name"  # поле для ввода фамилии
    INPUT_POSTCODE = By.ID, "postal-code"  # поле для ввода почтового индекса
    BUTTON_CONTINUE = By.ID, "continue"  # кнопка "Продолжить"
