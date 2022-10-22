import time
from locators.alerts_frame_windows_locators import *
from pages.base_page import BasePage


class BrowserWindowsPage(BasePage):

    locators = AlertsFrameWindowsLocators()

    def check_opened_new_tab(self):
        self.element_is_clickable(self.locators.NEW_TAB_BUTTON).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        return self.element_is_visible(self.locators.H1).text

    def check_opened_new_window(self):
        self.element_is_clickable(self.locators.NEW_WINDOW_BUTTON).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        return self.element_is_visible(self.locators.H1).text


class AlertPage(BasePage):
    locators = AlertsPageLocators()

    def click_simple_alert(self):
        self.element_is_visible(self.locators.REGULAR_ALERT_BUTTON).click()
        alert_msg = self.driver.switch_to.alert
        return alert_msg.text

    def click_alert_after_5_sec(self):
        self.element_is_visible(self.locators.TIME_ALERT_BUTTON).click()
        time.sleep(6)
        alert_msg = self.driver.switch_to.alert
        return alert_msg.text

    def click_confirm_button(self):
        self.element_is_visible(self.locators.CONFIRM_BUTTON).click()
        alt = self.driver.switch_to.alert
        alt.accept()
        msg_text = self.element_is_presence(self.locators.TEXT_SUCCESS).text
        return msg_text

    def click_prompt_button(self):
        self.element_is_visible(self.locators.PROMT_BUTTON).click()
        prmt = self.driver.switch_to.alert
        prmt.send_keys("Hello world")
        prmt.accept()
        msg = self.element_is_visible(self.locators.PROMT_TEXT).text
        return msg


class FramesPage(BasePage):
    locators = FramesPageLocators()

    def check_first_frame(self):
        frame = self.element_is_presence(self.locators.FRAME_1)
        width = frame.get_attribute('width')
        height = frame.get_attribute('height')
        self.driver.switch_to.frame(frame)

        text = self.element_is_presence(self.locators.IN_FRAME1_H1).text
        return text, width, height


class NestedFramesPage(BasePage):
    locators = NestedFramesPageLocators()

    def check_parent_frame(self):
        p_frame = self.element_is_presence(self.locators.FRAME_1)
        self.driver.switch_to.frame(p_frame)
        p_text = self.element_is_presence(self.locators.IN_FRAME1_BODY).text

        c_frame = self.element_is_presence(self.locators.CHILD_FRAME)
        self.driver.switch_to.frame(c_frame)
        c_text = self.element_is_presence(self.locators.IN_C_FRAME1_BODY).text

        return p_text, c_text
















