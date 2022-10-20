from locators.alerts_frame_windows_locators import AlertsFrameWindowsLocators
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








