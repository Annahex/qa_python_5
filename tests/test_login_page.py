from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

BASE_URL = 'https://stellarburgers.nomoreparties.site/'
REGISTER_URL = f'{BASE_URL}register'
LOGIN_URL = f'{BASE_URL}login'
FORGOT_PASSWORD_URL = f'{BASE_URL}forgot-password'
MAIN_PAGE_LOGIN_BUTTON_LOCATOR = ".//button[text()='Войти в аккаунт']"
NAVBAR_LOGIN_BUTTON_LOCATOR = ".//p[text()='Личный Кабинет']/parent::a"
REGISTER_PAGE_LOGIN_BUTTON_LOCATOR = ".//a[@href='/login']"
FORGOT_PASSWORD_LOGIN_BUTTON_LOCATOR = ".//a[@href='/login']"


class TestLoginPage:

    def test_open_login_page_from_main_page(self, driver):
        driver.get(BASE_URL)
        WebDriverWait(driver, 3).until(
            expected_conditions.url_to_be(BASE_URL))
        driver.find_element(By.XPATH, MAIN_PAGE_LOGIN_BUTTON_LOCATOR).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.url_to_be(LOGIN_URL))
        assert driver.current_url == LOGIN_URL

    def test_open_login_page_from_navbar(self, driver):
        driver.get(BASE_URL)
        WebDriverWait(driver, 3).until(
            expected_conditions.url_to_be(BASE_URL))
        driver.find_element(By.XPATH, NAVBAR_LOGIN_BUTTON_LOCATOR).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.url_to_be(LOGIN_URL))
        assert driver.current_url == LOGIN_URL

    def test_open_login_page_from_register_page(self, driver):
        driver.get(REGISTER_URL)
        WebDriverWait(driver, 3).until(
            expected_conditions.url_to_be(REGISTER_URL))
        driver.find_element(By.XPATH, REGISTER_PAGE_LOGIN_BUTTON_LOCATOR).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.url_to_be(LOGIN_URL))
        assert driver.current_url == LOGIN_URL

    def test_open_login_page_from_forgot_password_page(self, driver):
        driver.get(FORGOT_PASSWORD_URL)
        WebDriverWait(driver, 3).until(
            expected_conditions.url_to_be(FORGOT_PASSWORD_URL))
        driver.find_element(By.XPATH, FORGOT_PASSWORD_LOGIN_BUTTON_LOCATOR).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.url_to_be(LOGIN_URL))
        assert driver.current_url == LOGIN_URL
