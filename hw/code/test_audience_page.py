import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base_case import BaseCase

class TestAudience(BaseCase):
    def test_creating_audience(self, audience_page):
        audience_page.click_audience_create_button()
        WebDriverWait(audience_page.driver, 10).until(
            EC.visibility_of_element_located(audience_page.locators.AUDIENCE_CREATE_MODAL)
        )
        assert audience_page.audience_modal_became_visible(), "Модальное окно не открылось"

        audience_page.click_audience_add_source_button()
        assert audience_page.audience_add_source_modal_became_visible(), "Модальное окно не открылось"
        
        audience_page.click_audience_source_phrase_button()
        audience_page.enter_source_name("as")        
        audience_page.enter_phrase_name("as")    

        audience_page.click_save_phrase_button()        
        audience_page.click_save_button1()      
        
        WebDriverWait(audience_page.driver, 10).until(
            EC.visibility_of_element_located(audience_page.locators.AUDIENCE_ITEM)
        )
        assert audience_page.audience_item_became_visible(), "Элемент аудитории не появился на странице"
  
        audience_page.hover_and_click_delete()
