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
import warnings,config
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
    el_get = wait(browser,10).until(EC.presence_of_element_located((By.XPATH, el)))
    el_get.send_keys(Keys.CONTROL, 'a')
    el_get.send_keys(Keys.BACKSPACE)
    wait(browser,10).until(EC.presence_of_element_located((By.XPATH, el))).send_keys(mount)

def xpath_el(el):
    element_all = wait(browser,3).until(EC.presence_of_element_located((By.XPATH, el)))
    
    return browser.execute_script("arguments[0].click();", element_all)
def xpath_fast(el):
    element_all = wait(browser,3).until(EC.presence_of_element_located((By.XPATH, el)))
    
    return browser.execute_script("arguments[0].click();", element_all)

def target(limit):
    try:
        xpath_el('//*[@class="m4b-base-btn m4b-base-btn-primary m4b-base-btn-size-default m4b-base-btn-shape-square"]')
    except:
        pass
    sleep(1)
    try:
        xpath_fast('//*[@class="sc-fubCzh evDYVz sc-kEjbQP fjEebh reactour__close"]')
    except:
        pass
    try:
        xpath_fast('//*[@class="m4b-base-btn m4b-base-btn-size-default m4b-base-btn-shape-square flex-c m4b-base-btn-primary -ml-12"]')
    except:
        pass
    xpath_fast('(//span[@class="arco-icon-hover arco-checkbox-icon-hover arco-checkbox-mask-wrapper"])[1]')
    sleep(1)
    xpath_fast('//button[@class="arco-btn arco-btn-primary arco-btn-size-default arco-btn-shape-square i18n-ecom-alliance-btn i18n-ecom-alliance-btn-text-p2-proxima-semibold i18n-ecom-alliance-btn-type-primary"]')
    sleep(1)
    xpath_el('(//span[@class="arco-icon-hover arco-checkbox-icon-hover arco-checkbox-mask-wrapper"])[1]')
    sleep(1)
    xpath_type('(//input[@class="arco-input arco-input-size-default"])[2]',"10")
    sleep(1)
    wait(browser,10).until(EC.presence_of_element_located((By.XPATH, f'//*[@class="arco-btn arco-btn-secondary arco-btn-size-default arco-btn-shape-square i18n-ecom-alliance-btn i18n-ecom-alliance-btn-text-p1-proxima-semibold"]'))).click()
 
    sleep(1)
    xpath_type('//input[@class="arco-input arco-input-size-default"]',program_name)
    username = wait(browser,10).until(EC.presence_of_element_located((By.XPATH, f'//input[@class="arco-select-view-input"]')))
    browser.execute_script("arguments[0].scrollIntoView();", username)
    for i in range(0,3): 
        try:
            xpath_type('//input[@class="arco-select-view-input"]',limit[i])
            sleep(1)
            xpath_el(f'(//*[text()="{limit[i]}"])[2]')
            sleep(1)
        
            print(f"[{time.strftime('%d-%m-%y %X')}] {limit[i]} inputted...")
 
            limit.remove(limit[i])
            with open('result.txt','w',encoding='utf-8') as f: f.write(f'')
            for m in limit[:]:
                with open('result.txt','a',encoding='utf-8') as f: f.write(f'{m}\n')
        except:
            try:
                xpath_type('//input[@class="arco-select-view-input"]',limit[i+1])
                sleep(1)
                xpath_el(f'(//*[text()="{limit[i+1]}"])[2]')
                sleep(1)
            
                print(f"[{time.strftime('%d-%m-%y %X')}] {limit[i+1]} inputted...")
    
                limit.remove(limit[i+1])
                with open('result.txt','w',encoding='utf-8') as f: f.write(f'')
                for m in limit[:]:
                    with open('result.txt','a',encoding='utf-8') as f: f.write(f'{m}\n')
            except:
                pass
    sleep(1)
    xpath_el('//button[@class="arco-btn arco-btn-primary arco-btn-size-default arco-btn-shape-square index__submit-btn--2KqYH i18n-ecom-alliance-btn i18n-ecom-alliance-btn-text-p2-proxima-semibold i18n-ecom-alliance-btn-type-primary"]')
    sleep(2)
    notif = wait(browser,10).until(EC.presence_of_element_located((By.XPATH, f'//span[@class="text-12 leading-18 text-grey-30"]'))).text
    print(f"[{time.strftime('%d-%m-%y %X')}] {notif}")
    sleep(10)
def open_browser(limit,datas):
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
            browser.get('https://affiliate.tiktok.com/seller/dashboard/plan/target-plan/add-target-plan')
        except:
            sleep(2)
         
    except:
    
        browser.get('https://affiliate.tiktok.com/seller/dashboard/plan/target-plan/add-target-plan')
    
    target(limit)
    
if __name__ == '__main__':

    print(f"[{time.strftime('%d-%m-%y %X')}] Automation Scrape Tiktok Shop")
    program_name = input(f"[{time.strftime('%d-%m-%y %X')}] Input Program Name: ")
    datas = input(f"[{time.strftime('%d-%m-%y %X')}] Input Email|Password: ")
    myfile = open(f"{cwd}/result.txt","r")
    limit = myfile.read()
    #emilnuha@gmail.com|emilnuha76
    limit = limit.split("\n")
    open_browser(limit,datas)
    
 
