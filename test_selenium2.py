from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get("https://www.selenium.dev/selenium/web/web-form.html")
title = driver.title
text_box = driver.find_element(by=By.NAME, value="my-text")
text_box.send_keys("Selenium KF")
submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")
time.sleep(5)
#driver.implicitly_wait(0.5)
submit_button.click()
message = driver.find_element(by=By.ID, value="message")
text = message.text
print(text)
time.sleep(2)
#driver.implicitly_wait(0.5)
driver.quit()