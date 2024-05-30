from selenium.webdriver.common.by import By
from ui.locators.base_page_locators import BasePageLocators

class AudiencePageLocators(BasePageLocators):
    CREATE_AUDIENCE_BUTTON = (By.XPATH, "//*[contains(@class, 'vkuiButton__content') and text()='Создать аудиторию']")
    AUDIENCE_CREATE_MODAL = (By.CLASS_NAME, "ModalSidebarPage_container__Zopae")

    CREATE_AUDIENCE_MODAL_PAGE = (
        By.XPATH,
        "//*[contains(@class, 'ModalSidebarPage_') and child::h2[text()='Создание аудитории']]"
    )

    ERROR = (By.XPATH, "//*[@role='alert']")
    AUDIENCE_ADD_SOURCE_BUTTON = (By.XPATH, "//*[contains(@class, 'vkuiButton__content') and text()='Добавить источник']")
    AUDIENCE_SOURCE_MODAL = (By.XPATH, "//*[text()='Включить источник']")

    AUDIENCE_SOURCE_PHRASE_BUTTON = (By.XPATH, "//*[text()='Ключевые фразы']")
    AUDIENCE_SOURCE_NAME_INPUT = (By.XPATH, "//h5[contains(@class, 'vkuiTypography') and text()='Название']/following-sibling::span//input[@type='text']")
    AUDIENCE_SOURCE_PHRASE_INPUT = (By.XPATH, "//*[@placeholder='Введите фразу и нажмите Enter']")

    AUDIENCE_NAME_INPUT = (
        By.XPATH, 
        "//*[contains(@class, 'vkuiInput__el')]"
    )

    CROSS_BUTTON = (By.XPATH, "//button[@aria-label='Close']")
    CANCEL_BUTTON = (By.XPATH, "//button[@data-testid='cancel']")
    SUBMIT_BUTTON = (By.XPATH, "//button[@data-testid='submit']")

    @staticmethod
    def SOURCE_ITEM(item_name):
        return By.XPATH, f"//*[contains(@class, 'SourceTypeSelector_button__')]//*[text()='{item_name}']"
    
    ADD_SOURCE_BUTTON = (
        By.XPATH, 
        "//*[contains(@class, 'vkuiButton__content') and text()='Добавить источник']"
    )

    ADD_SOURCE_MODAL_PAGE = (
        By.XPATH,
        "//*[contains(@class, 'ModalSidebarPage_') and child::h2[text()='Включить источник']]"
    )

    SIDEBAR_SIGN = (
        By.XPATH, 
        "//*[contains(@class, 'vkuiTypography') and text()='Включить пользователей, которые соответствуют']"
    )

    SIDEBAR_SIGN_HINTS = (
        By.XPATH, 
        "//*[contains(@class, 'HintSelector_hintSelectorButton__') and text()='хотя бы одному из условий']"
    )

    KEY_PHRASES_MODAL_PAGE = (
        By.XPATH,
        "//*[contains(@class, 'ModalSidebarPage_') and child::h2[text()='Ключевые фразы']]"
    )

    SOURCE_CARD_CONTENT = (
        By.XPATH,
        "//*[contains(@class, 'SourcesList_wrapper__')]//*[contains(@class, 'InfoRow_content__')]"
    )

    MINUS_PHRASES_INPUT = (By.XPATH, "//*[contains(@class, 'KeyPhrases_negationPhrases__')]//textarea")
    KEY_PHRASES_INPUT = (By.XPATH, "//*[contains(@class, 'KeyPhrases_textarea__')]/textarea")
    PERIOD_INPUT = (By.XPATH, "//*[contains(@class, 'Context_daysInput__')]/input")

    SAVE_PHRASE_BUTTON = (By.XPATH, "(//*[text()='Сохранить'])[2]")
    SAVE_BUTTON_0 = (By.XPATH, "(//*[text()='Сохранить'])[0]")
    SAVE_BUTTON_2 = (By.XPATH, "(//*[text()='Сохранить'])[2]")

    MODAL_PAGE_SUBMIT_BUTTON = (By.XPATH, "//*[contains(@class, 'vkuiTappable--hasActive') and @type='submit']")
    CREATED_AUDIENCE_TITLE = (By.XPATH, "//*[contains(@class, 'NameCell_wrapper__')]/h5")
    AUDIENCE_ITEM = (By.CLASS_NAME, "NameCell_wrapper__hxqrL")

    AUDIENCE_MENU = (By.CLASS_NAME, "NameCell_details__WyuPr")
    DELETE_BUTTON = (By.XPATH, "(//*[text()='Удалить'])[1]")

    CANCEL_SOURCE_BUTTON = (By.XPATH, "(//button[@data-testid='cancel'])[2]")
    DELETE_CONFIRM_BUTTON = (By.XPATH, "(//*[text()='Удалить'])")
    DELETE_CONFIRM_MODAL = (By.XPATH, "(//*[text()='Удалить аудиторию?'])")

    SEARCH_INPUT = (By.XPATH, "//input[@placeholder='Поиск']")
