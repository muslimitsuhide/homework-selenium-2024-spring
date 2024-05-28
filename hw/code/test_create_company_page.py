import pytest
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base_case import BaseCase
from ui.locators.create_company_page_locators import CreateCompanyPageLocators

class TestCreateCompay(BaseCase):
    def test_open_catalog_modal(self, create_company_page):
        create_company_page.close_learning_modal()
        create_company_page.click_create_company_button()

        expected_url = 'https://ads.vk.com/hq/new_create/ad_plan'
        create_company_page.wait_for_redirect(expected_url)

        current_url = create_company_page.driver.current_url

        assert current_url == expected_url

    def test_site_option_displays_advertised_site_field(self, create_company_page):
        create_company_page.close_learning_modal()
        create_company_page.click_create_company_button()
        create_company_page.select_site_option()

        assert create_company_page.is_advertised_site_field_present(), "Поле 'Рекламируемый сайт' не найдено"

    def test_valid_url_site_input(self, create_company_page):
        create_company_page.close_learning_modal()
        create_company_page.click_create_company_button()
        create_company_page.select_site_option()

        valid_url = 'https://www.avito.ru/'
        create_company_page.enter_advertised_site_url(valid_url)

        assert create_company_page.fields_displayed(), "Дополнительные поля не отображаются"

    def test_required_fields(self, create_company_page):
        create_company_page.close_learning_modal()
        create_company_page.click_create_company_button()
        create_company_page.select_site_option()

        valid_url = 'https://www.avito.ru/'
        create_company_page.enter_advertised_site_url(valid_url)

        create_company_page.fill_budget_field('500')
        create_company_page.click_continue_button()

        expected_url = 'https://ads.vk.com/hq/new_create/ad_plan/new-site_conversions/ad_group/new-ad-group-form_'
        create_company_page.wait_for_redirect(expected_url)

        current_url = create_company_page.driver.current_url

        assert current_url.startswith(expected_url)

    def test_ads_required_fields(self, create_company_page):
        create_company_page.close_learning_modal()
        create_company_page.click_create_company_button()
        create_company_page.select_site_option()

        valid_url = 'https://www.avito.ru/'
        create_company_page.enter_advertised_site_url(valid_url)

        create_company_page.fill_budget_field('500')
        create_company_page.click_continue_button()

        create_company_page.select_region()
        create_company_page.click_continue_button()

    def test_cancel_button(self, create_company_page):
        create_company_page.close_learning_modal()
        create_company_page.click_create_company_button()
        create_company_page.select_site_option()

        valid_url = 'https://www.avito.ru/'
        create_company_page.enter_advertised_site_url(valid_url)

        create_company_page.fill_budget_field('500')
        create_company_page.click_continue_button()

        create_company_page.select_region()
        create_company_page.click_continue_button()
        create_company_page.click_cancel_button()

        expected_url = 'https://ads.vk.com/hq/new_create/ad_plan/new-site_conversions/ad_group/new-ad-group-form_'
        create_company_page.wait_for_redirect(expected_url)

        current_url = create_company_page.driver.current_url
        
        assert current_url.startswith(expected_url)
