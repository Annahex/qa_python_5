from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import time


class TestRegisterPage:

    def test_success_registration(self, register_url, login_url, base_url, random_email, random_password):
        driver = webdriver.Chrome()
        driver.get(register_url)
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ".//form//input")))
        for input_element in driver.find_elements(By.XPATH, ".//input[@name='name']"):
            input_element.send_keys(random_email)
        driver.find_element(By.XPATH, ".//input[@name='Пароль']").send_keys(random_password)
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ".//form//input")))
        driver.find_element(By.XPATH, ".//form/button").click()
        WebDriverWait(driver, 3).until(
            expected_conditions.url_to_be(login_url))
        assert driver.current_url == login_url
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ".//form//input")))
        driver.find_element(By.XPATH, ".//input[@name='name']").send_keys(random_email)
        driver.find_element(By.XPATH, ".//input[@name='Пароль']").send_keys(random_password)
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ".//form//input")))
        driver.find_element(By.XPATH, ".//form/button").click()
        WebDriverWait(driver, 3).until(
            expected_conditions.url_to_be(base_url))
        assert driver.current_url == base_url
        driver.quit()

    def test_wrong_password(self, register_url, last_generated_email):
        wrong_password = "1"
        driver = webdriver.Chrome()
        driver.get(register_url)
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ".//form//input")))
        for input_element in driver.find_elements(By.XPATH, ".//input[@name='name']"):
            input_element.send_keys(last_generated_email)
        driver.find_element(By.XPATH, ".//input[@name='Пароль']").send_keys(wrong_password)
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ".//form//input")))
        driver.find_element(By.XPATH, ".//form/button").click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, ".//fieldset//p[text()='Некорректный пароль']")))
        assert driver.current_url == register_url
        driver.quit()

    def test_open_login_page_from_main_page(self, base_url, login_url):
        driver = webdriver.Chrome()
        driver.get(base_url)
        locator = ".//main/section//button[text()='Войти в аккаунт']"
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, locator)))
        driver.find_element(By.XPATH, locator).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.url_to_be(login_url))
        assert driver.current_url == login_url
        driver.quit()

    def test_open_login_page_from_navbar(self, base_url, login_url):
        driver = webdriver.Chrome()
        driver.get(base_url)
        locator = ".//nav//p[text()='Личный Кабинет']/parent::a"
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, locator)))
        driver.find_element(By.XPATH, locator).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.url_to_be(login_url))
        assert driver.current_url == login_url
        driver.quit()

    def test_open_login_page_from_register_page(self, register_url, login_url):
        driver = webdriver.Chrome()
        driver.get(register_url)
        locator = ".//main/div/div/p/a"
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, locator)))
        driver.find_element(By.XPATH, locator).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.url_to_be(login_url))
        assert driver.current_url == login_url
        driver.quit()

    def test_open_login_page_from_forgot_password_page(self, forgot_password_url, login_url):
        driver = webdriver.Chrome()
        driver.get(forgot_password_url)
        locator = ".//main/div/div/p/a"
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, locator)))
        driver.find_element(By.XPATH, locator).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.url_to_be(login_url))
        assert driver.current_url == login_url
        driver.quit()

    def test_open_account_page_from_navbar(
            self, account_url, login_url, base_url, last_generated_password, last_generated_email):
        driver = webdriver.Chrome()
        driver.get(login_url)
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ".//form//input")))
        driver.find_element(By.XPATH, ".//input[@name='name']").send_keys(last_generated_email)
        driver.find_element(By.XPATH, ".//input[@name='Пароль']").send_keys(last_generated_password)
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ".//form//input")))
        driver.find_element(By.XPATH, ".//form/button").click()
        WebDriverWait(driver, 3).until(
            expected_conditions.url_to_be(base_url))
        assert driver.current_url == base_url
        locator = ".//nav//p[text()='Личный Кабинет']/parent::a"
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, locator)))
        driver.find_element(By.XPATH, locator).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.url_to_be(account_url))
        assert driver.current_url == account_url
        driver.quit()

    def test_open_main_page_from_navbar_button(
            self, account_url, login_url, base_url, last_generated_password, last_generated_email):
        driver = webdriver.Chrome()
        driver.get(login_url)
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ".//form//input")))
        driver.find_element(By.XPATH, ".//input[@name='name']").send_keys(last_generated_email)
        driver.find_element(By.XPATH, ".//input[@name='Пароль']").send_keys(last_generated_password)
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ".//form//input")))
        driver.find_element(By.XPATH, ".//form/button").click()
        WebDriverWait(driver, 3).until(
            expected_conditions.url_to_be(base_url))
        assert driver.current_url == base_url
        locator = ".//nav//p[text()='Личный Кабинет']/parent::a"
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, locator)))
        driver.find_element(By.XPATH, locator).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.url_to_be(account_url))
        assert driver.current_url == account_url
        locator = ".//nav//p[text()='Конструктор']/parent::a"
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, locator)))
        driver.find_element(By.XPATH, locator).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.url_to_be(base_url))
        assert driver.current_url == base_url
        driver.quit()

    def test_open_main_page_from_navbar_logo(
            self, account_url, login_url, base_url, last_generated_password, last_generated_email):
        driver = webdriver.Chrome()
        driver.get(login_url)
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ".//form//input")))
        driver.find_element(By.XPATH, ".//input[@name='name']").send_keys(last_generated_email)
        driver.find_element(By.XPATH, ".//input[@name='Пароль']").send_keys(last_generated_password)
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ".//form//input")))
        driver.find_element(By.XPATH, ".//form/button").click()
        WebDriverWait(driver, 3).until(
            expected_conditions.url_to_be(base_url))
        assert driver.current_url == base_url
        locator = ".//nav//p[text()='Личный Кабинет']/parent::a"
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, locator)))
        driver.find_element(By.XPATH, locator).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.url_to_be(account_url))
        assert driver.current_url == account_url
        locator = ".//nav//div/a[@href='/']"
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, locator)))
        driver.find_element(By.XPATH, locator).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.url_to_be(base_url))
        assert driver.current_url == base_url
        driver.quit()

    def test_logout_from_account_page(
            self, account_url, login_url, base_url, last_generated_password, last_generated_email):
        driver = webdriver.Chrome()
        driver.get(login_url)
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ".//form//input")))
        driver.find_element(By.XPATH, ".//input[@name='name']").send_keys(last_generated_email)
        driver.find_element(By.XPATH, ".//input[@name='Пароль']").send_keys(last_generated_password)
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ".//form//input")))
        driver.find_element(By.XPATH, ".//form/button").click()
        WebDriverWait(driver, 3).until(
            expected_conditions.url_to_be(base_url))
        assert driver.current_url == base_url
        locator = ".//nav//p[text()='Личный Кабинет']/parent::a"
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, locator)))
        driver.find_element(By.XPATH, locator).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.url_to_be(account_url))
        assert driver.current_url == account_url
        locator = ".//main/div/nav/ul/li/button[text()='Выход']"
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, locator)))
        driver.find_element(By.XPATH, locator).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.url_to_be(login_url))
        assert driver.current_url == login_url
        driver.quit()