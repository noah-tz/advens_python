# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestPastebin():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_tastebin(self):
    # Test name: tastebin
    # Step # | name | target | value
    # 1 | open | https://pastebin.com/ | 
    self.driver.get("https://pastebin.com/")
    # 2 | setWindowSize | 1528x816 | 
    self.driver.set_window_size(1528, 816)
    # 3 | click | id=postform-text | 
    self.driver.find_element(By.ID, "postform-text").click()
    # 4 | runScript | window.scrollTo(0,716.7999877929688) | 
    self.driver.execute_script("window.scrollTo(0,716.7999877929688)")
    # 5 | click | id=postform-name | 
    self.driver.find_element(By.ID, "postform-name").click()
    # 6 | type | id=postform-text | test 123 test test
    self.driver.find_element(By.ID, "postform-text").send_keys("test 123 test test")
    # 7 | type | id=postform-name | myfirstselenium
    self.driver.find_element(By.ID, "postform-name").send_keys("myfirstselenium")
    # 8 | click | css=.-big | 
    self.driver.find_element(By.CSS_SELECTOR, ".-big").click()
    # 9 | runScript | window.scrollTo(0,439.20001220703125) | 
    self.driver.execute_script("window.scrollTo(0,439.20001220703125)")
  
