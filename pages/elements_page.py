import os
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from generator.generator import generated_file, generated_person
from locators.elements_page_locator import *
from pages.base_page import BasePage
import random
from selenium.webdriver.common.action_chains import ActionChains
import requests


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
        count = 21
        while count != 0:
            item = item_list[random.randint(1, 16)]
            if count > 0:
                self.scroll_to_element(item)
                item.click()
                count -= 1
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


class RadioButton(BasePage):
    _locators = RadioButtonLocators()

    def click_radio_button(self, btn):
        self.element_is_presence((By.XPATH, f"//label[contains(text(),'{btn}')]")).click()

    def get_selected_text(self):
        return self.element_is_presence(self._locators.SELECTED_RADIO).text


class WebTablePage(BasePage):
    locators = WebTablePageLocators()

    def add_new_person(self):
        count = 1
        while count != 0:
            person_info = next(generated_person())
            first_name = person_info.first_name
            last_name = person_info.last_name
            email = person_info.email
            age = person_info.age
            salary = person_info.salary
            department = person_info.department

            self.element_is_visible(self.locators.ADD_BUTTON).click()
            self.element_is_visible(self.locators.FIRST_NAME_FIELD).send_keys(first_name)
            self.element_is_visible(self.locators.LAST_NAME_FIELD).send_keys(last_name)
            self.element_is_visible(self.locators.EMAIL_FIELD).send_keys(email)
            self.element_is_visible(self.locators.AGE_FIELD).send_keys(age)
            self.element_is_visible(self.locators.SALARY_FIELD).send_keys(salary)
            self.element_is_visible(self.locators.DEPARTMENT_FIELD).send_keys(department)
            self.element_is_clickable(self.locators.SUBMIT).click()
            count -= 1
            return [first_name, last_name, str(age), email, str(salary), department]

    def check_added_new_person(self):
        person_list = self.elements_are_presence(self.locators.FULL_PEOPLE_LIST)
        data = []
        for i in person_list:
            data.append(i.text.splitlines())
        return data

    def search_person(self, keyword):
        self.element_is_visible(self.locators.SEARCH_FIELD).click()
        self.element_is_visible(self.locators.SEARCH_FIELD).send_keys(keyword)

    def check_search_person(self):
        delete_btn = self.element_is_visible(self.locators.DELETE_BUTTON)
        row = delete_btn.find_element(*self.locators.ROW_PARENT)
        return row.text.splitlines()

    def edit_person_info(self):
        person_info = next(generated_person())
        age = person_info.age
        self.element_is_visible(self.locators.EDIT_BUTTON).click()
        self.element_is_visible(self.locators.AGE_FIELD).clear()
        self.element_is_visible(self.locators.AGE_FIELD).send_keys(age)
        self.element_is_clickable(self.locators.SUBMIT).click()
        return str(age)

    def delete_person(self):
        self.element_is_visible(self.locators.DELETE_BUTTON).click()

    @property
    def check_empty_tabel(self):
        return self.element_is_visible(self.locators.NO_ROWS_MESSAGE).text

    def change_count_row(self, count):
        self.scroll_to_element(self.element_is_visible(self.locators.SELECT))
        select = Select(self.driver.find_element(*self.locators.SELECT))
        select.select_by_value(count)

    def check_count_row_in_table(self):
        count = self.elements_are_presence(self.locators.ROW)
        return len(count)


class ButtonPage(BasePage):

    locators = ButtonPageLocators()

    def dbl_click(self):
        self.double_click(self.element_is_clickable(self.locators.DOUBLE_CLICK_BUTTON))
        msg = self.element_is_visible(self.locators.DOUBLE_CLICK_MESSAGE)
        return msg.text

    def rgt_click(self):
        self.right_click(self.element_is_clickable(self.locators.RIGHT_CLICK_BUTTON))
        msg = self.element_is_visible(self.locators.RIGHT_CLICK_MESSAGE)
        return msg.text

    def regular_click(self):
        actions = ActionChains(self.driver)
        actions.click(self.element_is_clickable(self.locators.REGULAR_CLICK_BUTTON)).perform()
        msg = self.element_is_visible(self.locators.REGULAR_CLICK_MESSAGE)
        return msg.text


class LinksPage(BasePage):

    locators = LinksPageLocators()

    def check_new_tab_simple_link(self):
        simple_link = self.element_is_visible(self.locators.SIMPLE_LINK)
        link_from_href = simple_link.get_attribute('href')
        response = requests.get(link_from_href)
        if response.status_code == 200:
            simple_link.click()
            self.driver.switch_to.window(self.driver.window_handles[1])
            new_tab_url = self.driver.current_url
            return link_from_href, new_tab_url
        else:
            return response.status_code

    def check_bocken_link(self, url):
        respone = requests.get(url)
        if respone.status_code == 200:
            self.element_is_presence(self.locators.BAD_LINK).click()
        else:
            return respone.status_code


class UploadDownloadPage(BasePage):

    locators = UploadDownloadPageLocators()

    def upload_file(self):
        path = generated_file()
        self.element_is_presence(self.locators.UPLOAD_FIELD).send_keys(path)
        os.remove(path)
        site_path = self.element_is_visible(self.locators.UPLOADED_FILE_PATH).text
        return os.path.basename(path), os.path.basename(site_path)

    def download_file(self):
        link = self.element_is_presence(self.locators.DOWNLOAD_BUTTON).get_attribute('href')


class DynamicPropertiesPage(BasePage):

    locators = DynamicPropertiesPageLocators()

    def check_changed_color(self):
        colol_button = self.element_is_presence(self.locators.COLOR_CHANGE_BTN)
        color_before = colol_button.value_of_css_property('color')
        time.sleep(6)
        color_after = colol_button.value_of_css_property('color')
        return color_before, color_after

    def check_visible_button(self):
        return self.element_is_visible(self.locators.VISIBLE_AFTER_FIVE_SEC_BTN, timeout=1)

    def check_clickable_button(self):
        return self.element_is_clickable(self.locators.ENABLE_AFTER_FIVE_SEC_BTN, timeout=1)






        

