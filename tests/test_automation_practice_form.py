import time
import pytest
from utils.csv_reader import read_test_data_from_csv
from pages.form_page import FormPage


class TestFormPage:

    @pytest.mark.parametrize("gender", ["MALE_GENDER", "FEMALE_GENDER", "OTHER_GENDER"])
    @pytest.mark.parametrize("hobbies", ["SPORTS", "READING", "MUSIC"])
    @pytest.mark.parametrize("subjects", ["Biology", "Arts", "Civics"])
    @pytest.mark.parametrize("state, city", read_test_data_from_csv())
    def test_form(self, driver, gender, hobbies, state, city, subjects):
        form_page = FormPage(driver, "https://demoqa.com/automation-practice-form")
        form_page.open()
        input_person =form_page.fill_form_fields(student_gender=gender, student_hobbies=hobbies,
                                   state=state, city=city,
                                   subjects=subjects)
        output_table = form_page.form_result()

        assert output_table[0] == input_person.first_name + " " + input_person.last_name
        assert input_person.email == output_table[1]
        assert input_person.mobile[:-3] == output_table[3]
        assert subjects == output_table[5]


