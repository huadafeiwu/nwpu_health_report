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
username = browser.find_element(By.ID, 'username')
username.send_keys(USERNAME)
password = browser.find_element(By.ID, 'password')
password.send_keys(PASSWORD)

aabb = browser.find_element(By.NAME, "execution")
time.sleep(1)

browser.quit()
