import time
from pages.elements_page import TextBoxPage, CheckBoxPage


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
    time.sleep(7)






