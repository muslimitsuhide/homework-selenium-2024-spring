import pytest
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base_case import BaseCase
from ui.locators.guide_page_locators import GuidePageLocators

class TestGuide(BaseCase):
    def test_open_guide_modal(self, guide_page):
        guide_page.click_guide_button()
        WebDriverWait(guide_page.driver, 10).until(
            EC.invisibility_of_element_located(guide_page.locators.GUIDE_MODAL)
        )
        assert guide_page.guide_modal_page_became_visible(), "Модальное окно обучения не открылось"

    def test_click_guide_modal_cancel_button(self, guide_page):
        guide_page.click_guide_button()
        guide_page.click_guide_close_button()
        WebDriverWait(guide_page.driver, 10).until(
            EC.invisibility_of_element_located(guide_page.locators.GUIDE_MODAL)
        )
        assert not guide_page.guide_modal_page_became_visible(), "Модальное окно обучения должно быть закрыто после нажатия на крестик"

    def test_open_community_modal(self, guide_page):
        guide_page.click_guide_button()
        guide_page.click_guide_community_button()
        assert guide_page.guide_inner_modal_became_visible(), "Модальное окно 'Сообщество ВКонтакте' не открылось"

    def test_close_community_modal(self, guide_page):
        guide_page.click_guide_button()
        guide_page.click_guide_community_button()
        guide_page.click_guide_close_button()
        WebDriverWait(guide_page.driver, 10).until(
            EC.invisibility_of_element_located(guide_page.locators.INNER_MODAL)
        )
        assert not guide_page.guide_inner_modal_became_visible(), "Модальное окно 'Сообщество ВКонтакте' должно быть закрыто после нажатия на крестик"
        assert not guide_page.guide_modal_page_became_visible(), "Модальное окно обучения должно быть закрыто после нажатия на крестик"

    def test_open_community_video_modal(self, guide_page):
        guide_page.click_guide_button()
        guide_page.click_guide_community_button()
        guide_page.click_video_button()
        assert guide_page.guide_campaign_video_became_visible(), "Модальное окно с видеороликом не открылось"

    def test_close_community_video_modal(self, guide_page):
        guide_page.click_guide_button()
        guide_page.click_guide_community_button()
        guide_page.click_video_button()
        assert guide_page.guide_campaign_video_became_visible(), "Модальное окно с видеороликом не открылось"
        guide_page.click_guide_close_button()
        WebDriverWait(guide_page.driver, 10).until(
            EC.invisibility_of_element_located(guide_page.locators.VIDEO_MODAL)
        )
        assert not guide_page.guide_campaign_video_became_visible(), "Модальное окно окно с видеороликом должно быть закрыто после нажатия на крестик"
        assert not guide_page.guide_modal_page_became_visible(), "Модальное окно обучения должно быть закрыто после нажатия на крестик"

    def test_open_catalog_modal(self, guide_page):
        guide_page.click_guide_button()
        guide_page.click_guide_catalog_button()
        assert guide_page.guide_inner_modal_became_visible(), "Модальное окно 'Каталог товаров' не открылось"

    def test_close_community_modal(self, guide_page):
        guide_page.click_guide_button()
        guide_page.click_guide_catalog_button()
        guide_page.click_guide_close_button()
        WebDriverWait(guide_page.driver, 10).until(
            EC.invisibility_of_element_located(guide_page.locators.INNER_MODAL)
        )
        assert not guide_page.guide_inner_modal_became_visible(), "Модальное окно 'Каталог товаров' должно быть закрыто после нажатия на крестик"
        assert not guide_page.guide_modal_page_became_visible(), "Модальное окно обучения должно быть закрыто после нажатия на крестик"

    