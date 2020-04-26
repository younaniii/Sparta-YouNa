from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import time

# pymongo를 임포트 하기(패키지 인스톨 먼저)
from pymongo import MongoClient
# mongoDB는 27017 포트로 돌아갑니다.
client = MongoClient('localhost', 27017)
# 'BangguseokTravel'라는 이름의 db를 만듭니다.
db = client.BangguseokTravel


# Home HTML을 주는 부분
@app.route('/')
def home():
    return render_template('PP_BGSTravel_Home.html')

@app.route('/mybucketlist')
def mybucketlist():
    return render_template('PP_BGSTravel_MyBucketlist.html')


# Crawling으로 인스타그램에서 사진을 가져오는 부분
# API를 사용하자!

# API 역할을 하는 부분: 마음에 드는 포스트를 저장하는 부분
@app.route('/home', methods = ['POST'])
def saving():
    # 1. 클라이언트로부터 데이터를 받기
    url = request.form['url_give']
    image = request.form['image_give']
    continent = request.form['continent_give']
    country = request.form['country_give']
    city = request.form['city_give']
    comment = request.form['comment_give']

    print(url)

    # 2. meta tag를 스크래핑하기
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(url, headers=headers)
    soup + BeautifulSoup(data.text, 'html.parser')

    #이 부분 어떻게 채워넣지?

    bucketlist = {'url':url, 'image':image, 'continent':continent, 'country':country, 'city':city, 'comment':comment}

    print(bucketlist)

    # 3. mongoDB에 데이터 넣기
    db.bucketlist.insert_one(bucketlist)

    return jsonify({'result':'success', 'msg':'버킷리스트를 추가했습니다:D'})


# 내가 저장한 포스트를 불러오는 부분
@app.route('/home', methods = ['GET'])
def listing():
    # 1. 모든 document 찾기 & _id 값은 출력에서 제외하기
    result = list(db.bucketlist.find({}))

    # 2. articles라는 키 값으로 포스트정보 내려주기
    return jsonify({'result':'success',
                    'msg':'저장한 포스트를 가져왔습니다:)',
                    'bucketlist':result})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)

