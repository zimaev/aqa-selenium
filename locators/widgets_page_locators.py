from selenium.webdriver.common.by import By


class AccordionPageLocators:
    TITLE_SECTION_1 = (By.XPATH, "//div[@id='section1Heading']")
    CONTENT_SECTION_1 = (By.XPATH, "//div[@id='section1Content']")
    TITLE_SECTION_2 = (By.XPATH, "//div[@id='section2Heading']")
    CONTENT_SECTION_2 = (By.XPATH, "//div[@id='section2Content']")
    TITLE_SECTION_3 = (By.XPATH, "//div[@id='section3Heading']")
    CONTENT_SECTION_3 = (By.XPATH, "//div[@id='section3Content']")


class AutocompletePageLocators:
    INPUT_MULTIPLE_COLOR = (By.XPATH, "//input[@id='autoCompleteMultipleInput']")
    VALUE_MULTIPLE_COLOR = (By.XPATH, "//div[@class='css-1rhbuit-multiValue auto-complete__multi-value']")
    DELETE_ONE_COLOR = (By.XPATH, "//div[@class='css-1rhbuit-multiValue auto-complete__multi-value']/div[2]")
    DELETE_ALL_COLOR = (By.CSS_SELECTOR, ".css-1wy0on6 .css-19bqh2r")

    INPUT_SINGLE_COLOR = (By.XPATH, "//input[@id='autoCompleteSingleInput']")
    VALUE_SINGLE_COLOR = (By.XPATH, "//div[@class='auto-complete__single-value css-1uccc91-singleValue']")


class DatePickerPageLocators:
    DATE_INPUT = (By.XPATH, "//input[@id='datePickerMonthYearInput']")
    DATE_INPUT_MONTH = (By.XPATH, "//select[@class='react-datepicker__month-select']")
    DATE_INPUT_DAY_LIST = (By.XPATH, "//div[contains(@class, 'react-datepicker__day react-datepicker__day')]")
    DATE_INPUT_YEAR = (By.XPATH, "//select[@class='react-datepicker__year-select']")

    DATE_AND_TIME_INPUT = (By.XPATH, "//input[@id='dateAndTimePickerInput']")
    DATE_AND_TIME_INPUT_MONTH = (By.XPATH, "//span[@class='react-datepicker__month-read-view--selected-month']")
    DATE_AND_TIME_INPUT_DAY_LIST = (By.XPATH, "//div[contains(@class, 'react-datepicker__day react-datepicker__day')]")
    DATE_AND_TIME_INPUT_YEAR = (By.XPATH, "//span[@class='react-datepicker__year-read-view--selected-year']")
    DATE_AND_TIME_INPUT_TIME_LIST = (By.XPATH, "//li[@class='react-datepicker__time-list-item ']")

    DATE_AND_TIME_INPUT_MONTH_LIST = (By.XPATH, "//div[@class='react-datepicker__month-option']")
    DATE_AND_TIME_INPUT_YEAR_LIST = (By.XPATH, "//div[@class='react-datepicker__year-option']")


class SliderPageLocators:
    INPUT_SLIDER = (By.XPATH, "//input[@class='range-slider range-slider--primary']")
    SLIDER_VALUE = (By.XPATH, "//input[@id='sliderValue']")


class ProgressBarPageLocators:
    BUTTON_STAR_STOP = (By.XPATH, "//button[@id='startStopButton']")
    PROGRESS_BAR = (By.XPATH, "//div[@class='progress-bar bg-info']")


class TabsLocators:
    TAB_WHAT = (By.XPATH, "//a[@id='demo-tab-what']")
    TAB_WHAT_CONTENT = (By.XPATH, "//div[@id='demo-tabpane-what']")
    TAB_ORIGIN = (By.XPATH, "//a[@id='demo-tab-origin']")
    TAB_ORIGIN_CONTENT = (By.XPATH, "//div[@id='demo-tabpane-origin']")
    TAB_USER = (By.XPATH, "//a[@id='demo-tab-use']")
    TAB_USER_CONTENT = (By.XPATH, "//div[@id='demo-tabpane-use']")
    TAB_MORE = (By.XPATH, "//a[@id='demo-tab-more']")


class ToolTipsPageLocators:
    BUTTON = (By.XPATH, "//button[@id='toolTipButton']")
    HOOVER_BUTTON = (By.XPATH, "//button[@aria-describedby='buttonToolTip']")
    INPUT_FIELD = (By.XPATH, "//input[@id='toolTipTextField']")
    HOOVER_INPUT_FIELD = (By.XPATH, "//input[@aria-describedby='textFieldToolTip']")
    CONTRARY = (By.XPATH, "//a[.='Contrary']")
    HOOVER_CONTRARY = (By.XPATH, "//a[@aria-describedby='contraryTexToolTip']")
    NUMBER = (By.XPATH, "//a[.='1.10.32']")
    NUMBER_HOVER = (By.XPATH, "//a[@aria-describedby='sectionToolTip']")
    HOVER_MSG = (By.XPATH, "//div[@class='tooltip-inner']")


class MenuPageLocators:
    MENU_LIST = (By.XPATH, "//ul[@id='nav']//li")

