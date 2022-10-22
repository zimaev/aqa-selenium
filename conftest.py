import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def driver():
    chrome_options = Options()
    chrome_options.set_capability('unhandledPromptBehavior', 'accept')
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    driver.maximize_window()
    yield driver
    driver.close()
    driver.quit()


