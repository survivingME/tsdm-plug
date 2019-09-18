from selenium import webdriver
import utils
import time

work_page = 'https://www.tsdm.live/plugin.php?id=np_cliworkdz:work'

print("start working...")
while True:
    browser = webdriver.Chrome()
    tsdm_cookies = utils.read_cookies()
    browser.get(work_page)
    browser.delete_all_cookies()
    print("wait login page...")
    time.sleep(4)
    for cookie in tsdm_cookies:
        browser.add_cookie({
            "domain": ".tsdm.live",
            "name": cookie,
            "value": tsdm_cookies[cookie],
            "path": '/',
            "expires": None
        })
    browser.get(work_page)
    if browser.current_url == work_page:
        break
    else:
        utils.get_cookies()
browser.maximize_window()
browser.find_element_by_xpath(
    '/html/body/div[7]/div/div[3]/div[1]/div/div[2]/table/tbody/tr[2]/td/center/div/div[1]/a').click()
pages = browser.window_handles
print("wait to simulate human...")
time.sleep(1)
browser.switch_to.window(pages[0])
browser.find_element_by_xpath(
    '/html/body/div[7]/div/div[3]/div[1]/div/div[2]/table/tbody/tr[2]/td/center/div/div[2]/a').click()
pages = browser.window_handles
print("wait to simulate human...")
time.sleep(1)
browser.switch_to.window(pages[0])
browser.find_element_by_xpath(
    '/html/body/div[7]/div/div[3]/div[1]/div/div[2]/table/tbody/tr[2]/td/center/div/div[3]/a').click()
pages = browser.window_handles
print("wait to simulate human...")
time.sleep(1)
browser.switch_to.window(pages[0])
browser.find_element_by_xpath(
    '/html/body/div[7]/div/div[3]/div[1]/div/div[2]/table/tbody/tr[2]/td/center/div/div[4]/a').click()
pages = browser.window_handles
print("wait to simulate human...")
time.sleep(1)
browser.switch_to.window(pages[0])
browser.find_element_by_xpath(
    '/html/body/div[7]/div/div[3]/div[1]/div/div[2]/table/tbody/tr[2]/td/center/div/div[5]/a').click()
pages = browser.window_handles
print("wait to simulate human...")
time.sleep(1)
browser.switch_to.window(pages[0])
browser.find_element_by_xpath(
    '/html/body/div[7]/div/div[3]/div[1]/div/div[2]/table/tbody/tr[2]/td/center/div/div[6]/a').click()
print("wait to simulate human...")
time.sleep(2)
browser.switch_to.window(pages[0])
browser.find_element_by_xpath('/html/body/div[7]/div/div[3]/div[2]/div[2]/div[2]/ul/li[2]/form/div/a').click()
print("no signature waiting...")
time.sleep(2)
browser.quit()
