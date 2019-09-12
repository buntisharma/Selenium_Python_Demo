import selenium.webdriver
from Library import ConfigReader
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
class test_ApplyJob():
    def test_searchjob(self):
        self.driver.find_element_by_class_name(ConfigReader.SearchPage("Search","Skill")).send_keys("python")
        self.driver.find_element_by_class_name(ConfigReader.SearchPage("Search", "Location")).send_keys("Chandigarh")
        self.driver.find_element_by_class_name(ConfigReader.SearchPage("Search","Experiance")).click()