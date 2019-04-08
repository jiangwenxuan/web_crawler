from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('D:/cs/python/chromedriver.exe')

def just_a_test(id_num, password):
    driver.get("http://fxcszx.hitwh.edu.cn/index.php/Home/Index/index.html")

    elem1 = driver.find_element_by_xpath("//input[@id='username']")
    elem1.send_keys(id_num)
    
    elem2 = driver.find_element_by_xpath("//input[@id='password']")
    elem2.send_keys(password)
    
    select = driver.find_element_by_xpath("//option[@value='2']")
    select.click()
    
    elem3 = driver.find_element_by_xpath("//button[@class='btn btn-primary btn-block loginbutton']")
    elem3.click()

    elem4 = driver.find_element_by_xpath("//a[@href='/index.php/Home/Index/instrList/sid/4.html']")
    elem4.click()

    elem5 = driver.find_element_by_xpath("//a[@href='/index.php/Home/Order/orderInstr/instr_id/13.html']")
    elem5.click()

    for i in range(1, 4):
        
        elem6 = driver.find_element_by_xpath("//td[@class='info']")
        elem6.click()
        all_handles = driver.window_handles
        current_window = driver.current_window_handle
        for handle in all_handles:
            if handle == current_window:
                driver.switch_to_window(handle)
                elem7 = driver.find_element_by_xpath("//button[@id='modalsubmitbtn']")
                time.sleep(0.5)
                elem7.click()
        driver.refresh()

"""
if you want to order some other equipment, you can change these code:

    for i in range(1, 9):
        driver.get("http://fxcszx.hitwh.edu.cn/index.php/Home/Index/instrList/sid/4/p/" + str(i) + "html")
        equipment_list = driver.find_elements_by_css_selector('h4.media-heading')
        for equipment in equipment_list:
            print(equipment.text)
"""

# id_num and password are strings
id_num = "1608XXX"
password = "XXXXXX"

just_a_test(id_num, password)
time.sleep(3)
driver.quit()
