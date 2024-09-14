from selenium.webdriver.common.by import By


class MainPageLocators:
    ADD_TO_CART_BTN = By.ID, "add-to-cart-sauce-labs-backpack"  # кнопка "Добавить в корзину"
    ADD_TO_CART_BTN_TITLE = By.ID, "remove-sauce-labs-backpack"  # надпись на  кнопке "Добавить в корзину товар",
    # в состоянии "Удалить"
    CART_LINK = By.CLASS_NAME, 'shopping_cart_link'  # кнопка/ссылка на корзину
