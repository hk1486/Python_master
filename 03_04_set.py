# set
# 만드는 방법
# 1.set()  함수로 만들수도 있고
# 2. {  } 으로 만들수도 있다.

#1. list   :  순서있다.  중복허용,  mutable
#2. tuple  :  순서있다,  중복허용,  immutable
#3. set : 순서없다,  중복허용안함
#4. dict : key, value 쌍으로 구성, 순서없다.

a = ""  # 빈 스트링
a = []  # 빈 리스트
a = ()  # 빈 튜플
a = {}  # 빈 딕셔너리

animals = {'dog','dog','cat','bird'}
print(animals)  # {'dog', 'bird', 'cat'} 순서없고 중복허용 x
print(len(animals))
print(type(animals))    # <class 'set'>
# print(animals[0]) 순서가 없으므로 인덱스 사용불가

myList = [10,20,30,40,20,30,10]
print(myList)

# 위 리스트에서 중복된 데이터 제거하고 싶다면??
print(list(set(myList)))    # set으로 만들고 list로 다시 바꿈



