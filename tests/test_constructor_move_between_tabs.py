from all_locators import Locators


class TestConstructor:

    def test_default_tab(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        tab = driver.find_element(*Locators.BULKI_TAB).text
        assert tab == driver.find_element(*Locators.ACTIVE_TAB).text

    def test_move_to_sousi_from_bulki(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(*Locators.SOUSI_TAB).click()
        tab = driver.find_element(*Locators.SOUSI_TAB).text
        assert tab == driver.find_element(*Locators.ACTIVE_TAB).text

    def test_move_to_nachinki_from_bulki(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(*Locators.NACHINKI_TAB).click()
        tab = driver.find_element(*Locators.NACHINKI_TAB).text
        assert tab == driver.find_element(*Locators.ACTIVE_TAB).text

    def test_move_to_nachinki_from_sousi(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(*Locators.SOUSI_TAB).click()
        driver.find_element(*Locators.NACHINKI_TAB).click()
        tab = driver.find_element(*Locators.NACHINKI_TAB).text
        assert tab == driver.find_element(*Locators.ACTIVE_TAB).text

    def test_move_to_bulki_from_nachinki(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(*Locators.NACHINKI_TAB).click()
        driver.find_element(*Locators.BULKI_TAB).click()
        tab = driver.find_element(*Locators.BULKI_TAB).text
        assert tab == driver.find_element(*Locators.ACTIVE_TAB).text

    def test_move_to_sousi_from_nachinki(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(*Locators.NACHINKI_TAB).click()
        driver.find_element(*Locators.SOUSI_TAB).click()
        tab = driver.find_element(*Locators.SOUSI_TAB).text
        assert tab == driver.find_element(*Locators.ACTIVE_TAB).text

    def test_move_to_bulki_from_sousi(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(*Locators.SOUSI_TAB).click()
        driver.find_element(*Locators.BULKI_TAB).click()
        tab = driver.find_element(*Locators.BULKI_TAB).text
        assert tab == driver.find_element(*Locators.ACTIVE_TAB).text
