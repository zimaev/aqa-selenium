from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from loguru import logger


class BasePage:
    def __init__(self, driver, url: str):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def element_is_visible(self, locator, timeout=30):
        try:
            return wait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
        except Exception as e:
            logger.critical(f"Ошибка видимости элемента {e}")


    def elements_are_visible(self, locator, timeout=30):
        try:
            return wait(self.driver, timeout).until(
                EC.visibility_of_all_elements_located(locator)
            )
        except Exception as e:
            print(e)

    def element_is_presence(self, locator, timeout=30):
        try:
            return wait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
        except Exception as e:
            print(e)

    def elements_are_presence(self, locator, timeout=30):
        try:
            return wait(self.driver, timeout).until(
                EC.presence_of_all_elements_located(locator)
            )
        except Exception as e:
            print(e)

    def element_is_not_visible(self, locator, timeout=30):
        try:
            return wait(self.driver, timeout).until(
                EC.invisibility_of_element_located(locator)
            )
        except Exception as e:
            print(e)

    def element_is_clickable(self, locator, timeout=30):
        try:
            return wait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator)
            )
        except Exception as e:
            print(e)

    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)



