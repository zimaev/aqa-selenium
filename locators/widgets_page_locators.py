from selenium.webdriver.common.by import By


class AccordionPageLocators:
    TITLE_SECTION_1 = (By.XPATH, "//div[@id='section1Heading']")
    CONTENT_SECTION_1 = (By.XPATH, "//div[@id='section1Content']")
    TITLE_SECTION_2 = (By.XPATH, "//div[@id='section2Heading']")
    CONTENT_SECTION_2 = (By.XPATH, "//div[@id='section2Content']")
    TITLE_SECTION_3 = (By.XPATH, "//div[@id='section3Heading']")
    CONTENT_SECTION_3 = (By.XPATH, "//div[@id='section3Content']")
