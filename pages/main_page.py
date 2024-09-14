import allure
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step('Найти кнопку "Добавить в корзину"')
    def find_ingredient_bun(self):
        return self.find_element(MainPageLocators.ADD_TO_CART_BTN)

    @allure.step('Клик по кнопке "Добавить в корзину"')
    def click_add_too_cart_btn(self):
        self.move_to_element_and_click(MainPageLocators.ADD_TO_CART_BTN)

    @allure.step('Клик по кнопке/ссылка на корзину для покупок"')
    def click_cart_link(self):
        self.move_to_element_and_click(MainPageLocators.CART_LINK)