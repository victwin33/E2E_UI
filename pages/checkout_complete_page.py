import allure
from pages.base_page import BasePage


class CheckoutCompletePage(BasePage):
    @allure.step('Получить текущую ссылку')
    def get_current_url(self):
        return self.driver.current_url
