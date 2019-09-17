from selenium import webdriver
import pickle
import time
import os

main_page = 'https://www.tsdm.live/forum.php'
login_page = 'https://www.tsdm.live/member.php?mod=logging&action=login'
sign_page = 'https://www.tsdm.live/plugin.php?id=dsu_paulsign:sign'
work_page = 'https://www.tsdm.live/plugin.php?id=np_cliworkdz:work'
content = 'happy tsdm, happy me'


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
    output_path = open('./dist/tsdm_cookies.pickle', 'wb')
    pickle.dump(cookies, output_path)
    output_path.close()
    return cookies


def read_cookies():
    # if hava cookies file ,use it
    # if not , getTaobaoCookies()
    if os.path.exists('./dist/tsdm_cookies.pickle'):
        read_path = open('./dist/tsdm_cookies.pickle','rb')
        tsdm_cookies = pickle.load(read_path)
    else:
        tsdm_cookies = get_cookies()
    return tsdm_cookies


def sign():
    browser = webdriver.Chrome()
    tsdm_cookies = read_cookies()

    browser.get(sign_page)
    print("wait login page...")
    time.sleep(5)
    for cookie in tsdm_cookies:
        browser.add_cookie({
            "domain": ".taobao.com",
            "name": cookie,
            "value": tsdm_cookies[cookie],
            "path": '/',
            "expires": None
        })
    browser.get(sign_page)
    print("show sign page")
    time.sleep(10)
    # todo: sign action
    browser.quit()


def work():
    browser = webdriver.Chrome()
    tsdm_cookies = read_cookies()

    browser.get(work_page)
    print("wait login page...")
    time.sleep(10)
    for cookie in tsdm_cookies:
        browser.add_cookie({
            "domain": ".taobao.com",
            "name": cookie,
            "value": tsdm_cookies[cookie],
            "path": '/',
            "expires": None
        })
    browser.get(work_page)
    # todo: sign action


if __name__ == "__main__":
    sign()