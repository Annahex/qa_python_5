import pytest
import random

BASE_URL = 'https://stellarburgers.nomoreparties.site/'


@pytest.fixture()
def register_url():
    return f'{BASE_URL}register'


@pytest.fixture()
def login_url():
    return f'{BASE_URL}login'


@pytest.fixture()
def base_url():
    return BASE_URL


@pytest.fixture()
def random_email():
    return f'anna_shekshueva_11_{random.randint(10000, 99999)}@gmail.com'


@pytest.fixture()
def random_password():
    return f'pass{random.randint(10000, 99999)}'
