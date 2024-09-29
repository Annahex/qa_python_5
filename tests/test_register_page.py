from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


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





