from ui.locators.auth_page_locators import AuthPageLocators
from ui.pages.base_page import BasePage


class AuthPage(BasePage):
    locators = AuthPageLocators()

    def login(self, login, password):
        self.click(self.locators.CABINET_LOCATOR)
        self.click(self.locators.OAUTH_LOCATOR)

        self.find_clickable(self.locators.USERNAME).send_keys(login)
        self.click(self.locators.OAUTH_SUBMIT)

        self.find_clickable(self.locators.PASSWORD).send_keys(password)
        self.click(self.locators.OAUTH_SUBMIT)