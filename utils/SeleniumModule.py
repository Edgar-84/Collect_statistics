import time

from utils.CustomExceptions import NotFoundXpathException

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


class SeleniumDriver:
    def __init__(self, hidden: bool = False):
        options = Options()

        if hidden:
            options.add_argument('--headless=new')

        options.add_argument('start-maximized')
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.__driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    @property
    def get_driver(self):
        return self.__driver

    def close_driver(self):
        self.__driver.close()
        self.__driver.quit()

    def xpath_checker(self, xpath: str, pause: int = 10) -> bool:
        """
        Get information is there xpath on the page
        """

        driver = self.__driver
        wait = WebDriverWait(driver, pause)

        try:
            wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
            result = True

        except Exception:
            result = False

        return result

    def while_not_element(self,
                          xpath: str,
                          sleep: float = 0.5,
                          kill: float = 0.5):
        """
        Wait while not xpath
        """

        wait_sleep = sleep
        start_time = time.perf_counter()

        while True:
            if self.xpath_checker(xpath=xpath):
                break
            else:
                time.sleep(wait_sleep)
                current_time = time.perf_counter()

                if current_time - start_time >= kill * 60:
                    self.close_driver()
                    raise NotFoundXpathException(f"Didn't find the XPATH: {xpath}")

    def click_xpath(self, xpath: str,
                    click: bool = True,
                    while_not_element: bool = True) -> None | WebElement:
        """
        Click on XPATH or return element
        """

        driver = self.__driver

        if while_not_element:
            self.while_not_element(xpath=xpath)

        element = driver.find_element(by=By.XPATH, value=xpath)

        if click:
            element.click()

        else:
            return element

    def get_text_xpath(self, xpath) -> str:
        """
        Get text from selected Xpath
        """

        web_element = self.click_xpath(xpath, click=False)
        result = web_element.get_attribute('textContent').strip()

        return result

    def get_elements(self, xpath: str, while_not_element: bool = True) -> list[WebElement]:
        """
        Get all elements with selected Xpath
        """

        driver = self.__driver

        if while_not_element:
            self.while_not_element(xpath)

        return driver.find_elements(by=By.XPATH, value=xpath)

    def get_text_or_null(self, xpath: str, pause: int = 1) -> list:
        """
        Get text from xpath or '' if xpath not find
        """

        if self.xpath_checker(xpath=xpath, pause=pause):
            return self.get_elements(xpath=xpath, while_not_element=False)

        return []
