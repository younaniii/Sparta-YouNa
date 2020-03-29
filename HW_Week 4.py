from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

@app.route('/')
def home():
    return render_template('HW_Week 4.html')

# 주문하기: POST - 주문 정보 입력 후 '주문하기' 클릭 시 주문 목록에 추가되어야 함
@app.route('/orders', methods=['POST'])
def make_order():
    orderAmount_receive = request.form['orderAmount_give']
    clientName_receive = request.form['clientName_give']
    clientContact_receive = request.form['clientContact_give']
    clientAddress_receive = request.form['clientAddress_give']

    order = {
        'orderAmount': orderAmount_receive,
        'clientName' : clientName_receive,
        'clientContact' : clientContact_receive,
        'clientAddress' : clientAddress_receive
    }

    db.orders.insert_one(order)
    return jsonify({'result':'success', 'msg': '주문정보를 성공적으로 저장했습니다.'})


# 주문내역 보기: GET - 하단 주문 목록이 자동으로 보여야 함
@app.route('/orders', methods=['GET'])
def review_orders():
    orders = list(db.orders.find({},{'_id':0}))
    return jsonify({'result':'success', 'orders':orders})


if __name__ == '__main__':
    app.run('0.0.0.0', port=3000, debug=True)