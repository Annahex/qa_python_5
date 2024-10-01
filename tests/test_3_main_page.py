from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import time


BASE_URL = 'https://stellarburgers.nomoreparties.site/'
LOGIN_URL = f'{BASE_URL}login'
ACCOUNT_URL = f'{BASE_URL}account/profile'
ANY_INPUT_LOCATOR = ".//main//form//input"
EMAIL_LOCATOR = ".//main//form//input[@name='name']"
PASSWORD_LOCATOR = ".//main//form//input[@name='Пароль']"
LOGIN_BUTTON_LOCATOR = ".//main//form/button"
NAVBAR_LOGIN_BUTTON_LOCATOR = ".//nav//p[text()='Личный Кабинет']/parent::a"
NAVBAR_CONSTRUCTOR_BUTTON_LOCATOR = ".//nav//p[text()='Конструктор']/parent::a"
NAVBAR_LOGO_BUTTON_LOCATOR = ".//nav//div/a[@href='/']"
TOPPING_LOCATOR = ".//main/section/div/div/span[text()='Начинки']/parent::div"
BREAD_LOCATOR = ".//main/section/div/div/span[text()='Булки']/parent::div"
SAUCES_LOCATOR = ".//main/section/div/div/span[text()='Соусы']/parent::div"
BREAD_HEADER_LOCATOR = ".//main/section/div/h2[text()='Булки']"
SAUCES_HEADER_LOCATOR = ".//main/section/div/h2[text()='Соусы']"
TOPPING_HEADER_LOCATOR = ".//main/section/div/h2[text()='Начинки']"


class TestMainPage:

    def test_open_main_page_from_navbar_button(self, driver, random_email, random_password):
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
            expected_conditions.visibility_of_element_located((By.XPATH, NAVBAR_CONSTRUCTOR_BUTTON_LOCATOR)))
        driver.find_element(By.XPATH, NAVBAR_CONSTRUCTOR_BUTTON_LOCATOR).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.url_to_be(BASE_URL))
        assert driver.current_url == BASE_URL

    def test_open_main_page_from_navbar_logo(self, driver, random_email, random_password):
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
            expected_conditions.visibility_of_element_located((By.XPATH, NAVBAR_LOGO_BUTTON_LOCATOR)))
        driver.find_element(By.XPATH, NAVBAR_LOGO_BUTTON_LOCATOR).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.url_to_be(BASE_URL))
        assert driver.current_url == BASE_URL

    def test_bread_button_scroll(self, driver):
        driver.get(BASE_URL)
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, SAUCES_LOCATOR)))
        # спрячем раздел булки, т.к. он виден по умолчанию
        driver.find_element(By.XPATH, SAUCES_LOCATOR).click()
        time.sleep(1)
        driver.find_element(By.XPATH, BREAD_LOCATOR).click()
        time.sleep(1)
        assert driver.find_element(By.XPATH, BREAD_HEADER_LOCATOR).location["y"] >= 0

    def test_sauce_button_scroll(self, driver):
        driver.get(BASE_URL)
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, TOPPING_LOCATOR)))
        # спрячем раздел соусы, т.к. он виден по умолчанию
        driver.find_element(By.XPATH, TOPPING_LOCATOR).click()
        time.sleep(1)
        driver.find_element(By.XPATH, SAUCES_LOCATOR).click()
        time.sleep(1)
        assert driver.find_element(By.XPATH, SAUCES_HEADER_LOCATOR).location["y"] >= 0

    def test_topping_button_scroll(self, driver):
        driver.get(BASE_URL)

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, TOPPING_LOCATOR)))
        initial_pos = driver.find_element(By.XPATH, TOPPING_HEADER_LOCATOR).location["y"]
        driver.find_element(By.XPATH, TOPPING_LOCATOR).click()
        time.sleep(1)
        current_pos = driver.find_element(By.XPATH, TOPPING_HEADER_LOCATOR).location["y"]
        assert initial_pos > current_pos
