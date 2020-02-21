from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import selenium.webdriver.support.ui as ui
from selenium.common.exceptions import TimeoutException
import time

def write(USN,name,sgpa):
    # Writing results into csv file
    f.write(USN.text[6:]+","+name.text+","+sgpa.text+"\n")

chrome = webdriver.Chrome('./chromedriver') #additional download maybe required to match chrome version

wait = WebDriverWait(chrome, 600)

# Website to get results from
chrome.get('http://exam.msrit.edu')

# XPATHs for all the elements we will be interacting with
x_usn = '//input[@id="usn"]'
x_captcha = '//input[@id="osolCatchaTxt0"]'
x_go = '//input[@class="buttongo"]'
x_name = '//td[@class="headingdateWhite"]'
x_USN = '//td[@style=" text-transform:uppercase;"]'
x_sgpa = '//*[@id="main"]/div/table/tbody/tr[11]/td/table/tbody/tr/td[2]/table/tbody/tr/td[4]/div/span[2]'

# File to write the results in
f = open("5thSemResults.csv", "w+")

# The range is the USN range, can be adjusted
for i in range(1, 160):

    # Change your USNs for your banch and year accordingly
    usn = wait.until(ec.presence_of_element_located((By.XPATH, x_usn)))
    usn.send_keys("1MS17IS" + str(i).zfill(3)) #change usn prefix to generate results for multiple years

    captcha = wait.until(ec.presence_of_element_located((By.XPATH, x_captcha)))

    # Takes captcha as input from user in the first iteration
    if i == 1:
        temp = input("Enter Captcha: ") #initial requirement
    captcha.send_keys(temp)

    go = wait.until(ec.presence_of_element_located((By.XPATH, x_go)))
    go.click()

    try:
        wait = ui.WebDriverWait(chrome, 5) #waits for 5 seconds for page to load, if the USN DNE, then timer expires
        #timer may need to be adjusted according to loading speed
        USN = wait.until(ec.presence_of_element_located((By.XPATH, x_USN)))
        name = wait.until(ec.presence_of_element_located((By.XPATH, x_name)))
        sgpa = wait.until(ec.presence_of_element_located((By.XPATH, x_sgpa)))
        write(USN,name,sgpa)

    except TimeoutException: #catches timeout
        pass #proceeds as if nothing happened

    chrome.back() #move back to landing page
f.close() #close file