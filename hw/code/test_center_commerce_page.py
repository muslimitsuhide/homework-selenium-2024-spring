import pytest
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base_case import BaseCase
from ui.locators.center_commerce_page_locators import CenterCommercePageLocators

class TestCommerceCenter(BaseCase):

    # Главная
    def test_open_catalog_modal(self, center_commerce_page):
        center_commerce_page.close_training_modal()
        center_commerce_page.click_create_catalog_button()
        WebDriverWait(center_commerce_page.driver, 10).until(
            EC.invisibility_of_element_located(center_commerce_page.locators.CATALOG_MODAL_PAGE)
        )
        assert center_commerce_page.catalog_modal_page_became_visible(), "Модальное окно создания каталога не открылось"

    def test_click_catalog_modal_cancel_button(self, center_commerce_page):
        center_commerce_page.close_training_modal()
        center_commerce_page.click_create_catalog_button()
        center_commerce_page.cancel_catalog_button()
        WebDriverWait(center_commerce_page.driver, 10).until(
            EC.invisibility_of_element_located(center_commerce_page.locators.CATALOG_MODAL_PAGE)
        )
        assert not center_commerce_page.catalog_modal_page_became_visible(), "Модальное окно создания каталога должно быть закрыто после нажатия кнопки 'Отмена'"

    def test_click_catalog_modal_close_button(self, center_commerce_page):
        center_commerce_page.close_training_modal()
        center_commerce_page.click_create_catalog_button()
        center_commerce_page.close_catalog_button()
        WebDriverWait(center_commerce_page.driver, 10).until(
            EC.invisibility_of_element_located(center_commerce_page.locators.CATALOG_MODAL_PAGE)
        )
        
        assert not center_commerce_page.catalog_modal_page_became_visible(), "Модальное окно создания каталога должно быть закрыто после нажатия кнопки 'Закрыть'"


    def test_open_choice_learning_modal(self, center_commerce_page):
        center_commerce_page.close_training_modal()
        center_commerce_page.сlick_choice_learning()
        assert center_commerce_page.choice_learning_modal_page_became_visible(), "Модальное окно создания каталога не открылось"

    def test_close_choice_learning_modal(self, center_commerce_page):
        center_commerce_page.close_training_modal()
        center_commerce_page.сlick_choice_learning()
        WebDriverWait(center_commerce_page.driver, 10).until(
            EC.invisibility_of_element_located(center_commerce_page.locators.CHOICE_LEARNING_MODAL)
        )
        
        assert center_commerce_page.close_choice_learning_modal_page(), "Модальное окно создания каталога не закрылось"

    # Новый каталог
    def test_empty_catalog_name_error(self, center_commerce_page):
        center_commerce_page.close_training_modal()
        center_commerce_page.click_create_catalog_button()
        center_commerce_page.input_empty_catalog_name()
        center_commerce_page.click_submit_button()

        assert center_commerce_page.is_required_field_error_displayed(), "Ошибка 'Обязательное поле' не отображается"

    def test_create_catalog_with_feed(self, center_commerce_page):
        center_commerce_page.close_training_modal()
        center_commerce_page.click_create_catalog_button()
        center_commerce_page.select_feed_or_community()
        center_commerce_page.verify_feed_fields_visible()
        
    def test_create_catalog_with_marketplace(self, center_commerce_page):
        center_commerce_page.close_training_modal()
        center_commerce_page.click_create_catalog_button()
        center_commerce_page.select_marketplace()
        center_commerce_page.verify_marketplace_fields_visible()

    '''def test_create_catalog_manually(self, center_commerce_page):
        center_commerce_page.close_training_modal()
        center_commerce_page.click_create_catalog_button()
        center_commerce_page.select_manually()
        center_commerce_page.verify_manually_fields_visible()'''