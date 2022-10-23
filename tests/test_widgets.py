import time
import pytest

from pages.widgets_page import AccordionPage, AutocompletePage


class TestAccordion:

    @pytest.mark.parametrize('section, tit', [('first', 'What is Lorem Ipsum?'),
                                                ('second', 'Where does it come from?'),
                                                ('third', 'Why do we use it?')])
    def test_accordion_page(self, driver, section, tit):
        accordion_page = AccordionPage(driver, "https://demoqa.com/accordian")
        accordion_page.open()
        title, content = accordion_page.check_accordion(section)
        assert content > 0
        assert title == tit


class TestAutocomplete:

    def test_add_multy_color(self,driver):
        autocomplete_page = AutocompletePage(driver, "https://demoqa.com/auto-complete")
        autocomplete_page.open()
        input_color = autocomplete_page.fill_input_multy_color()
        output_color = autocomplete_page.check_values_multy_color()
        assert input_color == output_color

    def test_autocomplete_remove_one_color(self, driver):
        autocomplete_page = AutocompletePage(driver, "https://demoqa.com/auto-complete")
        autocomplete_page.open()
        autocomplete_page.fill_input_multy_color()
        count_before, count_after = autocomplete_page.remove_one_color()
        assert count_before > count_after

    @pytest.mark.xfail(exception=TypeError)
    def test_autocomplete_remove_all_color(self, driver):
        autocomplete_page = AutocompletePage(driver, "https://demoqa.com/auto-complete")
        autocomplete_page.open()
        autocomplete_page.fill_input_multy_color()
        count_before, count_after = autocomplete_page.remove_all_color()
        assert count_before > count_after

    def test_single_color(self, driver):
        autocomplete_page = AutocompletePage(driver, "https://demoqa.com/auto-complete")
        autocomplete_page.open()
        input_color, output_color = autocomplete_page.fill_one_color()
        assert  input_color == output_color







