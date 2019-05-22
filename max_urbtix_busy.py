#!/usr/bin/env python
#encoding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By

import time
import platform


#執行方式：python max_checkbox.py 或 python3 max_checkbox.py
#附註：沒有寫的很好，很多地方應該可以模組化。

CONST_APP_VERSION = u"Max UrbtixBusy Bot (2019.05.23)"

# initial webdriver
# 說明：初始化 webdriver
driver = None

browser = "chrome"

print("version", CONST_APP_VERSION)

Root_Dir = ""
if browser == "chrome":
    chrome_options = None
    # default os is linux/mac
    chromedriver_path =Root_Dir+ "webdriver/chromedriver"
    if platform.system()=="windows":
        chromedriver_path =Root_Dir+ "webdriver/chromedriver.exe"
    driver = webdriver.Chrome(options=chrome_options, executable_path=chromedriver_path)

def checkbox_main(url):
    ret = False
    form_checkbox_list = None
    try:
        form_checkbox_list = driver.find_elements(By.CSS_SELECTOR, "input[type=checkbox]")
        if not form_checkbox_list is None:
            for form_checkbox in form_checkbox_list:
                if not form_checkbox.is_selected():
                    form_checkbox.click()
                    ret = True
    except Exception as exc:
        print("click checkbox fail")
        pass

    return ret


def main():
    driver.get('http://www.urbtix.hk/')
    
    last_url = ""

    while True:
        time.sleep(0.25)
        url = ""
        try:
            url = driver.current_url
        except Exception as exc:
            pass

        if url is None:
            continue
        else:
            if len(url) == 0:
                continue

        # 說明：輸出目前網址，覺得吵的話，請註解掉這行。
        if len(url) > 0 :
            if url != last_url:
                print(url)
            last_url = url

        is_checkboxed = checkbox_main(url)

        if 'msg.urbtix.hk' in url:
            driver.get('http://www.urbtix.hk/')
        if 'busy.urbtix.hk' in url:
            driver.get('http://www.urbtix.hk/')



main()