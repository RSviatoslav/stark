import os
from selenium import webdriver
import pyautogui
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


pwd = 'password'

os.environ['PATH'] += r"C:\Users\F5Vadym\projects\automatization\chromedriver_win32"

# o = webdriver.ChromeOptions()
# o.add_argument("--user-data-dir=/Users/F5Vadym/AppData/Local/Google/Chrome/User Data")
# o.add_argument("--profile-directory=Profile 19")
# o.add_argument("--disable-blink-features=AutomationControlled")
# o.add_experimental_option("excludeSwitches", ["enable-automation"])
# o.add_experimental_option("useAutomationExtension", False)
#
# driver = webdriver.Chrome(options=o)

driver = webdriver.Chrome()
# Open StarkNet Bridge
driver.maximize_window()

# Read & accept terms

driver.get('https://starkgate.starknet.io/')
mainHandle = driver.window_handles
time.sleep(2)

try:
    terms = driver.find_element(By.XPATH, '//li[15]/h2')
    time.sleep(2)
    driver.execute_script("arguments[0].scrollIntoView();", terms)
    Accept = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div[2]/div/button')
    Accept.click()
    time.sleep(2)
except NoSuchElementException:
    error_occurred = True
    EthWallet = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/button[1]')
    EthWallet.click()
    time.sleep(2)
    CEth = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div/div/div[2]/div')
    CEth.click()
    time.sleep(3)
    driver.switch_to.window(driver.window_handles[1])
    #
    # # Password MM
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys('password')
    pyautogui.press('enter')
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div[3]/div[2]/button[2]').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div[2]/div[2]/div[2]/footer/button[2]').click()
finally:
    EthWallet = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/button[1]')
    EthWallet.click()
    time.sleep(2)
    CEth = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div/div/div[2]/div')
    CEth.click()
    time.sleep(3)
    driver.switch_to.window(driver.window_handles[1])
    #
    # # Password MM
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys('password')
    pyautogui.press('enter')
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div[3]/div[2]/button[2]').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div[2]/div[2]/div[2]/footer/button[2]').click()

