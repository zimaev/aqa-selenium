import os
import time

from selenium.webdriver import Keys
from selenium.webdriver.support.select import Select

from generator.generator import generated_person, generated_file
from locators.form_page_locators import FormPageLocators
from pages.base_page import BasePage


class FormPage(BasePage):

    locators = FormPageLocators()

    def fill_form_fields(self, student_gender, student_hobbies, state, city, subjects):

        gender = {
            'MALE_GENDER': self.locators.MALE_GENDER,
            'FEMALE_GENDER': self.locators.FEMALE_GENDER,
            'OTHER_GENDER': self.locators.OTHER_GENDER,
        }

        hobbies = {
            'SPORTS': self.locators.HOBBIES_SPORT,
            'READING': self.locators.HOBBIES_READING,
            'MUSIC': self.locators.HOBBIES_MUSIC,
        }

        person_info = next(generated_person())
        file_path = generated_file()
        first_name = person_info.first_name
        last_name = person_info.last_name
        email = person_info.email
        mobile = person_info.mobile
        current_address = person_info.current_address
        birdh_date = person_info.birth_date

        self.driver.execute_script("document.getElementsByTagName('footer')[0].remove();")
        self.driver.execute_script("document.getElementById('close-fixedban').remove();")
        self.element_is_visible(self.locators.FIRST_NAME).send_keys(first_name)
        self.element_is_visible(self.locators.LAST_NAME).send_keys(last_name)
        self.element_is_visible(self.locators.USER_EMAIL).send_keys(email)
        self.element_is_visible(self.locators.MOBILE).send_keys(mobile)
        self.element_is_visible(self.locators.DATE_OF_BIRTH).click()
        self.element_is_visible(self.locators.DATE_OF_BIRTH).send_keys(Keys.CONTROL + "a")
        self.element_is_visible(self.locators.DATE_OF_BIRTH).send_keys(birdh_date)
        self.element_is_visible(self.locators.DATE_OF_BIRTH).click()
        self.element_is_visible(gender[student_gender]).click()
        self.element_is_visible(self.locators.SUBJECTS).send_keys(subjects)
        self.element_is_visible(self.locators.SUBJECTS).send_keys(Keys.RETURN)
        self.element_is_visible(hobbies[student_hobbies]).click()
        self.element_is_visible(self.locators.UPLOAD_PICTURE).send_keys(file_path)
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
        input_state = self.element_is_visible(self.locators.STATE)
        input_state.send_keys(state)
        input_state.send_keys(Keys.RETURN)
        os.remove(file_path)
        input_city = self.element_is_visible(self.locators.CITY)
        input_city.send_keys(city)
        input_city.send_keys(Keys.RETURN)
        self.element_is_presence(self.locators.SUBMIT).click()

