from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver
import time

# https://www.instagram.com/explore/tags/%EB%9E%9C%EC%84%A0%EC%97%AC%ED%96%89/

baseUrl = 'https://www.instagram.com/explore/tags/'
plusUrl = input('어디로 떠나고 싶나요? ')
url = baseUrl + quote_plus(plusUrl)

print(url)

driver = webdriver.Chrome()
driver.get(url)

time.sleep(3)

html = driver.page_source
soup = BeautifulSoup(html)

#'insta'라는 태그 안에 bs4를 사용하여 인스타그램에서 찾은 사진의 class를 가져온다.
insta = soup.select('.v1Nh3.kIKUG._bz0w')

#사진의 주소를 가져오고(href), 앞에 인스타그램 주소를 문자열로 붙여서 완전한 링크로 가져온다.
n = 1
for i in insta:
    print('https://www.instagram.com' + i.a['href'])
    #사진을 포함한 class를 하나 찍고 > 그 클래스의 img 태그에 들어잇는 src를 가져온다.
    imgUrl = i.select_one('.KL4Bh').img['src']
    #미리 지정한 폴더에 가져온 사진을 저장한다.
    with urlopen(imgUrl) as f:
        with open('./IG_Images/' + plusUrl + str(n) + '.jpg', 'wb') as h:
            img = f.read()
            h.write(img)
    n += 1
    print(imgUrl)
    print()

driver.close()
