import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import os

# open chrome
browser = webdriver.Chrome()

# open nwpu
browser.get('https://uis.nwpu.edu.cn/cas/login?service=https://ecampus.nwpu.edu.cn/')
time.sleep(1)

browser.maximize_window()

# login
browser.find_element(By.CSS_SELECTOR, "#vue_main > div:nth-child(2) > div.sw-login.sw-cloud-platform-nwpu-login > div > div:nth-child(2) > div:nth-child(3) > div > div > div:nth-child(1) > ul > li:nth-child(3)").click()
username = browser.find_element(By.ID, "username")
stu_number = ''
username.send_keys(stu_number)
stu_password = ''
password = browser.find_element(By.ID, "password")
password.send_keys(stu_password)
browser.find_element(By.XPATH, "//i[@class='el-button el-button--primary el-button--medium is-round']").click()
#browser.find_element(By.CSS_SELECTOR, "#fm1 > div:nth-child(4) > div > input.el-button.el-button--primary.el-button--medium.is-round").click()

time.sleep(5)
browser.refresh()


browser.get('https://yqtb.nwpu.edu.cn/wx/ry/jrsb_xs.jsp')
browser.refresh()
time.sleep(5)

#browser.find_element(By.CSS_SELECTOR, "#rbxx_div > div.weui-btn-area > div > a").click() # 提交填报信息
browser.find_element(By.LINK_TEXT, "提交填报信息").click() # 提交填报信息

#已核实
qrxx = browser.find_element(By.CSS_SELECTOR, "#qrxx_div > div.weui-cells.weui-cells_form > div.weui-cells.weui-cells_checkbox > label > div.weui-cell__hd > i")
hidden_qrxx = browser.find_element(By.CSS_SELECTOR, "#qrxx_div > div.weui-cells.weui-cells_form > div.weui-cells.weui-cells_checkbox > label")
ActionChains(browser).move_to_element(qrxx).click(hidden_qrxx).perform()

#browser.find_element(By.ID, "save_div").click() # 确认提交
time.sleep(1)

browser.quit()
