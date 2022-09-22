import sys
sys.path.append('../')
from Recognition.recognition import reader
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# chrome_options = webdriver.ChromeOptions()

driver = webdriver.Chrome("chromedriver.exe", chrome_options=chrome_options)
recognition_result = reader()

driver.get(f"https://www.google.com/search?q ={recognition_result}")

# driver = webdriver.Chrome('chromedriver.exe')



