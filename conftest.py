import pytest
import random
from selenium import webdriver


@pytest.fixture(scope='session')
def random_email():
    return f'anna_shekshueva_11_{random.randint(10000, 99999)}@gmail.com'


@pytest.fixture(scope='session')
def random_password():
    return f'pass{random.randint(10000, 99999)}'


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
