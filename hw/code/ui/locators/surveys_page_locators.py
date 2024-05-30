from selenium.webdriver.common.by import By
from ui.locators.base_page_locators import BasePageLocators

class SurveysPageLocators(BasePageLocators):
    CREATE_SURVEY_BUTTON = (By.XPATH, "//*[text()='Создать опрос']")
    SURVEY_CREATE_MODAL = (By.CLASS_NAME, "ModalSidebarPage_container__Zopae")

    CROSS_BUTTON = (By.XPATH, "//button[@aria-label='close_button']")

    SURVEY_NAME_INPUT = (By.XPATH, "//input[@placeholder='Введите название']")
    SURVEY_COMPANY_NAME_INPUT = (By.XPATH, "//input[@placeholder='Введите название компании']")
    SURVEY_TITLE_INPUT = (By.XPATH, "//input[@placeholder='Введите заголовок']")
    SURVEY_DESCRIPTION_INPUT = (By.XPATH, "//textarea[@placeholder='Введите описание опроса']")
    
    QUESTIONS_BUTTON = (By.XPATH, "(//*[text()='Вопросы'])")

    QUESTION_LIST = (By.XPATH, "//*[@class='Question_question__vRl-h']")