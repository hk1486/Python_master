# for 순환문
# 기존의 다른 프로그래밍 언어의 for 문에 비해 파이썬은 매우 직관적이고 사용하기 편리

# for 문 기본 구조]
# for 변수 in 리스트(또는 세트, 튜플, 문자열, 딕셔너리, iterable):
#     수행할 문장1
#     수행할 문장2
#     ....
# else:
#      순환문 빠져나오기 전에 수행

# for 에 올수 있는 반복 범위는 다음과 같은 것들이 있다  --> iterable
# 숫자 (3), str, list, set, tuple, dict 

# 숫자로 반복하는 경우
for i in range(3):  # range(3) => 0, 1, 2
    print("Hello world",i)
print()

for i in range(5,8):    #5부터 8전까지
    print('Hello world',i) 
print()

for i in range(4,15,3): #3씩 증가
    print('Hello world',i)
print()

for i in range(10,0, -2):
    print('Hello world',i)
    
print("*" * 30)

animals = ['dog','cat','bird','bear','tiger']

for x in animals :
    print(x)
print()

for x in (1,2,3):
    print('x=',x)
print()

for ch in 'Helld': print(ch)
# 블럭에서 수행할 문장이 하나면 블럭 우측에 붙여도 된다.
print()

myDic = {'name':'Hong','age':'14'}  # 키값이 나옴
for key in myDic:
    print(key, ':',myDic[key])
print()































