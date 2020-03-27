import requests
from bs4 import BeautifulSoup

# 타겟 URL을 읽어서 HTML를 받아온다.
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200309', headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
# 이제 코딩을 통해 필요한 부분을 추출하면 된다.
soup = BeautifulSoup(data.text, 'html.parser')

#movies = soup.select('#old_content > table > tbody > tr')

# movies (tr들) 의 반복문을 돌리기
#rank = 1
#for movie in movies:
    # movie 안에 a 가 있으면,
    #a_tag = movie.select_one('td.title > div > a')
    #if a_tag is not None:
    #   title = a_tag.text
    #   star = movie.select_one('td.point').text
    #   print(rank,title,star)
    #   rank += 1

# 여러개를 가져오고 싶은 경우
    # soup.select('태그명')
    # soup.select('.클래스명')
    # soup.select('#아이디명')
    # soup.select('상위태그명 > 하위태그명 > 하위태그명')
    # soup.select('상위태그명.클래스명 > 하위태그명.클래스명')
    # soup.select('태그명[속성="값"]')
# 한 개만 가져오고 싶은 경우
    # soup.select_one('위와 동일')

musicChart = soup.select('table.list-wrap > tbody > tr.list')
print(musicChart)

rank = 1
for song in musicChart:
    info = song.select_one('td.info > a')
    if info is not None:
        title = info.select_one('a.title ellipsis').text
        artist = info.select_one('a.artist ellipsis').text
        print(rank, title, artist)
        rank += 1
        
#.strip :공백을 지워주는 태그