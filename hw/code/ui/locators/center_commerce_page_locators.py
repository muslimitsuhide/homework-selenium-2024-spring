from selenium.webdriver.common.by import By
from ui.locators.base_page_locators import BasePageLocators

class CenterCommercePageLocators(BasePageLocators):
    CREATE_CATALOG_BUTTON = (By.XPATH, "//*[contains(@class, 'vkuiButton__content') and text()='Создать каталог']")
    TRAINING_BUTTON = (By.XPATH, "//button[@data-testid='ecomm-onboarding-start']")
    CATALOG_MODAL_PAGE = (By.CLASS_NAME, "ModalSidebarPage_container__Zopae")
    
    CATALOG_CANCEL_BUTTON = (By.XPATH, "//button[@data-testid='cancel']")
    CATALOG_CLOSE_BUTTON = (By.XPATH, "//button[@aria-label='Close']")
    
    LEARNING_MODAL = (By.CLASS_NAME, "vkuiModalCardBase__container")
    LEARNING_MODAL_DISMISS_BUTTON = (By.XPATH, "//button[@class='vkuiButton vkuiButton--size-l vkuiButton--mode-secondary vkuiButton--appearance-accent vkuiButton--align-center vkuiButton--sizeY-none vkuiButton--stretched vkuiTappable vkuiInternalTappable vkuiTappable--hasHover vkuiTappable--hasActive vkui-focus-visible']//*[contains(text(),'Не сейчас')]")
    LEARNING_MODAL_CLOSE_BUTTON = (By.XPATH, "//div[@class='vkuiModalDismissButton vkuiTappable vkuiInternalTappable vkuiTappable--hasHover vkuiTappable--hasActive vkui-focus-visible']//*[name()='svg']")

    CHOICE_LEARNING_MODAL = (By.CLASS_NAME, "vkuiModalPage__content-wrap")
    CLOSE_MODAL_BUTTON = (By.CSS_SELECTOR, ".vkuiModalDismissButton")

    CATALOG_NAME_INPUT = (By.XPATH, "//input[@data-testid='catalogName-input']")
    CATALOG_SOURCE_TYPE_FEED = (By.XPATH, "//div[@data-entityid='url']")
    CATALOG_SOURCE_TYPE_MARKETPLACE = (By.XPATH, "//div[@data-entityid='marketplace']")
    CATALOG_SOURCE_TYPE_FILE = (By.XPATH, "//div[@data-entityid='file']")
    
    SUBMIT_BUTTON = (By.XPATH, "//button[@data-testid='submit']")
    CANCEL_BUTTON = (By.XPATH, "//button[@data-testid='cancel']")
