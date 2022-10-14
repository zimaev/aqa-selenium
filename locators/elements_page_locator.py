from selenium.webdriver.common.by import By


class TextBoxLocator:
    # поля формы
    FULL_NAME = (By.XPATH, "//input[@id='userName']")
    EMAIL = (By.XPATH, "//input[@id='userEmail']")
    CURRENT_ADDRESS = (By.XPATH, "//textarea[@id='currentAddress']")
    PERMANENT_ADDRESS = (By.XPATH, "//textarea[@id='permanentAddress']")
    SUBMIT = (By.XPATH, "//button[@id='submit']")

    # созданная форма
    CREATED_FULL_NAME = (By.XPATH, "//p[@id='name']")
    CREATED_EMAIL = (By.XPATH, "//p[@id='email']")
    CREATED_CURRENT_ADDRESS = (By.XPATH, "//p[@id='currentAddress']")
    CREATED_PERMANENT_ADDRESS = (By.XPATH, "//p[@id='permanentAddress']")


class CheckBoxLocators:
    EXPAND_ALL = (By.XPATH, "//button[@title='Expand all']")
    ITEM_LIST = (By.XPATH, "//span[@class='rct-title']")
    CHECKED_ITEMS = (By.XPATH, "//*[@class='rct-icon rct-icon-check']")
    ITEM_TITLE = (By.XPATH, ".//ancestor::span[@class='rct-text']")
    OUTPUT_RESULT = (By.XPATH, "//span[@class='text-success']")


class RadioButtonLocators:
    YES_RADIO = (By.XPATH, "//input[@id='yesRadio']")
    IMPRESSIVE_RADIO = (By.XPATH, "//input[@id='impressiveRadio']")
    RADIO = (By.XPATH, "//label[contains(text(),'Yes')]")
    SELECTED_RADIO = (By.XPATH, "//span[@class='text-success']")


class WebTablePageLocators:
    #add form
    ADD_BUTTON = (By.XPATH, "//button[@id='addNewRecordButton']")
    FIRST_NAME_FIELD = (By.XPATH, "//input[@id='firstName']")
    LAST_NAME_FIELD = (By.XPATH, "//input[@id='lastName']")
    EMAIL_FIELD = (By.XPATH, "//input[@id='userEmail']")
    AGE_FIELD = (By.XPATH, "//input[@id='age']")
    SALARY_FIELD = (By.XPATH, "//input[@id='salary']")
    DEPARTMENT_FIELD = (By.XPATH, "//input[@id='department']")
    SUBMIT = (By.XPATH, "//button[@id='submit']")

    #tables
    FULL_PEOPLE_LIST = (By.XPATH, "//div[@class='rt-tr-group']")









