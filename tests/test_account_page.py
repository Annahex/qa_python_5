import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


BASE_URL = 'https://stellarburgers.nomoreparties.site/'
LOGIN_URL = f'{BASE_URL}login'
ACCOUNT_URL = f'{BASE_URL}account/profile'
EMAIL_LOCATOR = ".//input[@name='name']"
PASSWORD_LOCATOR = ".//input[@name='Пароль']"
LOGIN_BUTTON_LOCATOR = ".//button[text()='Войти']"
NAVBAR_LOGIN_BUTTON_LOCATOR = ".//p[text()='Личный Кабинет']/parent::a"
LOGOUT_BUTTON_LOCATOR = ".//button[text()='Выход']"


class TestAccountPage:

    def test_open_account_page_from_navbar(self, driver_registered, random_email, random_password):
        driver_registered.get(LOGIN_URL)
        WebDriverWait(driver_registered, 3).until(
            expected_conditions.url_to_be(LOGIN_URL))
        driver_registered.find_element(By.XPATH, EMAIL_LOCATOR).send_keys(random_email)
        driver_registered.find_element(By.XPATH, PASSWORD_LOCATOR).send_keys(random_password)
        driver_registered.find_element(By.XPATH, LOGIN_BUTTON_LOCATOR).click()
        WebDriverWait(driver_registered, 3).until(
            expected_conditions.url_to_be(BASE_URL))
        assert driver_registered.current_url == BASE_URL
        driver_registered.find_element(By.XPATH, NAVBAR_LOGIN_BUTTON_LOCATOR).click()
        WebDriverWait(driver_registered, 3).until(
            expected_conditions.url_to_be(ACCOUNT_URL))
        assert driver_registered.current_url == ACCOUNT_URL

    def test_logout_from_account_page(self, driver_registered, random_email, random_password):
        driver_registered.get(LOGIN_URL)
        WebDriverWait(driver_registered, 3).until(
            expected_conditions.url_to_be(LOGIN_URL))
        driver_registered.find_element(By.XPATH, EMAIL_LOCATOR).send_keys(random_email)
        driver_registered.find_element(By.XPATH, PASSWORD_LOCATOR).send_keys(random_password)
        driver_registered.find_element(By.XPATH, LOGIN_BUTTON_LOCATOR).click()
        WebDriverWait(driver_registered, 3).until(
            expected_conditions.url_to_be(BASE_URL))
        assert driver_registered.current_url == BASE_URL
        driver_registered.find_element(By.XPATH, NAVBAR_LOGIN_BUTTON_LOCATOR).click()
        WebDriverWait(driver_registered, 3).until(
            expected_conditions.url_to_be(ACCOUNT_URL))
        assert driver_registered.current_url == ACCOUNT_URL
        driver_registered.find_element(By.XPATH, LOGOUT_BUTTON_LOCATOR).click()
        WebDriverWait(driver_registered, 3).until(
            expected_conditions.url_to_be(LOGIN_URL))
        assert driver_registered.current_url == LOGIN_URL
