from selenium import webdriver
import time
import contextlib
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait


chromedriver = 'C:\\Users\\priya.singh\\Desktop\\chromedriver\\chromedriver.exe'
driver = webdriver.Chrome(executable_path=chromedriver) #, chrome_options=chromeOptions)
driver.get("https://ufeqa.markit.com/home/login.jsp")

uname = driver.find_element_by_id("username")
pwd = driver.find_element_by_id("password")
uname.send_keys("mer.test22@ihsmarkit.com")
pwd.send_keys("Welcome#30")
btn=driver.find_element_by_id("submit")
btn.click()
#element_present = EC.presence_of_element_located((By.ID, 'ext-gen53'))
#WebDriverWait(driver, timeout).until(element_present)
#btn1=driver.find_element_by_xpath("//div[@class='x-btn-arrow")
#btn1= WebDriverWait(driver, 10).until(
 #       EC.presence_of_element_located((By.XPATH, ".//div[@class='x-btn-arrow")
#driver.implicitly_wait(50)
#btn1=driver.find_element_by_xpath(".//div[contains(id,'ext-gen')][@role='button'][contains(@class, ' x-btn-text icon-new')]")
#btn1.click()
#n = WebDriverWait(driver, 30)
wait = WebDriverWait(driver, 50)
element = wait.until(EC.alert_is_present((By.CLASS_NAME, "brand pull-left")))
