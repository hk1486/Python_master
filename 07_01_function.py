print('안녕하세요')
print('제 이름은 이무진 입니다')

print('안녕하세요')
print('제 이름은 홍인기 입니다')

print('안녕하세요')
print('제 이름은 홍희훈입니다' )

print('안녕하세요')
print('제 이름은 유진호입니다' )

print('-'*30)

#함수정의
def sayAnthem():
    print('동해물과 백두산이')
    print('마르고 닳도록')
    print('하느님이 보우하사')
    print('우리나라 만세')
    
#함수호출
sayAnthem()
sayAnthem()
sayAnthem()
sayAnthem()

#함수정의
#매개변수 지정
def sayName(name):
    print('안녕하세요')
    print('제 이름은 ',name,'입니다')
    
#함수호출
#sayName()  # 에러
sayName('이해강') # 매개변수를 필히 넣어줘야함
sayName('이봄')

#함수정의
def sayAge(age):
    print('제 나이는요...')
    print(age,'살 입니다')

#함수 호출    
sayAge(100)
sayAge(77)
sayAge(26)

#함수정의
#매개변수 여러개 가능
#함수가 다른 함수 호출 가능
def sayHello(name,age):
    print('-'*10)
    sayName(name) #호출
    sayAge(age) #호출
    print('-'*10)

#함수호출
sayHello('이해강',26)
# sayHello('이봄') <- 매개변수 에러 

# 함수 호출시 매개변수 명시 가능
sayHello(name = '토끼',age = 25)
sayHello(age=30,name='거북이') # <- 이름만 일치하면 거꾸로해도 가능

# return 
def codeEveryday():
    print('파이썬 열공')
    print('Life is short')
    print('You need Python')
    return 

codeEveryday()
print('종료')

print()

def codeEveryday():
    print('파이썬 열공')
    print('Life is short')
    return # <- return 만나면 함수 종료
    print('You need Python')
     

codeEveryday()
print('종료')

def sum(num1,num2):
    result = num1 + num2
    return result

a = sum(10,20)
print(a)






























