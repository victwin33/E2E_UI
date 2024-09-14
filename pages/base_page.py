import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains



class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Получить текущую ссылку')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Проверка отображения элемента на странице')
    def check_element(self, locator):
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Поиск элемента')
    def find_element(self, locator):
        return WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(locator))

    @allure.step('Клик по видимому элементу')
    def click_to_visible_element(self, locator):
        self.driver.find_element(*locator).click()

    @allure.step('Вставить текст {text}')
    def set_text_to_element(self, locator, text):
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(locator))
        self.driver.find_element(*locator).send_keys(text)

    @allure.step('Получение текста элемента')
    def get_text_of_element(self, locator):
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(locator))
        return self.driver.find_element(*locator).text


    @allure.step('Перемещение до элемента и клик по нему')
    def move_to_element_and_click(self, locator):
        element = self.driver.find_element(*locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click(element).perform()

