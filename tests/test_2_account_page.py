from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


BASE_URL = 'https://stellarburgers.nomoreparties.site/'
LOGIN_URL = f'{BASE_URL}login'
ACCOUNT_URL = f'{BASE_URL}account/profile'
ANY_INPUT_LOCATOR = ".//main//form//input"
EMAIL_LOCATOR = ".//main//form//input[@name='name']"
PASSWORD_LOCATOR = ".//main//form//input[@name='Пароль']"
LOGIN_BUTTON_LOCATOR = ".//main//form/button"
NAVBAR_LOGIN_BUTTON_LOCATOR = ".//nav//p[text()='Личный Кабинет']/parent::a"
LOGOUT_BUTTON_LOCATOR = ".//main/div/nav/ul/li/button[text()='Выход']"


class TestAccountPage:

    def test_open_account_page_from_navbar(self, driver, random_email, random_password):
        driver.get(LOGIN_URL)
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ANY_INPUT_LOCATOR)))
        driver.find_element(By.XPATH, EMAIL_LOCATOR).send_keys(random_email)
        driver.find_element(By.XPATH, PASSWORD_LOCATOR).send_keys(random_password)
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ANY_INPUT_LOCATOR)))
        driver.find_element(By.XPATH, LOGIN_BUTTON_LOCATOR).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.url_to_be(BASE_URL))
        assert driver.current_url == BASE_URL
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, NAVBAR_LOGIN_BUTTON_LOCATOR)))
        driver.find_element(By.XPATH, NAVBAR_LOGIN_BUTTON_LOCATOR).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.url_to_be(ACCOUNT_URL))
        assert driver.current_url == ACCOUNT_URL

    def test_logout_from_account_page(self, driver, random_email, random_password):
        driver.get(LOGIN_URL)
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ANY_INPUT_LOCATOR)))
        driver.find_element(By.XPATH, EMAIL_LOCATOR).send_keys(random_email)
        driver.find_element(By.XPATH, PASSWORD_LOCATOR).send_keys(random_password)
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ANY_INPUT_LOCATOR)))
        driver.find_element(By.XPATH, LOGIN_BUTTON_LOCATOR).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.url_to_be(BASE_URL))
        assert driver.current_url == BASE_URL
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, NAVBAR_LOGIN_BUTTON_LOCATOR)))
        driver.find_element(By.XPATH, NAVBAR_LOGIN_BUTTON_LOCATOR).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.url_to_be(ACCOUNT_URL))
        assert driver.current_url == ACCOUNT_URL
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, LOGOUT_BUTTON_LOCATOR)))
        driver.find_element(By.XPATH, LOGOUT_BUTTON_LOCATOR).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.url_to_be(LOGIN_URL))
        assert driver.current_url == LOGIN_URL
