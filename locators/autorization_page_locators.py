from selenium.webdriver.common.by import By


class AuthorizationPageLocators:
    INPUT_LOGIN = By.ID, "user-name"  # поле ввода логина
    INPUT_PASSWORD = By.ID, "password"  # поле ввода пароля
    LOGIN_BTN = By.ID, "login-button"  # кнопка "Авторизоваться"
