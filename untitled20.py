# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 18:02:38 2018

@author: zhangp
"""

# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Panxiaodong(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_panxiaodong(self):
        driver = self.driver
        driver.get("https://www.wjx.cn/m/13467050.aspx")
        driver.find_element_by_xpath("//div[@id='div1']/div[2]/div/span/a").click()
        driver.find_element_by_xpath("//div[@id='div2']/div[2]/div/span/a").click()
        driver.find_element_by_xpath("//div[@id='div3']/div[2]/div/span/a").click()
        driver.find_element_by_xpath("//div[@id='div4']/div[2]/div/span/a").click()
        driver.find_element_by_xpath("//div[@id='div5']/div[2]/div/span/a").click()
        driver.find_element_by_xpath("//div[@id='div6']/div[2]/div/span/a").click()
        driver.find_element_by_xpath("//div[@id='div7']/div[2]/div/span/a").click()
        driver.find_element_by_xpath("//div[@id='div8']/div[2]/div/span/a").click()
        driver.find_element_by_id("q9").click()
        driver.find_element_by_id("q9").clear()
        driver.find_element_by_id("q9").send_keys(u"暂无")
        driver.find_element_by_id("q10").click()
        driver.find_element_by_id("q10").clear()
        driver.find_element_by_id("q10").send_keys(u"希望")
        time.sleep(5)
        driver.find_element_by_id("ctlNext").click()
        self.assertEqual(u"您输入的验证码有误，请重新输入！", self.close_alert_and_get_its_text())
        driver.find_element_by_id("yucinput").click()
        driver.find_element_by_id("yucinput").clear()
        driver.find_element_by_id("yucinput").send_keys("RAYA")
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
    unittest.main()
