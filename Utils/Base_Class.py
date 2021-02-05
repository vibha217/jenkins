from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Base_Class:
    @staticmethod
    def open_browser():

        driver = webdriver.Chrome(executable_path="../Resources/Driver/chromedriver.exe")
        driver.get("http://automationpractice.com/index.php")
        return driver

    def getByType(locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "classname":
            return By.CLASS_NAME
        elif locatorType == "linktext":
            return By.LINK_TEXT

        else:
            print("LocatorType " + locatorType + " not supported")
            return False

    def getElement(driver, locator, locatorType):
        element = None
        try:
            byType = Base_Class.getByType(locatorType)
            element = driver.find_element(byType, locator)
            print("Element Found")
        except:
            print("Element not found")
        return element

    def action_click(ele):
        ele.click()

    def action_sendkeys(ele,data):
          ele.action_sendkeys(data)

    def action_dropdown(ele,visible_text):
         act = Select(ele)
         act.Select_By_Visible_text(visible_text)

    def waitForElement(driver, locatorValue, locatorType="id", timeout=10):
        element = None
        try:
            byType = Base_Class.getByType(locatorType)
            print("Waiting for maximum :: " + str(timeout) +
                  " :: seconds for element to be clickable")
            wait = WebDriverWait(driver, timeout)
            element = wait.until(EC.element_to_be_clickable((byType, locatorValue)))
            print("Element appeared on the web page")
        except:
            print("Element not appeared on the web page")
        return element


#obj = Base_Class()

#d = obj.open_browser()
