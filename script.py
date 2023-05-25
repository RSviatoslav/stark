import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

pwd = 'password'
# Connect driver & chrome profile
s = Service(r"/Users/zorian/PycharmProjects/autoTest/chromedriver")
o = webdriver.ChromeOptions()
o.add_argument("--user-data-dir=/Users/zorian/Library/Application Support/Google/Chrome/")
o.add_argument("--profile-directory=Profile 4")
o.add_argument("--disable-blink-features=AutomationControlled")
o.add_experimental_option("excludeSwitches", ["enable-automation"])
o.add_experimental_option("useAutomationExtension", False)
)
# Open StarkNet Bridge
browser = webdriver.Chrome(service=s, options=o)
# browser.execute_cdp_cmd()
browser.maximize_window()

# Read & accept terms
# terms = browser.find_element(By.XPATH, '//li[15]/h2')
# time.sleep(2)
# browser.execute_script("arguments[0].scrollIntoView();", terms)
# Accept = browser.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div[2]/div/button')
# Accept.click()
# time.sleep(2)

browser.get('https://starkgate.starknet.io/')
mainHandle = browser.window_handles
time.sleep(2)
# Connect Wallet
EthWallet = browser.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/button[1]')
EthWallet.click()
time.sleep(2)
CEth = browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div/div/div[2]/div')
CEth.click()
time.sleep(3)
browser.switch_to.window(browser.window_handles[1])

# Password MM
browser.find_element(By.XPATH, '//*[@id="password"]').send_keys(pwd, Keys.ENTER)
time.sleep(1)
browser.find_element(By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div[3]/div[2]/button[2]').click()
time.sleep(1)
browser.find_element(By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div[2]/div[2]/div[2]/footer/button[2]').click()
time.sleep(10)
browser.close()
browser.quit()
