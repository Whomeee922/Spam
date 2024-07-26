from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chat_url = "https://example.com/chat"
username = "username"
password = "password"
message = "این یک پیام هرزنامه است."

driver = webdriver.Chrome()

driver.get(chat_url)
time.sleep(2)

driver.find_element_by_name("username").send_keys(username)
driver.find_element_by_name("password").send_keys(password)
driver.find_element_by_name("login").click()
time.sleep(2)

for i in range(10):
    driver.find_element_by_name("message").send_keys(message)
    driver.find_element_by_name("send").click()
    time.sleep(1)

driver.quit()
