import time

from pages.elements_page import TextBoxPage


def test_text_box(driver):
    page = TextBoxPage(driver, 'https://demoqa.com/text-box')
    page.open()
    page.fill_all_fields()
    out_full_name, out_email, out_current_address, out_permanent_address = page.check_output_form()




