from ui.pages.base_page import BasePage
from ui.locators.main_page_locators import MainPageLocators

class MainPage(BasePage):
    locators = MainPageLocators()
    url = 'https://ads.vk.com/'


    def change_slide(self):
        self.click(self.locators.NONACTIVE_CIRCLE)

    def click_slider_cabinet_button(self):
        self.click(self.locators.SLIDER_BUTTON('/hq'))