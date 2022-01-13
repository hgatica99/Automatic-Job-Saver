import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

user_email = os.environ.get("USER_EMAIL")
user_password = os.environ.get("USER_PASSWORD")

s = Service("C:\\Development\\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://www.linkedin.com/jobs/search/?distance=25&f_E=1%2C2&f_WT=2&geoId=106227249&keywords=sales"
           "%20engineer&location=Harrison%2C%20New%20York%2C%20United%20States")
driver.maximize_window()

sign_in_btn = driver.find_element(By.CSS_SELECTOR, "div a.nav__button-secondary")
sign_in_btn.click()

time.sleep(1)

user_name_field = driver.find_element(By.CSS_SELECTOR, "input#username")
password_field = driver.find_element(By.CSS_SELECTOR, "input#password")
sign_in_btn_login_page = driver.find_element(By.CSS_SELECTOR, "div.login__form_action_container button")

user_name_field.send_keys(user_email)
password_field.send_keys(user_password)
sign_in_btn_login_page.click()

time.sleep(1)

hide_msgs_btn = driver.find_element(By.XPATH, "/html/body/div[5]/aside/section/header/div[3]/button[2]")
hide_msgs_btn.click()

jobs_list = driver.find_elements(By.CSS_SELECTOR, "div.job-card-container")
top_five_jobs = jobs_list[0:6]

time.sleep(2)

save_btn = driver.find_element(By.CLASS_NAME, "jobs-save-button")

for item in top_five_jobs:
    item.click()
    time.sleep(1)
    save_btn.click()

print("Done saving top 5 jobs")
