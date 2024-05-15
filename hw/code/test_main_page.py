from base_case import BaseCase
from ui.fixtures import main_page
import time

class TestMainPage(BaseCase):
    def test_go_to_auth(self, main_page):
        main_page.change_slide()
        main_page.click_slider_cabinet_button()
        self.driver.close()