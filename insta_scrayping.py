from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import chromedriver_binary
import urllib.parse
import time
import const

const.INSTA_URL = "https://www.instagram.com/"
const.INSTA_TAG_SEARCH_URL = const.INSTA_URL + "explore/tags/{}/?hl=ja"
const.USER=''
const.PASS=''

#いいねのPATH
const.LIKE_BOTTON='body > div._2dDPU.CkGkG > div.zZYga > div > article > div.eo2As > section.ltpMr.Slqrh > span.fr66n > button > div > span > svg'

#loginメソッド
def login(url, user, password):
    if url == None or user == None or password == None:
        print("user,password or url is missing.")

    LOGIN_PATH = '//*[@id="loginForm"]/div/div[3]'

    try:
        # browser = webdriver.Chrome(executable_path='/Users/tashiroshunpei/Desktop/chromedriver')
        browser = webdriver.Chrome()
        browser.get(url)
        sleep(1)
        browser.find_element_by_xpath(LOGIN_PATH).click()
        usernameField = browser.find_element_by_name('username')
        usernameField.send_keys(user)
        passwordField = browser.find_element_by_name('password')
        passwordField.send_keys(password)
        sleep(1)
        passwordField.send_keys(Keys.RETURN)
    except:
        "An error has occurred. login failed."

    return browser

def search_post_with_tag(browser, tag_name):
    #tag検索メソッド
    encodedTag = urllib.parse.quote(tag_name) #普通にURLに日本語は入れられないので、エンコードする
    encodedURL = const.INSTA_TAG_SEARCH_URL.format(encodedTag)
    print("encodedURL:{}".format(encodedURL))
    browser.get(encodedURL)
    # print("")

# time classのwrapper
def sleep(sec):
    time.sleep(sec)

def main():
    #各種XPATH
    MEDIA_SELECTER ='div._9AhH0'
    MEDIA_NEXT = '/html/body/div[4]/div[1]/div/div/a[2]'

    # login
    browser = login(const.INSTA_URL, const.USER, const.PASS)

    sleep(6)

    tag_name = '検索タグ'
    search_post_with_tag(browser, tag_name)

    #body > div._2dDPU.CkGkG > div.zZYga > div > article > div.eo2As > section.ltpMr.Slqrh > span.fr66n > button > div > span > svg
    #body > div._2dDPU.CkGkG > div.zZYga > div > article > div.eo2As > section.ltpMr.Slqrh > span.fr66n > button > div > span > svg

    #投稿をクリック
    sleep(1)
    browser.implicitly_wait(10)
    browser.find_element_by_css_selector(MEDIA_SELECTER).click()

    #いいねカウンター
    likeCounter = 0
    likeMax = 100

    if likeCounter < likeMax:
        sleep(1)
        print("========= いいね検索開始 =========")
        
        # browser.find_elements_by_css_selector[0](LIKE_BOTTON).click        
        button = browser.find_element_by_css_selector(const.LIKE_BOTTON)
        button.click()
            
        likeCounter += 1
        print("likeed {}".format(likeCounter))
        sleep(5)
        browser.find_element_by_name('次へ').click()
    elif likeCounter == likeMax:
        pass
    else :
        print("You liked {} media".format(likedCounter))
    
main()

 
#   try:
#      browser.browser.find_element_by_name('いいね').click()
#        likeCounter += 1
#        print("likeed {}".format(likeCounter))
#    except:
#        #読み込まれなかったりすでにいいねしてたらpass
#        print("not good") 
#        pass

    #次へ
#    try:
#        browser.browser.find_element_by_name('次へ').click()
#    except:
#        break
#print("you liked {} media".format(likeCounter))




