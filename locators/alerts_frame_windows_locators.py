from selenium.webdriver.common.by import By


class AlertsFrameWindowsLocators:
    NEW_TAB_BUTTON = (By.XPATH, "//button[@id='tabButton']")
    NEW_WINDOW_BUTTON = (By.XPATH, "//button[@id='windowButton']")
    NEW_MESSAGE_BUTTON = (By.XPATH, "//button[@id='messageWindowButton']")
    H1 = (By.XPATH, '//h1')
    BODY = (By.XPATH, '//body')

