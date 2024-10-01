from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

BASE_URL = 'https://stellarburgers.nomoreparties.site/'
REGISTER_URL = f'{BASE_URL}register'
LOGIN_URL = f'{BASE_URL}login'
ANY_INPUT_LOCATOR = ".//main//form//input"
EMAIL_OR_NAME_LOCATOR = ".//main//form//input[@name='name']"
PASSWORD_LOCATOR = ".//main//form//input[@name='Пароль']"
REGISTER_BUTTON_LOCATOR = ".//main//form/button"
ERROR_MESSAGE_LOCATOR = ".//fieldset//p[text()='Некорректный пароль']"


class TestRegisterPage:

    def test_success_registration(self, driver, random_email, random_password):
        driver.get(REGISTER_URL)
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ANY_INPUT_LOCATOR)))
        for input_element in driver.find_elements(By.XPATH, EMAIL_OR_NAME_LOCATOR):
            input_element.send_keys(random_email)
        driver.find_element(By.XPATH, PASSWORD_LOCATOR).send_keys(random_password)
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ANY_INPUT_LOCATOR)))
        driver.find_element(By.XPATH, REGISTER_BUTTON_LOCATOR).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.url_to_be(LOGIN_URL))
        assert driver.current_url == LOGIN_URL
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ANY_INPUT_LOCATOR)))
        driver.find_element(By.XPATH, EMAIL_OR_NAME_LOCATOR).send_keys(random_email)
        driver.find_element(By.XPATH, PASSWORD_LOCATOR).send_keys(random_password)
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ANY_INPUT_LOCATOR)))
        driver.find_element(By.XPATH, REGISTER_BUTTON_LOCATOR).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.url_to_be(BASE_URL))
        assert driver.current_url == BASE_URL

    def test_wrong_password(self, driver, random_email):
        wrong_password = "1"
        driver.get(REGISTER_URL)
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ANY_INPUT_LOCATOR)))
        for input_element in driver.find_elements(By.XPATH, EMAIL_OR_NAME_LOCATOR):
            input_element.send_keys(random_email)
        driver.find_element(By.XPATH, PASSWORD_LOCATOR).send_keys(wrong_password)
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ANY_INPUT_LOCATOR)))
        driver.find_element(By.XPATH, REGISTER_BUTTON_LOCATOR).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, ERROR_MESSAGE_LOCATOR)))
        assert driver.current_url == REGISTER_URL
