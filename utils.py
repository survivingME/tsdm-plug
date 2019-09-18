from selenium import webdriver
import pickle
import time
import os

login_page = 'https://www.tsdm.live/member.php?mod=logging&action=login'


def get_cookies():
    browser = webdriver.Chrome()
    browser.get(login_page)
    print("wait web...")
    time.sleep(5)

    browser.find_element_by_xpath(
        '/html/body/div[7]/div/div[2]/div[2]/div/div[2]/div[1]/div[1]/form/div/div[1]/table/tbody/tr/td[1]/input').send_keys(
        'survivingME')
    browser.find_element_by_xpath(
        '/html/body/div[7]/div/div[2]/div[2]/div/div[2]/div[1]/div[1]/form/div/div[2]/table/tbody/tr/td[1]/input').send_keys(
        '123fyaiqyn!@3')
    print("wait to simulate human...")
    time.sleep(2)
    man_verify_code = input("input verify code：")
    print("verify code inputted, waiting...")
    browser.find_element_by_xpath(
        '/html/body/div[7]/div/div[2]/div[2]/div/div[2]/div[1]/div[1]/form/div/div[3]/p[2]/input').send_keys(
        man_verify_code)
    browser.find_element_by_xpath(
        '/html/body/div[7]/div/div[2]/div[2]/div/div[2]/div[1]/div[1]/form/div/div[7]/table/tbody/tr/td[1]/button').click()
    print("wait web...")
    time.sleep(5)
    # dump cookies
    print("start dumping cookies")
    tsdm_cookies = browser.get_cookies()
    browser.quit()
    cookies = {}
    for item in tsdm_cookies:
        cookies[item['name']] = item['value']
    output_path = open('./tsdm_cookies.pickle', 'wb')
    pickle.dump(cookies, output_path)
    output_path.close()
    return cookies


def read_cookies():
    # if hava cookies file ,use it
    # if not , get_cookies()
    if os.path.exists('./tsdm_cookies.pickle'):
        print("read cookies success...")
        read_path = open('./tsdm_cookies.pickle','rb')
        tsdm_cookies = pickle.load(read_path)
    else:
        tsdm_cookies = get_cookies()
    return tsdm_cookies
