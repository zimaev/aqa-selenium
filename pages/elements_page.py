from generator.generator import generated_person
from locators.elements_page_locator import TextBoxLocator, CheckBoxLocators
from pages.base_page import BasePage
import random
from loguru import logger


class TextBoxPage(BasePage):
    locators = TextBoxLocator()

    def fill_all_fields(self):
        person_info = next(generated_person())
        full_name = person_info.full_name
        email = person_info.email
        current_address = person_info.current_address
        permanent_address = person_info.permanent_address

        self.element_is_visible(self.locators.FULL_NAME).send_keys(full_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys(permanent_address)
        self.element_is_clickable(self.locators.SUBMIT).click()

        return full_name, email, current_address, permanent_address

    def check_output_form(self):
        full_name = self.element_is_presence(self.locators.CREATED_FULL_NAME).text.split(":")[1]
        email = self.element_is_presence(self.locators.CREATED_EMAIL).text.split(":")[1]
        current_address = self.element_is_presence(self.locators.CREATED_CURRENT_ADDRESS).text.split(":")[1]
        permanent_address = self.element_is_presence(self.locators.CREATED_PERMANENT_ADDRESS).text.split(":")[1]
        return full_name, email, current_address, permanent_address


class CheckBoxPage(BasePage):

    _locators = CheckBoxLocators()

    def expand_full_item_list(self):
        self.element_is_clickable(self._locators.EXPAND_ALL).click()

    def click_random_item(self):
        item_list = self.elements_are_presence(self._locators.ITEM_LIST)
        cout = 21
        while cout != 0:
            item = item_list[random.randint(1, 16)]
            if cout > 0:
                self.scroll_to_element(item)
                item.click()
                cout -= 1
            else:
                break

    def get_checked_items(self):
        checked_list = self.elements_are_presence(self._locators.CHECKED_ITEMS)
        data = []
        for box in checked_list:
            title_item = box.find_element(*self._locators.ITEM_TITLE)
            data.append(title_item.text)
        return str(data).replace(' ', '').replace('doc', '').replace('.', '').lower()

    def get_output_result(self):
        output_list = self.elements_are_presence(self._locators.OUTPUT_RESULT)
        data = []
        for item in output_list:
            data.append(item.text)
        return str(data).replace(' ', '').lower()







