import pytest
from base_case import BaseCase
from ui.locators.center_commerce_page_locators import CenterCommercePageLocators

class TestCommerceCenter(BaseCase):
    def test_open_catalog_modal(self, center_commerce_page):
       center_commerce_page.close_training_modal()
       center_commerce_page.click_create_catalog_button()
       assert center_commerce_page.catalog_modal_page_became_visible(), "Модальное окно создания каталога не открылось"

    def test_click_catalog_modal_dismiss_button(self, center_commerce_page):
        center_commerce_page.close_training_modal()
        center_commerce_page.click_create_catalog_button()
        center_commerce_page.close_training_modal()
        center_commerce_page.click_create_catalog_button()
        center_commerce_page.cancel_catalog_button()
        assert not center_commerce_page.catalog_modal_page_became_visible(), "Модальное окно создания каталога должно быть закрыто после нажатия кнопки 'Отмена'"

    def test_click_catalog_modal_close_button(self, center_commerce_page):
        center_commerce_page.close_training_modal()
        center_commerce_page.click_create_catalog_button()
        center_commerce_page.close_training_modal()
        center_commerce_page.click_create_catalog_button()
        center_commerce_page.close_catalog_button
        assert not center_commerce_page.catalog_modal_page_became_visible(), "Модальное окно создания каталога должно быть закрыто после нажатия кнопки 'Закрыть'"

    def test_open_choice_learning_modal(self, center_commerce_page):
        center_commerce_page.close_training_modal()
        center_commerce_page.сlick_choice_learning()
        assert center_commerce_page.choice_learning_modal_page_became_visible(), "Модальное окно создания каталога не открылось"
