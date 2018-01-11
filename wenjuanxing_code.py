# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Wenjuanxing(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_wenjuanxing(self):
        driver = self.driver
        driver.get("https://www.wjx.top/m/19773335.aspx")
        driver.find_element_by_id("q1").click()
        driver.find_element_by_id("q1").clear()
        driver.find_element_by_id("q1").send_keys("zhangpeng")
        driver.find_element_by_xpath("//div[@id='div2']/div[2]/div[13]/span/a").click()
        driver.find_element_by_id("q3_0").click()
        driver.find_element_by_id("q3_0").clear()
        driver.find_element_by_id("q3_0").send_keys("1")
        driver.find_element_by_id("q3_1").click()
        driver.find_element_by_id("q3_1").clear()
        driver.find_element_by_id("q3_1").send_keys("1")
        driver.find_element_by_id("q4_0").click()
        driver.find_element_by_id("q4_0").clear()
        driver.find_element_by_id("q4_0").send_keys("1")
        driver.find_element_by_id("q4_1").click()
        driver.find_element_by_id("q4_1").clear()
        driver.find_element_by_id("q4_1").send_keys("1")
        driver.find_element_by_id("q5_0").click()
        driver.find_element_by_id("q5_0").clear()
        driver.find_element_by_id("q5_0").send_keys("1")
        driver.find_element_by_id("q5_1").click()
        driver.find_element_by_id("q5_1").clear()
        driver.find_element_by_id("q5_1").send_keys("1")
        driver.find_element_by_id("q6_0").click()
        driver.find_element_by_id("q6_0").clear()
        driver.find_element_by_id("q6_0").send_keys("1")
        driver.find_element_by_id("q6_1").click()
        driver.find_element_by_id("q6_1").clear()
        driver.find_element_by_id("q6_1").send_keys("1")
        driver.find_element_by_id("q7_0").click()
        driver.find_element_by_id("q7_0").clear()
        driver.find_element_by_id("q7_0").send_keys("1")
        driver.find_element_by_id("q7_1").click()
        driver.find_element_by_id("q7_1").clear()
        driver.find_element_by_id("q7_1").send_keys("1")
        driver.find_element_by_id("q8_0").click()
        driver.find_element_by_id("q8_0").clear()
        driver.find_element_by_id("q8_0").send_keys("1")
        driver.find_element_by_id("q8_1").click()
        driver.find_element_by_id("q8_1").clear()
        driver.find_element_by_id("q8_1").send_keys("1")
        driver.find_element_by_id("ctlNext").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    for i in range(3):
        unittest.main()
