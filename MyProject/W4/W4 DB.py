# Python에서는 패키지 이름이 그대로 파일명으로 reserved되어 있기 때문에, 파일 생성 시 이름을 패키지 명으로 하지 않는 것이 중요하다!

# RDBMS(SQL): 행/열의 생김새가 정해진 엑셀에 데이터를 저장하는 것과 유사합니다.
# 데이터 50만 개가 적재된 상태에서, 갑자기 중간에 열을 하나 더하기는 어려울 것입니다. 그러나, 정형화되어 있는 만큼, 데이터의 일관성이나 / 분석에 용이할 수 있습니다.
# ex) MS-SQL, My-SQL 등

# No-SQL: 딕셔너리 형태로 데이터를 저장해두는 DB입니다. 고로 데이터 하나 하나 마다 같은 값들을 가질 필요가 없게 됩니다. 자유로운 형태의 데이터 적재에 유리한 대신, 일관성이 부족할 수 있습니다.
# 세션, 쿠키 등 일시적으로만 필요한 가벼운 데이터 저장에 사용됨.
# ex) MongoDB --> SQL과 달리 순서대로 데이터를 찾지 않고 바로 찾아내기 때문에 속도가 빠르다. 대신, 한번 더 생각하고 코드를 짜야 하는 단점이 있음.


from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)

client = MongoClient('localhost', 27017)  # localhost-> 나중에 IP No. 생성 후 대체. mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta  # 내 서버에 'dbsparta'라는 이름의 db가 있으면 가져오고, 아니면 만들라는 명령.

# MongoDB에 insert 하기
# 'users'라는 collection에 {'name':'bobby','age':21}를 넣습니다.
# 나는 'users'라는 collection을 생성한 적이 없으므로, 이 명령어로 인해 새로운 dictionary가 만들어 질 것임!
db.users.insert_one({'name': 'bobby', 'age': 21})
db.users.insert_one({'name': 'kay', 'age': 27})
db.users.insert_one({'name': 'john', 'age': 30})
# db.users.insert_many([]) --> list 형태로 넣어야 하며, 여러개를 한 번에 추가할 수 잇음


# MongoDB에서 데이터 모두 보기
# db 안의 데이터를 모두 가져오되(.find()), list 형태로 가져와라!
all_users = list(db.users.find())

# 참고) MongoDB에서 특정 조건의 데이터 모두 보기
# key & value를 지정해서 특정 조건의 데이터를 list 형태로 가져와라!
same_ages = list(db.users.find({'age': 21}))
# 예약어를 알고 있어야 하는 단점이 있다 --> 이상 gte, 이하 lte, 초과 gt, 미만 lt
same_ages = list(db.users.find({'age': 21}))

print(all_users[0])  # 0번째 결과값을 보기
print(all_users[0]['name'])  # 0번째 결과값의 'name'을 보기

for user in all_users:  # 반복문을 돌며 모든 결과값을 보기
    print(user)

# 가져올 결과값이 명확하게 하나만(.find_one({:}) 있을 때!
user = db.users.find_one({'name':'bobby'})
print (user)


# mongoDB에서는 모든 데이터에 대해서 고유값(id)를 부여함.
# 예를 들면, 엑셀 파일의 여러 Sheet에서 연쇄적으로 연결되어 있는 동일한 데이터 구조와 같은 개념!
# 그 중 특정 키 값을 빼고 보기 --> mongoDB 내 고유 id 값은 빼고 가져와라!
user = db.users.find_one({'name':'bobby'},{'_id':0})
print (user)


# 수정하기 - 생김새
# db.people.update_many(찾을 조건, {'$set': 어떻게 바꿀지})
# 'one'이 들어가 있는 함수는 가장 위에 있는 데이터에 적용이 됨.
# 예를 들어, bobby라는 이름의 사람이 여러 명일 때 아래 코드를 돌리면, 맨 위에 있는 bobby에만 update가 적용됨.
db.users.update_one({'name': 'bobby'}, {'$set': {'age': 19}})

user = db.users.find_one({'name': 'bobby'})
print(user)


# 삭제하기 - 거의 안 씀. 데이터를 완전히 삭제하는 대신, 서비스 측면에서는 '3개월 후 재가입 가능'과 같은 active/inactive 형태로 처리함.
db.users.delete_one({'name':'bobby'})

user = db.users.find_one({'name':'bobby'})
print (user)