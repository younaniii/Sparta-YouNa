# Server의 기능
    # 그림파일(html, css, js), data 를 준다!
# Django: 규모가 큰 서버에 많이 쓰임. 전체적인 큰 service 제공 용도로 많이 쓰임. 따라서 learning curve가 높은 편.
# Flask: 간단한 기능이 많음. API, product를 만들 때 많이 쓰이며, 큰 서비스를 제공하기에는 어려움이 있음. Microservice 제공 용도로 많이 씀.

# render_template: html을 불러오기 위해 필요한 기능
    # static folder: js
    # templates folder: html, css
from flask import Flask, render_template, jsonify, request
# server code: __name__
app = Flask(__name__)

# host(e.g. www.naver.com)의 각 방에 대한 정의를 내려주는 약속
# GET 방식(method) --> default 임. 따라서, @app 작성할 때 명확하게 나타내기 위해 , methods를 명시해 주는 습관을 들이자.

## HTML을 주는 부분
@app.route('/', methods=['GET'])
# e.g. www.naver.com/ --> 이건 홈페이지야!
def home():
    return render_template('index.html')

## API 역할을 하는 부분
@app.route('/test', methods=['POST'])
def test_post():
    # request로 프론트엔드 개발자가 던져주는 데이터(dictionary 형태)를 받는다.
    # POST - form: dictionary 내 데이터 중, key에 맞는 value를 꺼내와서 title_receive에 넣어 준다.
   title_receive = request.form['title_give']
   print(title_receive)
    # Json화 시켜서 프론트엔드 개발자에게 예쁘게 정제된 형태의 데이터를 돌려준다.
   return jsonify({'result':'success', 'msg': '이 요청은 POST!'})

@app.route('/test', methods=['GET'])
def test_get():
    # request로 프론트엔드 개발자가 던져주는 데이터(key 값)를 받는다.
    # GET - args.get
   title_receive = request.args.get('title_give')
   print(title_receive)
   return jsonify({'result':'success', 'msg': '이 요청은 GET!'})


# 서버가 시작되는 부분
if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
    # OS에 따라서 셋 중에 작동하는 하나를 쓰면 됨: localhost = '0.0.0.0' = 127.0.0.1
    # port: '방'. Flask 서버에서 사용할 '방'을 지정하는 것. Flask는 내가 설치한 서버이기 때문에, 포트 넘버는 내가 임의로 지정할 수 있다.
        # http: 80. https: 443
    # debug