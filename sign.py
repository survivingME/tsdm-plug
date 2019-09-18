from selenium import webdriver
import time
import utils

sign_page = 'https://www.tsdm.live/plugin.php?id=dsu_paulsign:sign'
content = 'happy tsdm, happy me'

print("start signing...")
while True:
    browser = webdriver.Chrome()
    tsdm_cookies = utils.read_cookies()
    browser.get(sign_page)
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
    browser.get(sign_page)
    if browser.current_url == sign_page:
        break
    else:
        utils.get_cookies()
browser.maximize_window()
browser.find_element_by_xpath('/html/body/div[7]/div/div[3]/div/div[1]/div[1]/form/table[1]/tbody/tr/td/ul/li[1]') \
    .click()
pages = browser.window_handles
browser.switch_to.window(pages[0])
browser.find_element_by_xpath('/html/body/div[7]/div/div[3]/div/div[1]/div[1]/form/table[2]/tbody/tr[2]/td[1]/input') \
    .send_keys(content)
browser.find_element_by_xpath('/html/body/div[7]/div/div[3]/div/div[1]/div[1]/form/table[1]/tbody/tr/td/div/a[1]') \
    .click()
print('no signature waiting...')
time.sleep(4)
browser.quit()