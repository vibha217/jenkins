import pytest

from selenium import webdriver


class Driver:
    driver = None

    @staticmethod
    def open_browser(browser):

        if browser.lower() == "chrome":
            driver = webdriver.Chrome(
                executable_path="../Resources/Driver/chromedriver.exe")
        elif browser.lower() == "firefox":
            driver = webdriver.Firefox(
                executable_path="../Resources/Driver/geckodriver.exe")
        else:
            print("Browser not supported. Suggested values are [Chrome,Firefox]")
        return driver

    @staticmethod
    def close_browser(driver):
        driver.close()
        driver.quit()
