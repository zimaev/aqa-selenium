import time

from pages.alerts_frame_windows_page import BrowserWindowsPage


class TestFrameWindowsAlerts:

    def test_new_tab(self, driver):
        new_tab_page = BrowserWindowsPage(driver, "https://demoqa.com/browser-windows")
        new_tab_page.open()
        h1 = new_tab_page.check_opened_new_tab()
        assert h1 == "This is a sample page"
        time.sleep(5)

    def test_new_window(self, driver):
        new_tab_page = BrowserWindowsPage(driver, "https://demoqa.com/browser-windows")
        new_tab_page.open()
        h1 = new_tab_page.check_opened_new_window()
        assert h1 == "This is a sample page"
        time.sleep(5)
