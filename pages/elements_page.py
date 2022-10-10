from locators.elements_page_locator import TextBoxLocator
from pages.base_page import BasePage


class TextBoxPage(BasePage):
    locators = TextBoxLocator()

    def fill_all_fields(self):
        self.element_is_visible(self.locators.FULL_NAME).send_keys("Anton")
        self.element_is_visible(self.locators.EMAIL).send_keys("Anton@mail.df")
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys("Antonova st")
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys("Izmailova st")
        self.element_is_clickable(self.locators.SUBMIT).click()

    def check_output_form(self):
        full_name = self.element_is_presence(self.locators.CREATED_FULL_NAME).text.split(":")[0]
        email = self.element_is_presence(self.locators.EMAIL).text.split(":")[0]
        current_address = self.element_is_presence(self.locators.CREATED_CURRENT_ADDRESS).text.split(":")[0]
        permanent_address = self.element_is_presence(self.locators.CREATED_PERMANENT_ADDRESS).text.split(":")[0]
        return full_name, email, current_address, permanent_address
