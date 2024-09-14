from selenium.webdriver.common.by import By


class ShoppingCartPageLocators:
    ADD_TO_CART_BTN = By.ID, "add-to-cart-sauce-labs-backpack"  # кнопка "Добавить в корзину"
    CART_CONTENTS = By.ID, "cart_contents_container"  # контейнер с информацией о заказе
    CHECKOUT_BTN = By.ID, "checkout"  # кнопка "Оформить"
