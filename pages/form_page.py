from generator.generator import generated_person, generated_file
from locators.form_page_locators import FormPageLocators
from pages.base_page import BasePage


class FormPage(BasePage):

    locators = FormPageLocators()

    def fill_form_fields(self, student_gender, student_hobbies):

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
        current_address = person_info.current_address

        # self.element_is_visible(self.locators.FIRST_NAME).send_keys(first_name)
        # self.element_is_visible(self.locators.LAST_NAME).send_keys(last_name)
        # self.element_is_visible(self.locators.USER_EMAIL).send_keys(email)
        self.element_is_visible(gender[student_gender]).click()
        self.element_is_visible(hobbies[student_hobbies]).click()
        # self.element_is_visible(self.locators.UPLOAD_PICTURE).send_keys(file_path)
        # self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
        # self.element_is_visible(self.locators.SUBMIT).click()

