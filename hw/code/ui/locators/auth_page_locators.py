from selenium.webdriver.common.by import By


class AuthPageLocators:
    CABINET_LOCATOR = (By.CLASS_NAME, "ButtonCabinet_primary__LCfol")
    OAUTH_LOCATOR = (By.XPATH, ".//button[@data-test-id='oAuthService_mail_ru']")
    USERNAME = (By.NAME, "username")
    PASSWORD = (By.NAME, "password")
    OAUTH_SUBMIT = (By.CLASS_NAME, "submit-button-wrap")