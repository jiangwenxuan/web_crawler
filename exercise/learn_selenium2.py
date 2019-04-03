import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome('D:/cs/python/chromedriver.exe')

def just_a_test():
    driver.get("http://fxcszx.hitwh.edu.cn/index.php/Home/Index/index.html")

    elem1 = driver.find_element_by_xpath("//input[@id='username']")
    elem1.send_keys("160810309")
    
    elem2 = driver.find_element_by_xpath("//input[@id='password']")
    elem2.send_keys("Lw4SLhpniXzb7xg")
    
    select = driver.find_element_by_xpath("//option[@value='2']")
    select.click()
    
    elem3 = driver.find_element_by_xpath("//button[@class='btn btn-primary btn-block loginbutton']")
    elem3.click()

def tearDown(self):
    driver.close()

just_a_test()
