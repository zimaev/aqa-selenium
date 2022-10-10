from pages.base_page import BasePage


def test_text_box(driver):
    page = BasePage(driver, 'https://demoqa.com/text-box')
    page.open()


