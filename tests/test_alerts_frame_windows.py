import time

from pages.alerts_frame_windows_page import *


class TestFrameWindowsAlerts:

    def test_new_tab(self, driver):
        new_tab_page = BrowserWindowsPage(driver, "https://demoqa.com/browser-windows")
        new_tab_page.open()
        h1 = new_tab_page.check_opened_new_tab()
        assert h1 == "This is a sample page"

    def test_new_window(self, driver):
        new_tab_page = BrowserWindowsPage(driver, "https://demoqa.com/browser-windows")
        new_tab_page.open()
        h1 = new_tab_page.check_opened_new_window()
        assert h1 == "This is a sample page"


class TestAlertPage:

    def test_see_alert(self, driver):
        alert_page = AlertPage(driver, "https://demoqa.com/alerts")
        alert_page.open()
        msg = alert_page.click_simple_alert()
        assert msg == "You clicked a button"

    def test_see_alert_after_5_sec(self, driver):
        alert_page = AlertPage(driver, "https://demoqa.com/alerts")
        alert_page.open()
        msg = alert_page.click_alert_after_5_sec()
        assert msg == "This alert appeared after 5 seconds"

    def test_click_confirm_button(self, driver):
        alert_page = AlertPage(driver, "https://demoqa.com/alerts")
        alert_page.open()
        message = alert_page.click_confirm_button()
        assert message == "You selected Ok"

    def test_click_prompt_button(self, driver):
        alert_page = AlertPage(driver, "https://demoqa.com/alerts")
        alert_page.open()
        message = alert_page.click_prompt_button()
        assert message == "You entered Hello world"


class TestFrameTable:
    def test_frames(self, driver):
        alert_page = FramesPage(driver, "https://demoqa.com/frames")
        alert_page.open()
        text, width, height = alert_page.check_first_frame()
        assert text == 'This is a sample page'
        assert width == "500px"
        assert height == "350px"


class TestNestedFrameTable:
    def test_nested_frames(self, driver):
        nested_frame_page = NestedFramesPage(driver, "https://demoqa.com/nestedframes")
        nested_frame_page.open()
        p_text, c_text = nested_frame_page.check_parent_frame()
        assert p_text == "Parent frame"
        assert c_text == "Child Iframe"


class TestModalDialogs:

    def test_modal_dialogs(self, driver):
        modal_dialogs = ModalDialogsPage(driver, "https://demoqa.com/modal-dialogs")
        modal_dialogs.open()
        text, title = modal_dialogs.check_small_modal_dialogs()
        assert title == "Small Modal"
        assert text == "This is a small modal. It has very less content"





