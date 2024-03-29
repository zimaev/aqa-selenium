import time
import pytest

from pages.widgets_page import AccordionPage, AutocompletePage, DatePickerPage, SliderPage, ProgressBarPage, TabsPage, \
    ToolTipsPage, MenuPage


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

    def test_add_multy_color(self, driver):
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
        assert input_color == output_color


class TestDatePicker:

    def test_change_data(self, driver):
        date_piker_page = DatePickerPage(driver, "https://demoqa.com/date-picker")
        date_piker_page.open()
        date_before, date_after = date_piker_page.select_date()
        assert date_before != date_after

    def test_change_data_and_time(self, driver):
        date_piker_page = DatePickerPage(driver, "https://demoqa.com/date-picker")
        date_piker_page.open()
        date_before, date_after = date_piker_page.select_date_and_time()
        assert date_before != date_after


class TestSliderPage:
    def test_slider(self, driver):
        slider_page = SliderPage(driver, "https://demoqa.com/slider")
        slider_page.open()
        value_after, value_before = slider_page.change_slider_value()
        assert value_after != value_before


class TestProgressBarPage:
    def test_progress_bar(self, driver):
        progress_bar_page = ProgressBarPage(driver, "https://demoqa.com/progress-bar")
        progress_bar_page.open()
        before, after = progress_bar_page.change_progress_bar_value()
        print(before, after)
        assert before != after


class TestTabsPage:
    @pytest.mark.parametrize("tab, len", [('What', 574), ('Origin', 1059), ('Use', 613)])
    def test_change_tabs(self, driver, tab, len):
        tabs_page = TabsPage(driver, "https://demoqa.com/tabs")
        tabs_page.open()
        title, len_content = tabs_page.check_tabs(tab)
        assert title == tab
        assert len_content == len


class TestToolTips:

    def test_tool_tips(self, driver):
        tool_tips_page = ToolTipsPage(driver, 'https://demoqa.com/tool-tips')
        tool_tips_page.open()
        tool_tips_button, tool_tips_input, tool_tips_contrary, tool_tips_number = tool_tips_page.check_tool_tips()
        assert tool_tips_button == "You hovered over the Button"
        assert tool_tips_input == 'You hovered over the text field'
        assert tool_tips_contrary == 'You hovered over the Contrary'
        assert tool_tips_number == "You hovered over the 1.10.32"


class TestMenu:
    def test_menu(self, driver):
        menu_page = MenuPage(driver, "https://demoqa.com/menu")
        menu_page.open()
        menu = menu_page.check_nemu()
        assert menu == ['Main Item 1', 'Main Item 2\nSub Item\nSub Item\nSUB SUB LIST »', 'Sub Item', 'Sub Item',
                        'SUB SUB LIST »\nSub Sub Item 1\nSub Sub Item 2',
                        'Sub Sub Item 1', 'Sub Sub Item 2', 'Main Item 3']
