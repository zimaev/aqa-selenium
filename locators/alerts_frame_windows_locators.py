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


class FramesPageLocators:
    FRAME_1 = (By.XPATH, "//iframe[@id='frame1']")
    IN_FRAME1_H1 = (By.XPATH, "//h1[@id='sampleHeading']")
    FRAME_2 = (By.XPATH, "//iframe[@id='frame2']")


class NestedFramesPageLocators:
    FRAME_1 = (By.XPATH, "//iframe[@id='frame1']")
    IN_FRAME1_BODY = (By.XPATH, "//body")
    CHILD_FRAME = (By.XPATH, '//iframe[@srcdoc="<p>Child Iframe</p>"]')
    IN_C_FRAME1_BODY = (By.XPATH, "//p")

