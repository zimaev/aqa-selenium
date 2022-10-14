import time
import pytest
from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButton, WebTablePage


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
        time.sleep(1)











