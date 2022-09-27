import sys
sys.path.append('../')
# from config import Config
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Recognition.recognition import reader
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time


chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# chrome_options = webdriver.ChromeOptions()

driver = webdriver.Chrome("chromedriver.exe", chrome_options=chrome_options)
recognition_result = reader()

driver.get(f"https://www.google.com/")

try:
    cookie = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, '/html/body/div[2]/div[2]/div[3]/span/div/div/div/div[3]/div[1]/button[2]'))
    )
    cookie = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[3]/span/div/div/div/div[3]/div[1]/button[2]')
    cookie.click()
except NoSuchElementException:
    pass

try:
    input_bar = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input'))
        )
    input_bar = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
    input_bar.send_keys(recognition_result)
except NoSuchElementException:
    pass

try:
    search_button = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]')
    search_button.click()
except NoSuchElementException:
    pass

# driver = webdriver.Chrome('chromedriver.exe')



