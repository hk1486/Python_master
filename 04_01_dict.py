# dict
# value는 어떠한 타입이라도 가능... 같은 값도 가능
# key : ...  hash 가능한 타입만 가능, 중복 값 불가
 
myDict = {
    1 : 'haha',
    'two' : 'haha',
    1 : 'hoho', # 키가 덮어써짐(키값은 절대 중복 불가)
    False : 'hehe',
    # [10,20,30] : 'haha' # TypeError: unhashable type, 집합데이터는 키 값으로 사용 불가
    }
print(myDict)   

myDict = {
    'name' : 'hong',
    'age' : 34,
    'height' : 175.6,
    'score' : [80,76,44],
    'family' : {
        'father' : '다스베이더',
        'mother' : '아미달라',
        'son' : '루크'
        },
    'items':[
        {
            'name' : '바지',
            'color' : '파랑'
            },
        {
            'name' : '양말',
            'color' : '레드'
            },
        {
            'name' : '모자',
            'color' : '노랑'
            },
        {
            'name' : '장갑',
            'color' : '블랙'
            }
        ]
    }
print(myDict)
print(myDict['score'])      # [80, 76, 44]
print(myDict['score'][1])   # 76
print(myDict['family']['son'])  # 루크
print(myDict['items'][1]['name'])   # 양말

print(len(myDict))      # 6

# dict 와 in 연산자
# 키 존재하는지의 여부
print('score' in myDict)    # True
print('email' in myDict)    # False
































