from selenium.webdriver.common.by import By


class AccordionPageLocators:
    TITLE_SECTION_1 = (By.XPATH, "//div[@id='section1Heading']")
    CONTENT_SECTION_1 = (By.XPATH, "//div[@id='section1Content']")
    TITLE_SECTION_2 = (By.XPATH, "//div[@id='section2Heading']")
    CONTENT_SECTION_2 = (By.XPATH, "//div[@id='section2Content']")
    TITLE_SECTION_3 = (By.XPATH, "//div[@id='section3Heading']")
    CONTENT_SECTION_3 = (By.XPATH, "//div[@id='section3Content']")


class AutocompletePageLocators:
    INPUT_MULTIPLE_COLOR = (By.XPATH, "//input[@id='autoCompleteMultipleInput']")
    VALUE_MULTIPLE_COLOR = (By.XPATH, "//div[@class='css-1rhbuit-multiValue auto-complete__multi-value']")
    DELETE_ONE_COLOR = (By.XPATH, "//div[@class='css-1rhbuit-multiValue auto-complete__multi-value']/div[2]")
    DELETE_ALL_COLOR = (By.CSS_SELECTOR, ".css-1wy0on6 .css-19bqh2r")

    INPUT_SINGLE_COLOR = (By.XPATH, "//input[@id='autoCompleteSingleInput']")
    VALUE_SINGLE_COLOR = (By.XPATH, "//div[@class='auto-complete__single-value css-1uccc91-singleValue']")
