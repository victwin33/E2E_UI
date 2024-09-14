import allure
from conftest import driver, authorization_data, create_user_data
from data import Urls
from pages.authorization_page import AuthorizationPage
from pages.checkout_complete_page import CheckoutCompletePage
from pages.main_page import MainPage
from pages.order_page import OrderPage
from pages.order_review_page import OrderReviewPage
from pages.shopping_cart_page import ShoppingCartPage


class TestOrderProduct:
    @allure.step('Проверки сценария удачной покупки товара на сайте "')
    def test_successful_product_order(self, driver, authorization_data, create_user_data):
        authorization_page = AuthorizationPage(driver)
        authorization_page.login_user(authorization_data)
        main_page = MainPage(driver)
        main_page.click_add_too_cart_btn()
        main_page.click_cart_link()
        shopping_card_page = ShoppingCartPage(driver)
        shopping_card_page.check_cart_contents()
        shopping_card_page.click_checkout_btn()
        order_page = OrderPage(driver)
        order_page.making_an_order(create_user_data)
        order_review_page = OrderReviewPage(driver)
        order_review_page.click_too_finish_btn()
        checkout_complete_page = CheckoutCompletePage(driver)
        current_url = checkout_complete_page.get_current_url()
        assert current_url == Urls.CHECKOUT_COMPLETE_PAGE
