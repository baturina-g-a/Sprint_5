from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from all_locators import Locators


class TestLogout:

    def test_logout_from_profile_by_button_exit(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/login')
        driver.find_element(*Locators.EMAIL_INPUT_AUTH).send_keys('g_bat_14@ya.ru')
        driver.find_element(*Locators.PASSWORD_INPUT_AUTH).send_keys('123456')
        driver.find_element(*Locators.LOGIN_BUTTON_AUTH).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.PLACE_ORDER_BUTTON))
        driver.find_element(*Locators.PROFILE_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            Locators.PROFILE_PAGE_DESCRIPTION))
        driver.find_element(*Locators.LOGOUT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.LOGIN_BUTTON_AUTH))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'
