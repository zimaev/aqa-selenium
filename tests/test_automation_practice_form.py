import time
import pytest

from pages.form_page import FormPage


class TestFormPage:

    @pytest.mark.parametrize("gender", ["MALE_GENDER", "FEMALE_GENDER", "OTHER_GENDER"])
    @pytest.mark.parametrize("hobbies", ["SPORTS", "READING", "MUSIC"])
    @pytest.mark.parametrize("subjects", ["Biology", "Arts", "Civics"])
    @pytest.mark.parametrize("state, city", [('NCR', 'Delhi'), ('NCR', 'Gurgaon'), ('NCR', 'Noida')])
    def test_form(self, driver, gender, hobbies, state, city, subjects):
        form_page = FormPage(driver, "https://demoqa.com/automation-practice-form")
        form_page.open()
        form_page.fill_form_fields(student_gender=gender, student_hobbies=hobbies,
                                   state=state, city=city, subjects=subjects)
        time.sleep(3)
