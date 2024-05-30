from ui.pages.base_page import BasePage
from selenium.webdriver import Keys
from ui.locators.surveys_page_locators import SurveysPageLocators
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC


class SurveysPage(BasePage):
    url = 'https://ads.vk.com/hq/leadads/surveys'
    locators = SurveysPageLocators()

    def click_create_surveys_button(self):
        self.click(self.locators.CREATE_SURVEY_BUTTON, timeout=1)
        
    def click_cross_button(self):
        self.click(self.locators.CROSS_BUTTON, timeout=1)
        
    def click_questions_button(self):
        self.click(self.locators.QUESTIONS_BUTTON, timeout=1)

    def cross_button_became_visible(self) -> bool:
        return self.became_visible(self.locators.CROSS_BUTTON)
    
    def create_survey_modal_page_became_visible(self) -> bool:
        return self.became_visible(self.locators.SURVEY_CREATE_MODAL, timeout=1)
    
    def create_survey_modal_page_became_invisible(self) -> bool:
        return self.became_invisible(self.locators.SURVEY_CREATE_MODAL, timeout=2)
    
    def create_survey_questions_list_became_visible(self) -> bool:
        return self.became_visible(self.locators.QUESTION_LIST, timeout=1)
    
    def create_survey_questions_list_became_invisible(self) -> bool:
        return self.became_invisible(self.locators.QUESTION_LIST, timeout=2)
    

    def set_survey_name_input(self, str: str):
        elem = self.find(self.locators.SURVEY_NAME_INPUT)
        self.driver.execute_script("arguments[0].value = '';", elem)
        elem.send_keys(str)

    def get_survey_name_input_value(self):
        elem = self.find(self.locators.SURVEY_NAME_INPUT)
        return elem.get_attribute('value')
    
    
    def set_survey_company_name_input(self, str: str):
        elem = self.find(self.locators.SURVEY_COMPANY_NAME_INPUT)
        self.driver.execute_script("arguments[0].value = '';", elem)
        elem.send_keys(str)

    def get_survey_company_name_input_value(self):
        elem = self.find(self.locators.SURVEY_COMPANY_NAME_INPUT)
        return elem.get_attribute('value')
    

    def set_survey_title_input(self, str: str):
        elem = self.find(self.locators.SURVEY_TITLE_INPUT)
        self.driver.execute_script("arguments[0].value = '';", elem)
        elem.send_keys(str)

    def get_survey_title_input_value(self):
        elem = self.find(self.locators.SURVEY_TITLE_INPUT)
        return elem.get_attribute('value')
    
    
    def set_survey_description_input(self, str: str):
        elem = self.find(self.locators.SURVEY_DESCRIPTION_INPUT)
        self.driver.execute_script("arguments[0].value = '';", elem)
        elem.send_keys(str)

    def get_survey_description_input_value(self):
        elem = self.find(self.locators.SURVEY_DESCRIPTION_INPUT)
        return elem.get_attribute('value')
    