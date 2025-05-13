from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time


service = ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://panel.kudos.ir/")
title = driver.title
print(f"title: {title}")


input_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.label-input > input[type='text']"))
    )
input_element.send_keys("***enter your msisdn***")

button_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[.//span[text()='ادامه']]"))
    )
button_element.click()

# login_link = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.CSS_SELECTOR, "span.font-semibold.text-sm.text-title.cursor-pointer"))
#     )
# login_link.click()
# print("pass login_link ")


password_input = WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.XPATH, "//input[@type='password' and @data-v-665af39e]"))
)
password_input.send_keys("***enter your password***")
print("password")

icon_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.v-btn-fill-primary.flex.justify-center.items-center.rounded-xl"))
    )
icon_element.click()
print("login")


send_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "span[data-v-b97a42a7].font-bold.text-sm.xs\\:text-xs"))
    )
send_element.click()
print("send")

skeleton_element = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "div.image-container.w-full.rounded-t-xl.h-40"))
    )
skeleton_element.click()
print("select 50")


try:
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "dropdown"))
    )
    search_box.click()
    search_box.send_keys("***enter user name***")
    print("search box")
    search_results = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, "//div[@data-v-71890b53 and @class='user-item']"))
    )
    print(f"{len(search_results)} find")
    time.sleep(10)
    user_item = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//div[@data-v-71890b53 and @class='user-item']"))
    )
    user_item.click()
    print("click user item")

except Exception as e:
    print(f"exception: {e}")
time.sleep(10)

textarea_element = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//label[text()='متن کارت خود را بنویسید']/preceding-sibling::textarea"))
    )
textarea_element.send_keys("The panel has a bug, and its 24-hour limit has been removed.If this is not considered a bug (this kudos was recorded for teamwork).")
print("enter your text in the textarea")
send_span = WebDriverWait(driver, 50).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "span[data-v-b97a42a7].font-bold.text-sm.xs\\:text-xs"))
    )
time.sleep(10)

send_span.find_element(By.XPATH, '//*[@id="app"]/div/div/div[4]/main/div/div[1]/div/div[2]/button/span/span').click()
print("send kudos")

time.sleep(10)

driver.quit()

