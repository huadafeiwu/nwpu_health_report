import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import os

USERNAME = os.environ["USERNAME"]
PASSWORD = os.environ["PASSWORD"]

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
browser = webdriver.Chrome('/usr/bin/chromedriver', chrome_options=chrome_options)

# open nwpu
browser.get('https://uis.nwpu.edu.cn/cas/login?service=https://ecampus.nwpu.edu.cn/')
browser.maximize_window()
time.sleep(5)

# login
browser.find_element(By.CSS_SELECTOR, "#vue_main > div:nth-child(2) > div.sw-login.sw-cloud-platform-nwpu-login > div > div:nth-child(2) > div:nth-child(3) > div > div > div:nth-child(1) > ul > li:nth-child(3)").click()
username = browser.find_element(By.ID, "username")

username.send_keys(USERNAME)
#password = browser.find_element(By.ID, 'password')
#password.send_keys(PASSWORD)

#aabb = browser.find_element(By.NAME, "execution")
time.sleep(1)

browser.quit()
