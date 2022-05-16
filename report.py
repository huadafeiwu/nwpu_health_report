import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os


# open chrome
driver = webdriver.Chrome()

# open nwpu
driver.get('https://uis.nwpu.edu.cn/cas/login?service=https://ecampus.nwpu.edu.cn/')

driver.maximize_window()

# login
username = driver.find_element(By.ID, "username")
stu_number = '2021262833'
username.send_keys(stu_number)
stu_password = 'wc15664907920.'
password = driver.find_element(By.ID, "password")
password.send_keys(stu_password)
driver.find_element(By.NAME, "submit").click()
time.sleep(1)

driver.get('https://yqtb.nwpu.edu.cn/wx/xg/yz-mobile/index.jsp')
driver.get('https://yqtb.nwpu.edu.cn/wx/ry/jrsb_xs.jsp')

driver.execute_script('javascript:go_sub();')

driver.find_element(By.XPATH, "//i[@class='weui-icon-checked']").click() # 已核实 
driver.execute_script('javascript:save();')
time.sleep(1)
    
driver.close()
driver.quit()