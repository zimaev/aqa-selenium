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
    SEARCH_FIELD = (By.XPATH, "//input[@id='searchBox']")
    DELETE_BUTTON = (By.XPATH, "//span[@title='Delete']")
    ROW_PARENT = (By.XPATH, ".//ancestor::div[@class='rt-tr-group']")
    EDIT_BUTTON = (By.XPATH, "//span[@title='Edit']")
    NO_ROWS_MESSAGE = (By.XPATH, "//div[@class='rt-noData']")
    ROW = (By.XPATH, "//div[@class='rt-tr-group']")
    SELECT = (By.XPATH, '//select[@aria-label="rows per page"]')


class ButtonPageLocators:
    DOUBLE_CLICK_BUTTON = (By.XPATH, "//button[@id='doubleClickBtn']")
    RIGHT_CLICK_BUTTON = (By.XPATH, "//button[@id='rightClickBtn']")
    REGULAR_CLICK_BUTTON = (By.XPATH, "//button[text()='Click Me']")

    DOUBLE_CLICK_MESSAGE= (By.XPATH, "//p[@id='doubleClickMessage']")
    RIGHT_CLICK_MESSAGE = (By.XPATH, "//p[@id='rightClickMessage']")
    REGULAR_CLICK_MESSAGE = (By.XPATH, "//p[@id='dynamicClickMessage']")


class LinksPageLocators:
    SIMPLE_LINK = (By.XPATH, "//a[@id='simpleLink']")
    BAD_LINK = (By.XPATH, "//a[@id='bad-request']")


class UploadDownloadPageLocators:
    UPLOAD_FIELD = (By.XPATH, '//input[@id="uploadFile"]')
    UPLOADED_FILE_PATH = (By.XPATH, "//p[@id='uploadedFilePath']")
    DOWNLOAD_BUTTON = (By.XPATH, "//a[@id='downloadButton']")

class DynamicPropertiesPageLocators:
    COLOR_CHANGE_BTN = (By.XPATH, "//button[@id='colorChange']")
    VISIBLE_AFTER_FIVE_SEC_BTN = (By.XPATH, "//button[@id='visibleAfter']")
    ENABLE_AFTER_FIVE_SEC_BTN = (By.XPATH, "//button[@id='enableAfter']")




