from selenium.webdriver.common.by import By


class SortablePageLocators:
    TAB_LIST = (By.XPATH, "//a[@id='demo-tab-list']")
    LIST_ITEM = (By.XPATH, "//div[@class='vertical-list-container mt-4']/div")
    TAB_GRID = (By.XPATH, "//a[@id='demo-tab-grid']")
    GRID_ITEM = (By.XPATH, "//div[@class='create-grid']/div")


class SelectablePageLocators:
    TAB_LIST = (By.XPATH, "//a[@id='demo-tab-list']")
    LIST_ITEM = (By.XPATH, "//li[@class='mt-2 list-group-item list-group-item-action']")
    LIST_ITEM_ACTIVE = (By.XPATH, "//li[@class='mt-2 list-group-item active list-group-item-action']")
    TAB_GRID = (By.XPATH, "//a[@id='demo-tab-grid']")
    GRID_ITEM =(By.XPATH, "//li[@class='list-group-item list-group-item-action']")
    GRID_ITEM_ACTIVE = (By.XPATH, "//li[@class='list-group-item active list-group-item-action']")


class ResizablePageLocators:
    RESIZABLE_BOX_HANDLE = (By.XPATH,
                            "//div[@id='resizableBoxWithRestriction']/span[@class='react-resizable-handle react-resizable-handle-se']")
    RESIZABLE_BOX = (By.XPATH, "//div[@id='resizableBoxWithRestriction']")
    RESIZABLE = (By.XPATH, "//div[@id='resizable']")
    RESIZABLE_HANDLE = (By.XPATH,
                        "//div[@id='resizable']/span[@class='react-resizable-handle react-resizable-handle-se']")


class DroppablePageLocators:
    # Simple
    SIMPLE_TAB = (By.XPATH, "//a[@id='droppableExample-tab-simple']")
    SIMPLE_DRAG_ME = (By.XPATH, "//*[@class='simple-drop-container']//*[@id='draggable']")
    SIMPLE_DROP_ME = (By.XPATH, "//*[@class='simple-drop-container']//*[@id='droppable']")

    # Accept
    ACCEPT_TAB = (By.XPATH, "//a[@id='droppableExample-tab-accept']")
    ACCEPTABLE = (By.XPATH, "//*[@id='acceptDropContainer']//*[@id='acceptable']")
    NOT_ACCEPTABLE = (By.XPATH, "//*[@id='acceptDropContainer']//*[@id='notAcceptable']")
    ACCEPT_DROP_ME = (By.XPATH, "//*[@id='acceptDropContainer']//*[@id='droppable']")

    # PreventPropogation
    PREVENT_PROPOGATION_TAB = (By.XPATH, "//a[@id='droppableExample-tab-preventPropogation']")
    PREVENT_DRAG_ME = (By.XPATH, "//a[@id='droppableExample-tab-preventPropogation']")
    NOT_GREEDY_DROP_BOX_TEX = (By.XPATH, "")
    NOT_GREEDY_INNER_BOX = (By.XPATH, "")
    GREEDY_DROP_BOX_TEX = (By.XPATH, "")
    GREEDY_INNER_BOX = (By.XPATH, "")

    # RevertDraggable
    REVERT_DRAGGABLE_TAB = (By.XPATH, "//a[@id='droppableExample-tab-revertable']")
    WILL_REVERT = (By.XPATH, "//*[@id='revertableDropContainer']//*[@id='revertable']")
    NOT_REVERT = (By.XPATH, "//*[@id='revertableDropContainer']//*[@id='notRevertable']")
    REVERT_DROP_ME = (By.XPATH, "//*[@id='revertableDropContainer']//*[@id='droppable']")


