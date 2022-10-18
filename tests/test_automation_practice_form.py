import time
import pytest

from pages.form_page import FormPage


class TestFormPage:

    @pytest.mark.parametrize("gender", ["MALE_GENDER", "FEMALE_GENDER", "OTHER_GENDER"])
    @pytest.mark.parametrize("hobbies", ["SPORTS", "READING", "MUSIC"])
    def test_form(self, driver, gender, hobbies):
        form_page = FormPage(driver, "https://demoqa.com/automation-practice-form")
        form_page.open()
        form_page.fill_form_fields(student_gender=gender, student_hobbies=hobbies)
        time.sleep(3)