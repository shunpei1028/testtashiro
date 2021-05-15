# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib.parse
import time
import const
#import chromedriver_binary                  # パスを通すためのコード
#from selenium.webdriver.chrome.options import Options # オプションを使うために必要
#option = Options()                          # オプションを用意
#option.add_argument('--headless')           # ヘッドレスモードの設定を付与
#driver = webdriver.Chrome(options=option)   # Chromeを準備(optionでヘッドレスモードにしている）


#Webdriver
browser = webdriver.Chrome(executable_path='/Users/tashiroshunpei/Desktop/chromedriver')
#browser = driver(executable_path='/Users/tashiroshunpei/Desktop/chromedriver')
INSTA_URL = 'https://www.instagram.com/'
TAG_SEARCH_URL = INSTA_URL + "explore/tags/{}/?hl=ja"


#各種XPATH
LOGIN_PATH = '//*[@id="loginForm"]/div/div[3]'
MEDIA_SELECTER ='div._9AhH0'
MEDIA_NEXT = '/html/body/div[4]/div[1]/div/div/a[2]'

#ユーザー情報
username=''
user_passward = ''
tag_name = '珈琲'
next_botton = "body > div._2dDPU.CkGkG > div.EfHg9 > div > div > a._65Bje.coreSpriteRightPaginationArrow"
good_escape='aria-label="いいね！"'

#<a class=" _65Bje  coreSpriteRightPaginationArrow" tabindex="0">次へ</a>
#いいねカウンター
likeCounter = 0
likeMax = 100

#いいねのPATH
LIKE_BOTTON = 'body > div._2dDPU.CkGkG > div.zZYga > div > article > div.eo2As > section.ltpMr.Slqrh > span.fr66n > button > div > span > svg'




#loginメソッド

browser.get(INSTA_URL)
time.sleep(5)
browser.find_element_by_xpath(LOGIN_PATH).click()
usernameField = browser.find_element_by_name('username')
usernameField.send_keys(username)
passwordField = browser.find_element_by_name('password')
passwordField.send_keys(user_passward)
time.sleep(5)
passwordField.send_keys(Keys.RETURN)


#tag検索メソッド

time.sleep(3)
encodedTag = urllib.parse.quote(tag_name) #普通にURLに日本語は入れられないので、エンコードする
encodedURL = TAG_SEARCH_URL.format(encodedTag)
print("encodedURL:{}".format(encodedURL))
browser.get(encodedURL)
print("")


#投稿をクリック
time.sleep(3)
browser.implicitly_wait(10)
browser.find_element_by_css_selector(MEDIA_SELECTER).click()

while likeCounter < likeMax:
    time.sleep(3)
    browser.find_element_by_css_selector(LIKE_BOTTON).click()
    likeCounter += 1
    print("liked {}".format(likeCounter))
    time.sleep(5)
    browser.find_element_by_css_selector(next_botton).click()
else :
    print("You liked {} media".format(likedCounter))
