from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from all_locators import Locators


class TestGoToProfile:

    def test_access_to_profile_by_click_on_profile_button(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(*Locators.PROFILE_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.LOGIN_BUTTON_AUTH))
        driver.find_element(*Locators.EMAIL_INPUT_AUTH).send_keys('g_bat_14@ya.ru')
        driver.find_element(*Locators.PASSWORD_INPUT_AUTH).send_keys('123456')
        driver.find_element(*Locators.LOGIN_BUTTON_AUTH).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.PLACE_ORDER_BUTTON))
        driver.find_element(*Locators.PROFILE_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            Locators.PROFILE_PAGE_DESCRIPTION))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'
