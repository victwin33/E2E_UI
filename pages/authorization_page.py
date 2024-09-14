import allure
from locators.autorization_page_locators import AuthorizationPageLocators
from pages.base_page import BasePage
from conftest import authorization_data


class AuthorizationPage(BasePage):

    @allure.step('Авторизация')
    def login_user(self, authorization_data):
        self.set_text_to_element(AuthorizationPageLocators.INPUT_LOGIN, authorization_data['login'])
        self.set_text_to_element(AuthorizationPageLocators.INPUT_PASSWORD, authorization_data['password'])
        self.click_to_visible_element(AuthorizationPageLocators.LOGIN_BTN)
