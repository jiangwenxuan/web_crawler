from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('D:/cs/python/chromedriver.exe')
driver.get('http://www.python.org')
assert "Python" in driver.title
elem = driver.find_element_by_name('q')
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
print(driver.page_source)
