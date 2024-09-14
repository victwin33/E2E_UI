import allure

from locators.order_review_page_locators import OrderReviewPageLocators
from pages.base_page import BasePage


class OrderReviewPage(BasePage):
    @allure.step('Клик по кнопке "Финиш"')
    def click_too_finish_btn(self):
        self.move_to_element_and_click(OrderReviewPageLocators.FINISH_BTN)