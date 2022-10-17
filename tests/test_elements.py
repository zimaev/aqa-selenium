import time
from unicodedata import name
import pytest
from pages.elements_page import *
from selenium.webdriver.common.action_chains import ActionChains


def test_text_box(driver):
    page = TextBoxPage(driver, 'https://demoqa.com/text-box')
    page.open()
    full_name, email, current_address, permanent_address = page.fill_all_fields()
    out_full_name, out_email, out_current_address, out_permanent_address = page.check_output_form()
    assert full_name == out_full_name, "Введенное имя не соответствует отображаемомому в итоговой форме"
    assert email == out_email, "Введенный email не соответствует отображаемомому в итоговой форме"
    assert current_address == out_current_address, "Введенный текущий адрес не соответствует отображаемомому в итоговой форме"
    assert permanent_address == out_permanent_address, "Введенный постоянный адрес не соответствует отображаемомому в итоговой форме"


def test_checkbox(driver):
    checkbox_page = CheckBoxPage(driver, 'https://demoqa.com/checkbox')
    checkbox_page.open()
    checkbox_page.expand_full_item_list()
    checkbox_page.click_random_item()
    input_chekbox = checkbox_page.get_checked_items()
    output_chekbox = checkbox_page.get_output_result()
    assert input_chekbox == output_chekbox, "Установленные чекбоксы не равны отображаемым"


@pytest.mark.parametrize("radio", ['Yes', 'Impressive', "No"])
def test_radio_button(driver, radio):
    radio_button = RadioButton(driver, 'https://demoqa.com/radio-button')
    radio_button.open()
    radio_button.click_radio_button(radio)
    get = radio_button.get_selected_text()
    if radio in ['Yes', 'Impressive']:
        assert radio == get
    else:
        pytest.xfail(reason="Негативный тест. Чекбокс заблокирован")


class TestWebTable:

    def test_web_table_add_person(self, driver):
        web_table = WebTablePage(driver, 'https://demoqa.com/webtables')
        web_table.open()
        new_person = web_table.add_new_person()
        table = web_table.check_added_new_person()
        assert new_person in table

    @pytest.mark.parametrize("field", [0, 1, 4])
    def test_web_table_search_person(self, driver, field):
        #TODO Переделать праметризацию для корректного отображения в тестах.
        web_table = WebTablePage(driver, 'https://demoqa.com/webtables')
        web_table.open()
        new_person = web_table.add_new_person()[field]
        web_table.search_person(new_person)
        search_table = web_table.check_search_person()
        assert new_person in search_table , "Введенное знание в поле поиста не присутсвует в таблице"

    def test_web_table_edit_person_info(self, driver):
        web_table = WebTablePage(driver, 'https://demoqa.com/webtables')
        web_table.open()
        new_person = web_table.add_new_person()[0]
        web_table.search_person(new_person)
        new_age = web_table.edit_person_info()
        search_table = web_table.check_search_person()
        assert new_age in search_table , "значение в анкете не изменено"

    def test_web_table_delete_person_info(self, driver):
        web_table = WebTablePage(driver, 'https://demoqa.com/webtables')
        web_table.open()
        new_person = web_table.add_new_person()[0]
        web_table.search_person(new_person)
        web_table.delete_person()
        assert web_table.check_empty_tabel == "No rows found"

    @pytest.mark.parametrize('count', ['5', '10', '20', '25', '50', '100'])
    def test_web_table_change_count_row(self, driver, count):
        web_table = WebTablePage(driver, 'https://demoqa.com/webtables')
        web_table.open()
        web_table.change_count_row(count)
        row = web_table.check_count_row_in_table()
        assert row == int(count)


class TestButton:

    def test_double_click(self, driver):
        button_pages = ButtonPage(driver, "https://demoqa.com/buttons")
        button_pages.open()
        msg = button_pages.dbl_click()
        assert msg == 'You have done a double click'

    def test_right_click(self, driver):
        button_pages = ButtonPage(driver, "https://demoqa.com/buttons")
        button_pages.open()
        msg = button_pages.rgt_click()
        assert msg == 'You have done a right click'

    def test_regular_click(self, driver):
        button_pages = ButtonPage(driver, "https://demoqa.com/buttons")
        button_pages.open()
        msg = button_pages.regular_click()
        assert msg == 'You have done a dynamic click'


class TestLink:

    def test_link(self, driver):
        link_page = LinksPage(driver, 'https://demoqa.com/links')
        link_page.open()
        target_url, actual_url = link_page.check_new_tab_simple_link()
        print(target_url, actual_url)
        assert target_url == actual_url


    def test_broken_link(self, driver):
        #TODO пересмотреть реализацию негативных тестов. доделать остальные
        link_page = LinksPage(driver, 'https://demoqa.com/links')
        response_code = link_page.check_bocken_link("https://demoqa.com/bad-request")
        assert response_code == 400


class TestUploadDownload:

    def test_upload_file(self, driver):

        upload_download = UploadDownloadPage(driver, 'https://demoqa.com/upload-download')
        upload_download.open()
        name_file, path_in_site = upload_download.upload_file()
        assert name_file in path_in_site
















