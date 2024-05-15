from ui.pages.base_page import BasePage
from ui.locators.center_commerce_page_locators import CenterCommercePageLocators

class CenterCommercePage(BasePage):
    url = 'https://ads.vk.com/hq/ecomm/catalogs'
    locators = CenterCommercePageLocators()

    def catalog_modal_page_became_visible(self) -> bool:
        return self.became_visible(self.locators.CATALOG_MODAL_PAGE)

    def learning_modal_page_became_visible(self) -> bool:
        return self.became_visible(self.locators.LEARNING_MODAL)
    
    def choice_learning_modal_page_became_visible(self) -> bool:
        return self.became_visible(self.locators.CHOICE_LEARNING_MODAL)

    def close_training_modal(self):
        self.click(self.locators.LEARNING_MODAL_DISMISS_BUTTON)

    def click_create_catalog_button(self):
        self.click(self.locators.CREATE_CATALOG_BUTTON)

    def click_training_button(self):
        self.click(self.locators.TRAINING_BUTTON)

    def сlick_choice_learning(self):
        self.click(self.locators.TRAINING_BUTTON)

    def cancel_catalog_button(self):
        self.click(self.locators.CATALOG_CANCEL_BUTTON)

    def close_catalog_button(self):
        self.click(self.locators.CATALOG_CLOSE_BUTTON)