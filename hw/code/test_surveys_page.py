import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
from base_case import BaseCase

SURVEY_NAME = 'SURVEY_NAME'
SURVEY_COMPANY_NAME = 'SURVEY_COMPANY_NAME'
SURVEY_TITLE = 'SURVEY_TITLE'
SURVEY_DESCRIPTION = 'SURVEY_DESCRIPTION'

class TestSurveysPage(BaseCase):
    def test_create_surveys_modal_page_opened(self, surveys_page):
        surveys_page.click_create_surveys_button()
        assert surveys_page.cross_button_became_visible()
        assert surveys_page.create_survey_modal_page_became_visible()

    def test_create_surveys_modal_page_closed(self, surveys_page):
        surveys_page.click_create_surveys_button()
        assert surveys_page.cross_button_became_visible()
        surveys_page.click_cross_button()
        assert surveys_page.create_survey_modal_page_became_invisible()

    def test_open_questions_when_fields_are_empty(self, surveys_page):
        surveys_page.click_create_surveys_button()
        assert surveys_page.cross_button_became_visible()
        surveys_page.click_questions_button()
        assert surveys_page.create_survey_questions_list_became_invisible()

    def test_open_questions_when_fields_are_empty(self, surveys_page):
        surveys_page.click_create_surveys_button()
        assert surveys_page.cross_button_became_visible()

    def test_set_survey_name_input(self, surveys_page):
        surveys_page.click_create_surveys_button()
        assert surveys_page.cross_button_became_visible()

        surveys_page.set_survey_name_input(SURVEY_NAME)        
        actual_survey_name = surveys_page.get_survey_name_input_value()
        assert actual_survey_name == SURVEY_NAME, f"Expected '{SURVEY_NAME}', but got '{actual_survey_name}'"

    def test_set_survey_company_name_input(self, surveys_page):
        surveys_page.click_create_surveys_button()
        assert surveys_page.cross_button_became_visible()

        surveys_page.set_survey_company_name_input(SURVEY_COMPANY_NAME)        
        actual_survey_company_name = surveys_page.get_survey_company_name_input_value()
        assert actual_survey_company_name == SURVEY_COMPANY_NAME, f"Expected '{SURVEY_COMPANY_NAME}', but got '{actual_survey_company_name}'"
 
    def test_set_survey_title_input(self, surveys_page):
        surveys_page.click_create_surveys_button()
        assert surveys_page.cross_button_became_visible()

        surveys_page.set_survey_title_input(SURVEY_TITLE)        
        actual_survey_title = surveys_page.get_survey_title_input_value()
        assert actual_survey_title == SURVEY_TITLE, f"Expected '{SURVEY_TITLE}', but got '{actual_survey_title}'"

    def test_set_survey_description_input(self, surveys_page):
        surveys_page.click_create_surveys_button()
        assert surveys_page.cross_button_became_visible()

        surveys_page.set_survey_description_input(SURVEY_DESCRIPTION)        
        actual_survey_description = surveys_page.get_survey_description_input_value()
        assert actual_survey_description == SURVEY_DESCRIPTION, f"Expected '{SURVEY_DESCRIPTION}', but got '{actual_survey_description}'"
