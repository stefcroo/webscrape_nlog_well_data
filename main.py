from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time
import os
import streamlit as st

before = os.listdir(os.getcwd())

def launchBrowser():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--incognito")
    chrome_options.add_experimental_option("prefs", {"download.default_directory":os.getcwd()})
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), chrome_options=chrome_options)
    driver.get('https://www.nlog.nl/datacenter/brh-overview')
    return driver
driver = launchBrowser()
driver.maximize_window()

def find_element():
    try:
        parent = driver.find_element_by_css_selector('span[class="select-all-box"]')
        checkbox = parent.find_element_by_css_selector('div[role="checkbox"]')
        print(checkbox)
        time.sleep(3)
        checkbox.click()
        time.sleep(2)
        download_btn =  driver.find_element_by_id('downloadExcel')
        file= download_btn.click()
        df = pd.read_excel(file)
        print(df.head())
        print(os.getcwd())
    except:
        print('no element with this class name')
find_element()
time.sleep(10)
driver.quit()
#checking the difference in the directory listing before and after downloading the file 
def fetch_df():
    after = os.listdir(os.getcwd())
    change = set(after) - set(before)
    if len(change)==1:
        file_name = change.pop()
    else:
        print('more than one file or no file downloaded')
    df = pd.read_excel(file_name)
    return df
df = fetch_df()
