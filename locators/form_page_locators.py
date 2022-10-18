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
    SUBJECTS = (By.XPATH, "//div[@id='subjectsContainer']")
    CURRENT_ADDRESS = (By.XPATH, "//textarea[@id='currentAddress']")
    HOBBIES_SPORT = (By.XPATH, "//label[@for='hobbies-checkbox-1']")
    HOBBIES_READING = (By.XPATH, "//label[@for='hobbies-checkbox-2']")
    HOBBIES_MUSIC = (By.XPATH, "//label[@for='hobbies-checkbox-3']")
    UPLOAD_PICTURE = (By.XPATH, "//input[@id='uploadPicture']")
    STATE = (By.XPATH, "//div[@id='state']")
    CITY = (By.XPATH, "//div[@id='city']")
    SUBMIT = (By.XPATH, "//button[@id='submit']")
