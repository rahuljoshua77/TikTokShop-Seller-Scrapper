from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import os, json
import random
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from multiprocessing import Pool
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 
cwd = os.getcwd()

opts = webdriver.ChromeOptions()

 
opts.headless = False
opts.add_argument('log-level=3') 
dc = DesiredCapabilities.CHROME
dc['loggingPrefs'] = {'driver': 'OFF', 'server': 'OFF', 'browser': 'OFF'}
opts.add_argument('--ignore-ssl-errors=yes')
opts.add_argument("--start-maximized")
#opts.add_argument("window-size=200,100"
opts.add_argument('--no-sandbox')
 
opts.add_argument('--disable-setuid-sandbox')
opts.add_argument('disable-infobars')
opts.add_argument('--ignore-certificate-errors')
opts.add_argument('--disable-blink-features=AutomationControlled')
 
opts.add_experimental_option("useAutomationExtension", False)
opts.add_experimental_option("excludeSwitches",["enable-automation"])
prefs = {"profile.default_content_setting_values.notifications" : 2}
opts.add_experimental_option("prefs",prefs)
opts.add_experimental_option('excludeSwitches', ['enable-logging'])
def xpath_type(el,mount):
    return wait(browser,10).until(EC.presence_of_element_located((By.XPATH, el))).send_keys(mount)

def xpath_el(el):
    element_all = wait(browser,10).until(EC.presence_of_element_located((By.XPATH, el)))
    
    return browser.execute_script("arguments[0].click();", element_all)
def xpath_fast(el):
    element_all = wait(browser,10).until(EC.presence_of_element_located((By.XPATH, el)))
    
    return browser.execute_script("arguments[0].click();", element_all)

def scrape(cathegory,limit):
    try:
        xpath_el('//*[@class="m4b-base-btn m4b-base-btn-primary m4b-base-btn-size-default m4b-base-btn-shape-square"]')
    except:
        pass
 
    try:
        xpath_fast('//*[@class="sc-fubCzh evDYVz sc-kEjbQP fjEebh reactour__close"]')
    except:
        pass
    
    sleep(1)
    xpath_el('//button[@elementtiming="element-timing"]')
    sleep(1)
    xpath_type('//input[@class="arco-input-tag-input arco-input-tag-input-size-large"]',cathegory)
    sleep(1)
    xpath_type('//input[@class="arco-input-tag-input arco-input-tag-input-size-large"]',Keys.ENTER)
    sleep(1)
    xpath_el('(//button[@elementtiming="element-timing"])[1]')
    n=1
    trying = 1
    for i in range(1,limit+1): 
        try:
            username = wait(browser,10).until(EC.presence_of_element_located((By.XPATH, f'(//div[@class="flex items-center"]/div[@elementtiming="element-timing"])[{i}]')))
            browser.execute_script("arguments[0].scrollIntoView();", username)
            print(f"[{time.strftime('%d-%m-%y %X')}] {n} {username.text}")
            n=n+1
            with open('result.txt','a') as f: f.write(f'{username.text}\n')
        except:
            if trying == 5:
                break
            trying = trying + 1
            
def open_browser(cathegory,limit,datas):
    datas = datas.split("|")
    email = datas[0]
    password = datas[1]
    global browser
    #opts.add_argument(f"user-agent=Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36")
    opts.add_argument("--user-data-dir=C:\\Users\\rahul\\AppData\\Local\\Google\\Chrome\\User Data\\Default")
    opts.add_argument(f'--profile-directory={email}')
    browser = webdriver.Chrome(options=opts, desired_capabilities=dc)
 
    
   
    try:
        browser.get('https://seller-id.tiktok.com/account/login?redirect_url=https%3A%2F%2Faffiliate.tiktok.com%2Fseller%2Fdashboard')
        sleep(5)
    except:
        sleep(2)
 
    try:
        xpath_el('//span[@id="TikTok_Ads_SSO_Login_Email_Panel_Button"]')
        xpath_type('//input[@type="email"]',email)
        xpath_type('//input[@type="password"]',password)
        xpath_type('//input[@type="password"]',Keys.ENTER)
         
        input(f"[{time.strftime('%d-%m-%y %X')}] Push ENTER if you solved the captcha: ")
        try:
            xpath_fast('//div[@class="verify-captcha-submit-button mobile-button__Button-tntg7q-0 bQqmBt"]')
        except:
            pass
        otp = int(input(f"[{time.strftime('%d-%m-%y %X')}] Input OTP: "))
        xpath_type('//input[@name="code"]',otp)
        xpath_fast('//*[@name="CodeloginBtn"]')
        sleep(10)
        try:
            browser.get('https://affiliate.tiktok.com/seller/dashboard/tcm/creator-marketplace')
        except:
            sleep(2)
         
    except:
    
        browser.get('https://affiliate.tiktok.com/seller/dashboard/tcm/creator-marketplace')
 
    scrape(cathegory,limit)
    
if __name__ == '__main__':

    print(f"[{time.strftime('%d-%m-%y %X')}] Automation Scrape Tiktok Shop")
    cathegory = input(f"[{time.strftime('%d-%m-%y %X')}] Kategori: ")
    limit = int(input(f"[{time.strftime('%d-%m-%y %X')}] Limit Scrape(1-999999): "))
    datas = input(f"[{time.strftime('%d-%m-%y %X')}] Input Email|Password: ")
    open_browser(cathegory,limit,datas)

    
