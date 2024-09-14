import allure
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):

    @allure.step('Оформление заказа')
    def making_an_order(self, user_data):
        self.set_text_to_element(OrderPageLocators.INPUT_FIRST_NAME, user_data['first_name'])
        self.set_text_to_element(OrderPageLocators.INPUT_LAST_NAME, user_data['last_name'])
        self.set_text_to_element(OrderPageLocators.INPUT_POSTCODE, user_data['postcode'])
        self.click_to_visible_element(OrderPageLocators.BUTTON_CONTINUE)