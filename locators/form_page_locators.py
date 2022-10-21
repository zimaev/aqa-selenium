from selenium.webdriver.common.by import By


class FormPageLocators:
    FIRST_NAME = (By.XPATH, "//input[@id='firstName']")
    LAST_NAME = (By.XPATH, "//input[@id='lastName']")
    USER_EMAIL = (By.XPATH, "//input[@id='userEmail']")
    MALE_GENDER = (By.XPATH, "//label[contains(.,'Male')]")
    FEMALE_GENDER = (By.XPATH, "//label[contains(.,'Female')]")
    OTHER_GENDER = (By.XPATH, "//label[contains(.,'Other')]")
    MOBILE = (By.XPATH, "//input[@id='userNumber']")
    DATE_OF_BIRTH = (By.XPATH, "//input[@id='dateOfBirthInput']")
    SELECT_MONTH = (By.XPATH, "//select[@class='react-datepicker__month-select']")
    SELECT_YEAR = (By.XPATH, "//select[@class='react-datepicker__year-select']")
    SUBJECTS = (By.XPATH, "//input[@id='subjectsInput']")
    CURRENT_ADDRESS = (By.XPATH, "//textarea[@id='currentAddress']")
    HOBBIES_SPORT = (By.XPATH, "//label[@for='hobbies-checkbox-1']")
    HOBBIES_READING = (By.XPATH, "//label[@for='hobbies-checkbox-2']")
    HOBBIES_MUSIC = (By.XPATH, "//label[@for='hobbies-checkbox-3']")
    UPLOAD_PICTURE = (By.XPATH, "//input[@id='uploadPicture']")
    STATE = (By.XPATH, "//input[@id='react-select-3-input']")
    CITY = (By.XPATH, "//input[@id='react-select-4-input']")
    SUBMIT = (By.XPATH, "//button[@id='submit']")

