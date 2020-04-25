from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.PP_BangguseokTravel

## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('PP_BGSTravel_Home.html')

@app.route('/home', methods = ['GET'])
def listing():
    # 1. 모든 document 찾기 & _id 값은 출력에서 제외하기
    result = list(db.bucketlist.find({}))

    # 2. articles라는 키 값으로 포스트정보 내려주기
    return jsonify({'result':'success',
                    'msg':'저장한 포스트를 가져왔습니다:)',
                    'bucketlist':result})

## API 역할을 하는 부분
@app.route('/home', methods = ['POST'])
def saving():
    # 1. 클라이언트로부터 데이터를 받기
    url = request.form['url_give']
    comment = request.form['comment_give']

    print(url)

    # 2. meta tag를 스크래핑하기
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(url, headers=headers)
    soup + BeautifulSoup(data.text, 'html.parser')

    #이 부분 어떻게 채워넣지?

    bucketlist = {'keyword':keyword, 'image':image}

    print(bucketlist)

    # 3. mongoDB에 데이터 넣기
    db.bucketlist.insert_one(bucketlist)

    return jsonify({'result':'success', 'msg':'버킷리스트를 추가했습니다:D'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)

