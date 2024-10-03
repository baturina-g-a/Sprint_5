from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from all_locators import Locators


class TestGoToConstructor:

    def test_access_to_constructor_through_the_constructor_button(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/login')
        driver.find_element(*Locators.EMAIL_INPUT_AUTH).send_keys('g_bat_14@ya.ru')
        driver.find_element(*Locators.PASSWORD_INPUT_AUTH).send_keys('123456')
        driver.find_element(*Locators.LOGIN_BUTTON_AUTH).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.PLACE_ORDER_BUTTON))
        driver.find_element(*Locators.PROFILE_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            Locators.PROFILE_PAGE_DESCRIPTION))
        driver.find_element(*Locators.CONSTRUCTOR_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.PLACE_ORDER_BUTTON))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

    def test_access_to_constructor_through_the_logo(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/login')
        driver.find_element(*Locators.EMAIL_INPUT_AUTH).send_keys('g_bat_14@ya.ru')
        driver.find_element(*Locators.PASSWORD_INPUT_AUTH).send_keys('123456')
        driver.find_element(*Locators.LOGIN_BUTTON_AUTH).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.PLACE_ORDER_BUTTON))
        driver.find_element(*Locators.PROFILE_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            Locators.PROFILE_PAGE_DESCRIPTION))
        driver.find_element(*Locators.LOGO).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.PLACE_ORDER_BUTTON))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
