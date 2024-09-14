import pytest
from faker import Faker
from selenium import webdriver
from data import Urls


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.set_window_size(1920, 1080)
    driver.get(Urls.AUTHORIZATION_PAGE)
    yield driver
    driver.quit()


@pytest.fixture()
def authorization_data():
    payload = {
        "login": 'standard_user',
        "password": 'secret_sauce'
    }
    return payload


@pytest.fixture()
def create_user_data():
    fake = Faker("ru_RU")
    user_data = {
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "postcode": fake.postcode()
    }
    return user_data
