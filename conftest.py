import pytest
import random

BASE_URL = 'https://stellarburgers.nomoreparties.site/'

__last_generated_email = None
__last_generated_password = None


@pytest.fixture()
def register_url():
    return f'{BASE_URL}register'


@pytest.fixture()
def login_url():
    return f'{BASE_URL}login'


@pytest.fixture()
def forgot_password_url():
    return f'{BASE_URL}forgot-password'


@pytest.fixture()
def account_url():
    return f'{BASE_URL}account/profile'


@pytest.fixture()
def base_url():
    return BASE_URL


@pytest.fixture()
def random_email():
    global __last_generated_email
    __last_generated_email = f'anna_shekshueva_11_{random.randint(10000, 99999)}@gmail.com'
    return __last_generated_email


@pytest.fixture()
def random_password():
    global __last_generated_password
    __last_generated_password = f'pass{random.randint(10000, 99999)}'
    return __last_generated_password


@pytest.fixture()
def last_generated_email():
    global __last_generated_email
    return __last_generated_email


@pytest.fixture()
def last_generated_password():
    global __last_generated_password
    return __last_generated_password
