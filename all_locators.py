from selenium.webdriver.common.by import By


class Locators:
    # поле для ввода имени в форме регистрации:
    NAME_INPUT_FIELD_REG = (By.XPATH, '//label[text()="Имя"]/parent::div/input')

    # поле для ввода эл.почты в форме регистрации:
    EMAIL_INPUT_FIELD_REG = (By.XPATH, '//label[text()="Email"]/parent::div/input')

    # поле для ввода пароля в форме регистрации:
    PASSWORD_INPUT_FIELD_REG = (By.XPATH, '//label[text()="Пароль"]/parent::div/input')

    # кнопка "Зарегистрироваться" в форме регистрации:
    REGISTER_BUTTON = (By.XPATH, '//button[text()="Зарегистрироваться"]')

    # ошибка при некорректном пароле:
    INVALID_PASSWORD_ERROR = (By.XPATH, '//p[text()="Некорректный пароль"]')

    # кнопка "Войти" в форме авторизации:
    LOGIN_BUTTON_AUTH = (By.XPATH, '//button[text()="Войти"]')

    # кнопка «Войти в аккаунт» на главной:
    LOGIN_BUTTON_FROM_MAIN_PAGE = (By.XPATH, '//button[text()="Войти в аккаунт"]')

    # кнопка "Личный кабинет":
    PROFILE_BUTTON = (By.XPATH, '//p[text()="Личный Кабинет"]')

    # ссылка "Войти" на странице регистрации:
    LOGIN_LINK_FROM_REG_PAGE = (By.XPATH, '//a[@class="Auth_link__1fOlj"]')

    # ссылка "Войти" на странице восстановления пароля:
    LOGIN_LINK_FROM_RECOVER_PASSWORD_PAGE = (By.XPATH, '//a[@class="Auth_link__1fOlj"]')

    # поле для ввода эл.почты в форме регистрации:
    EMAIL_INPUT_AUTH = (By.XPATH, '//label[text()="Email"]/parent::div/input')

    # поле для ввода пароля в форме регистрации:
    PASSWORD_INPUT_AUTH = (By.XPATH, '//label[text()="Пароль"]/parent::div/input')

    # кнопка "Оформить заказ" на главной:
    PLACE_ORDER_BUTTON = (By.XPATH, '//button[text()="Оформить заказ"]')

    # текст описания страницы "Личный кабинет":
    PROFILE_PAGE_DESCRIPTION = (By.XPATH, '//p[contains(text(), "В этом разделе")]')

    # кнопка "Конструктор":
    CONSTRUCTOR_BUTTON = (By.XPATH, '//p[text()="Конструктор"]')

    # логотип:
    LOGO = (By.CLASS_NAME, 'AppHeader_header__logo__2D0X2')

    # кнопка "Выход" в личном кабинете:
    LOGOUT_BUTTON = (By.XPATH, '//button[text()="Выход"]')

    # активный таб в конструкторе бургеров:
    ACTIVE_TAB = (By.XPATH, '//div[contains(@class, "type_current")]')

    # таб "Булки" в конструкторе бургеров:
    BULKI_TAB = (By.XPATH, '//span[text() = "Булки"]')

    # таб "Соусы" в конструкторе бургеров:
    SOUSI_TAB = (By.XPATH, '//span[text() = "Соусы"]')

    # таб "Начинки" в конструкторе бургеров:
    NACHINKI_TAB = (By.XPATH, '//span[text() = "Начинки"]')
