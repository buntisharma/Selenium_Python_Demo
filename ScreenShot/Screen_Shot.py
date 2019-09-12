from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
class Screenshots():
    def takeScreenshot(self, driver):
        """
        Takes screenshot of the current open web pag
        """
        fileName = str(round(time.time() * 1000)) + ".png"
        screenshotDirectory = "/Users/atomar/desktop/"
        destinationFile = screenshotDirectory + fileName

        try:
            driver.save_screenshot(destinationFile)
            print("Screenshot saved to directory --> :: " + destinationFile)
        except NotADirectoryError:
            print("Not a directory issue")


ff = Screenshots()
ff.test()