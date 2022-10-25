import random
import time

from selenium.webdriver import Keys
from selenium.webdriver.support.select import Select

from generator.generator import generated_color, generated_date
from locators.widgets_page_locators import *
from pages.base_page import BasePage


class AccordionPage(BasePage):
    locators = AccordionPageLocators()

    def check_accordion(self, title_num):
        accordion = {"first":
                         {"title": self.locators.TITLE_SECTION_1,
                          "content": self.locators.CONTENT_SECTION_1
                          },
                     "second": {
                         "title": self.locators.TITLE_SECTION_2,
                         "content": self.locators.CONTENT_SECTION_2
                     },
                     "third": {"title": self.locators.TITLE_SECTION_3,
                               "content": self.locators.CONTENT_SECTION_3
                               },
                     }

        section_title = self.element_is_visible(accordion[title_num]["title"])
        section_title.click()
        content = self.element_is_visible(accordion[title_num]["content"])
        return section_title.text, len(content.text)


class AutocompletePage(BasePage):

    locators = AutocompletePageLocators()

    def fill_input_multy_color(self):
        colors = random.sample(next(generated_color()).color_name, k=random.randint(2, 4))
        for color in colors:
            input_multi = self.element_is_visible(self.locators.INPUT_MULTIPLE_COLOR)
            input_multi.send_keys(color)
            self.element_is_visible(self.locators.INPUT_MULTIPLE_COLOR).send_keys(Keys.RETURN)
        return colors

    def check_values_multy_color(self):
        color_list = self.elements_are_visible(self.locators.VALUE_MULTIPLE_COLOR)
        colors = []
        for color in color_list:
            colors.append(color.text)
        return colors

    def remove_one_color(self):
        count_value_before = len(self.elements_are_visible(self.locators.VALUE_MULTIPLE_COLOR))
        remove_button_list = self.elements_are_visible(self.locators.DELETE_ONE_COLOR)

        for value in remove_button_list:
            value.click()
            break
        count_value_after = len(self.elements_are_visible(self.locators.VALUE_MULTIPLE_COLOR))

        return count_value_before, count_value_after

    def remove_all_color(self):
        count_value_before = len(self.elements_are_visible(self.locators.VALUE_MULTIPLE_COLOR))
        self.element_is_visible(self.locators.DELETE_ALL_COLOR).click()
        count_value_after = len(self.elements_are_visible(self.locators.VALUE_MULTIPLE_COLOR))
        return count_value_before, count_value_after

    def fill_one_color(self):
        color = next(generated_color()).color_name[random.randint(1, 11)]
        self.element_is_visible(self.locators.INPUT_SINGLE_COLOR).send_keys(color)
        self.element_is_visible(self.locators.INPUT_SINGLE_COLOR).send_keys(Keys.RETURN)
        color_value = self.element_is_visible(self.locators.VALUE_SINGLE_COLOR).text
        return color, color_value


class DatePickerPage(BasePage):

    locators = DatePickerPageLocators()

    def select_date(self):
        date = next(generated_date())
        input_date = self.element_is_visible(self.locators.DATE_INPUT)
        input_date_before = input_date.get_attribute("value")
        input_date.click()
        self.select_date_by_text(self.locators.DATE_INPUT_MONTH, date.month)
        self.select_date_by_text(self.locators.DATE_INPUT_YEAR, date.year)
        self.select_day_from_list(self.locators.DATE_INPUT_DAY_LIST, date.day)
        input_date_after = input_date.get_attribute("value")
        input_date.send_keys(Keys.RETURN)
        return input_date_before, input_date_after

    def select_date_by_text(self, element, value ):
        select = Select(self.element_is_presence(element))
        select.select_by_visible_text(value)

    def select_day_from_list(self, elements, value):
        elements_list = self.elements_are_presence(elements)
        for i in elements_list:
            if i.text == value:
                i.click()
                break

    def select_date_and_time(self):
        date = next(generated_date())
        input_date = self.element_is_visible(self.locators.DATE_AND_TIME_INPUT)
        input_date_before = input_date.get_attribute("value")
        input_date.click()
        self.element_is_visible(self.locators.DATE_AND_TIME_INPUT_MONTH).click()
        self.select_day_from_list(self.locators.DATE_AND_TIME_INPUT_MONTH_LIST, date.month)

        self.element_is_visible(self.locators.DATE_AND_TIME_INPUT_YEAR).click()
        self.select_day_from_list(self.locators.DATE_AND_TIME_INPUT_YEAR_LIST, date.year)

        self.select_day_from_list(self.locators.DATE_AND_TIME_INPUT_DAY_LIST, date.day)
        self.select_day_from_list(self.locators.DATE_AND_TIME_INPUT_TIME_LIST, date.time)
        input_date_after = input_date.get_attribute("value")
        return input_date_before, input_date_after


class SliderPage(BasePage):
    locators = SliderPageLocators()

    def change_slider_value(self):
        value_before = self.element_is_visible(self.locators.SLIDER_VALUE).get_attribute('value')
        slider = self.element_is_visible(self.locators.INPUT_SLIDER)
        self.brag_and_drop_by_offset(slider, random.randint(0, 100), 0)
        value_after = self.element_is_visible(self.locators.SLIDER_VALUE).get_attribute('value')
        return value_before, value_after


class ProgressBarPage(BasePage):
    locators = ProgressBarPageLocators()

    def change_progress_bar_value(self):
        value_before = self.element_is_presence(self.locators.PROGRESS_BAR).text
        self.element_is_visible(self.locators.BUTTON_STAR_STOP).click()
        time.sleep(random.randint(2, 10))
        self.element_is_visible(self.locators.BUTTON_STAR_STOP).click()
        value_after = self.element_is_presence(self.locators.PROGRESS_BAR).text
        return value_before, value_after












