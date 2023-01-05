import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv


URL = 'https://shop.rewe.de/p/all-stars-whey-protein-pulver-milky-vanilla-400g/8658165'

driver = uc.Chrome(use_subprocess=True)
wait = WebDriverWait(driver, 20)


def get_data_product(URL):
    driver.get(URL)
    wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[3]/div[2]/section/div[3]/div[1]/h2')))
    rows = len(driver.find_elements(By.XPATH, '/html/body/div[3]/div[2]/section/div[3]/div[2]/div[2]/table/tbody'))
    print(rows)
    print(driver.find_elements(By))
    
get_data_product(URL)
print("stsw")


# /html/body/div[2]/div[2]/section/div[3]/div[2]/div[2]/table/tbody/tr[6]/td[1]
# /html/body/div[2]/div[2]/section/div[3]/div[2]/div[2]/table/tbody/tr[7]/td[1]
# /html/body/div[2]/div[2]/section/div[3]/div[2]/div[2]/table/tbody/tr[7]/td[2]
