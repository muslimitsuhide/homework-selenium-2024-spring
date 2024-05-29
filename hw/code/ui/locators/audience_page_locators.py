from selenium.webdriver.common.by import By
from ui.locators.base_page_locators import BasePageLocators

class AudiencePageLocators(BasePageLocators):
    AUDIENCE_CREATE_BUTTON = (By.XPATH, "//*[contains(@class, 'vkuiButton__content') and text()='Создать аудиторию']")
    AUDIENCE_CREATE_MODAL = (By.CLASS_NAME, "ModalSidebarPage_container__Zopae")

    AUDIENCE_ADD_SOURCE_BUTTON = (By.XPATH, "//*[contains(@class, 'vkuiButton__content') and text()='Добавить источник']")
    AUDIENCE_SOURCE_MODAL = (By.XPATH, "//*[text()='Включить источник']")

    AUDIENCE_SOURCE_PHRASE_BUTTON = (By.XPATH, "//*[text()='Ключевые фразы']")
    AUDIENCE_SOURCE_NAME_INPUT = (By.XPATH, "//h5[contains(@class, 'vkuiTypography') and text()='Название']/following-sibling::span//input[@type='text']")
    AUDIENCE_SOURCE_PHRASE_INPUT = (By.XPATH, "//*[@placeholder='Введите фразу и нажмите Enter']")

    SAVE_PHRASE_BUTTON = (By.XPATH, "(//*[text()='Сохранить'])[2]")
    SAVE_BUTTON_0 = (By.XPATH, "(//*[text()='Сохранить'])[0]")
    SAVE_BUTTON_1 = (By.XPATH, "(//*[text()='Сохранить'])[1]")
    SAVE_BUTTON_2 = (By.XPATH, "(//*[text()='Сохранить'])[2]")
    SAVE_BUTTON_3 = (By.XPATH, "(//*[text()='Сохранить'])[3]")

    AUDIENCE_ITEM = (By.CLASS_NAME, "NameCell_wrapper__hxqrL")

    AUDIENCE_MENU = (By.CLASS_NAME, "NameCell_details__WyuPr")
    DELETE_BUTTON = (By.XPATH, "(//*[text()='Удалить'])[1]")