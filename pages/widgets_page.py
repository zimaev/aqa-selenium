import random
import time

from selenium.webdriver import Keys

from generator.generator import generated_color
from locators.widgets_page_locators import AccordionPageLocators, AutocompletePageLocators
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




