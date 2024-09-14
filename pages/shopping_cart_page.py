import allure
from locators.shopping_cart_page_locators import ShoppingCartPageLocators
from pages.base_page import BasePage



class ShoppingCartPage(BasePage):
    @allure.step('Получение информации о товаре в корзине')
    def check_cart_contents(self):
        return self.check_element(ShoppingCartPageLocators.CART_CONTENTS)

    @allure.step('Клик по кнопке "Добавить в корзину"')
    def click_checkout_btn(self):
        self.move_to_element_and_click(ShoppingCartPageLocators.CHECKOUT_BTN)

