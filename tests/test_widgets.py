import time
import pytest

from pages.widgets_page import AccordionPage


class TestAccordion:

    @pytest.mark.parametrize('section, tit', [('first', 'What is Lorem Ipsum?'),
                                                ('second', 'Where does it come from?'),
                                                ('third','Why do we use it?')])
    def test_accordion_page(self, driver, section, tit):
        accordion_page = AccordionPage(driver, "https://demoqa.com/accordian")
        accordion_page.open()
        title, content = accordion_page.check_accordion(section)
        assert content > 0
        assert title == tit
