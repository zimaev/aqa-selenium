from selenium.webdriver.common.by import By


class SortablePageLocators:
    TAB_LIST = (By.XPATH, "//a[@id='demo-tab-list']")
    LIST_ITEM =(By.XPATH, "//div[@class='vertical-list-container mt-4']/div")
    TAB_GRID = (By.XPATH, "//a[@id='demo-tab-grid']")
    GRID_ITEM = (By.XPATH, "//div[@class='create-grid']/div")
