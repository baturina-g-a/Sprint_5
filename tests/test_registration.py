import random

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from all_locators import Locators


class TestRegistration:

    def test_successful_registration_with_correct_data(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/register')
        driver.find_element(*Locators.NAME_INPUT_FIELD_REG).send_keys('name')
        driver.find_element(*Locators.EMAIL_INPUT_FIELD_REG).send_keys('g_baturina_14' +
                                                                       str(random.randint(100, 999)) + '@yandex.ru')
        driver.find_element(*Locators.PASSWORD_INPUT_FIELD_REG).send_keys('123456')
        driver.find_element(*Locators.REGISTER_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.LOGIN_BUTTON_AUTH))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

    def test_invalid_password_error(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/register')
        driver.find_element(*Locators.PASSWORD_INPUT_FIELD_REG).send_keys('12345')
        driver.find_element(*Locators.REGISTER_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            Locators.INVALID_PASSWORD_ERROR))
        assert driver.find_element(*Locators.INVALID_PASSWORD_ERROR).text == "Некорректный пароль"
