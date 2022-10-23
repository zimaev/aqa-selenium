from locators.widgets_page_locators import AccordionPageLocators
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
