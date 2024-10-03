from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from all_locators import Locators


class TestLogin:

    def test_login_from_main_page(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(*Locators.LOGIN_BUTTON_FROM_MAIN_PAGE).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.LOGIN_BUTTON_AUTH))
        driver.find_element(*Locators.EMAIL_INPUT_AUTH).send_keys('g_bat_14@ya.ru')
        driver.find_element(*Locators.PASSWORD_INPUT_AUTH).send_keys('123456')
        driver.find_element(*Locators.LOGIN_BUTTON_AUTH).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.PLACE_ORDER_BUTTON))
        assert driver.find_element(*Locators.PLACE_ORDER_BUTTON).text == "Оформить заказ"

    def test_login_from_profile(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(*Locators.PROFILE_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.LOGIN_BUTTON_AUTH))
        driver.find_element(*Locators.EMAIL_INPUT_AUTH).send_keys('g_bat_14@ya.ru')
        driver.find_element(*Locators.PASSWORD_INPUT_AUTH).send_keys('123456')
        driver.find_element(*Locators.LOGIN_BUTTON_AUTH).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.PLACE_ORDER_BUTTON))
        assert driver.find_element(*Locators.PLACE_ORDER_BUTTON).text == "Оформить заказ"

    def test_login_from_link_on_registration_page(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/register')
        driver.find_element(*Locators.LOGIN_LINK_FROM_REG_PAGE).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.LOGIN_BUTTON_AUTH))
        driver.find_element(*Locators.EMAIL_INPUT_AUTH).send_keys('g_bat_14@ya.ru')
        driver.find_element(*Locators.PASSWORD_INPUT_AUTH).send_keys('123456')
        driver.find_element(*Locators.LOGIN_BUTTON_AUTH).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.PLACE_ORDER_BUTTON))
        assert driver.find_element(*Locators.PLACE_ORDER_BUTTON).text == "Оформить заказ"

    def test_login_from_link_on_recover_password_page(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/forgot-password')
        driver.find_element(*Locators.LOGIN_LINK_FROM_RECOVER_PASSWORD_PAGE).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.LOGIN_BUTTON_AUTH))
        driver.find_element(*Locators.EMAIL_INPUT_AUTH).send_keys('g_bat_14@ya.ru')
        driver.find_element(*Locators.PASSWORD_INPUT_AUTH).send_keys('123456')
        driver.find_element(*Locators.LOGIN_BUTTON_AUTH).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.PLACE_ORDER_BUTTON))
        assert driver.find_element(*Locators.PLACE_ORDER_BUTTON).text == "Оформить заказ"
