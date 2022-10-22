from selenium.webdriver.common.by import By


class AlertsFrameWindowsLocators:
    NEW_TAB_BUTTON = (By.XPATH, "//button[@id='tabButton']")
    NEW_WINDOW_BUTTON = (By.XPATH, "//button[@id='windowButton']")
    NEW_MESSAGE_BUTTON = (By.XPATH, "//button[@id='messageWindowButton']")
    H1 = (By.XPATH, '//h1')
    BODY = (By.XPATH, '//body')


class AlertsPageLocators:
    REGULAR_ALERT_BUTTON = (By.XPATH, "//button[@id='alertButton']")
    TIME_ALERT_BUTTON = (By.XPATH, "//button[@id='timerAlertButton']")
    CONFIRM_BUTTON = (By.XPATH, "//button[@id='confirmButton']")
    PROMT_BUTTON = (By.XPATH, "//button[@id='promtButton']")
    PROMT_TEXT = (By.XPATH, "//span[@id='promptResult']")
    TEXT_SUCCESS = (By.XPATH, "//span[@id='confirmResult']")

