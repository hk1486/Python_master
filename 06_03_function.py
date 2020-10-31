# 함수 (function)
# 프로그래밍에서 동일한(혹은 거의 비슷한) 내용의 코드가 반복될때가 있다.
# 바로 이러한 코드 낭비를 없애기 위해
# 반복되는 코드를 묶어서 하나의 함수로 정의해 놓고 사용하는 것이다

# 즉, 반복되는 부분이 있을 경우 "반복적으로 사용되는 가치 있는 부분"을 
# 한 뭉치로 묶어서 
# 1. 어떤 입력값( 매개변수 )을 주었을 때
# 2. 어떤 일을 수행하고, 
# 3. 어떤 결과값( 리턴값 )을 돌려준다"라는식의 
# 함수로 작성하는 것이 현명하다.
# --------------------------------------------------------------------


# 함수 만들기 (함수 정의 : Function Definition)

# def 키워드로 작성 

# def 함수이름( 매개변수 들):
#     함수 본체 <수행할 문장1>
#     함수 본체 <수행할 문장2>
#     ...

# 함수의 동작 정의
#   입력(매개변수) -> 본체 수행 -> 결과(리턴)

# 함수이름은 변수 이름 작성과 거의 동일한 규칙
# ------------------------------------------------------------------------

# 함수호출 Functioncall, invoke
# 함수호출시 넘겨지는 인자(parameter) 값들은
# 함수의 매개변수(argument)들이 받습니다.
# 매개변수는 0개, 한개, 여러개 있을수 있을수 있습니다

# 함수에는 리턴값이 있다.
# 리턴값은 함수를 호출(call) 한쪽에 돌려준다
# return 키워드로 리턴값을
# 함수 본체 수행중 return 을 만나면 함수를 종료 하게 됩니다
# 어떠한 타입도 리턴할수 있다.
# 리턴값은 없을수도 있다.
# -------------------------------------------------------------------

# 함수정의 예
# 입력: 두개의 숫자를 입력받아서  (매개변수)
# 수행: 덧셈을 수행한뒤
# 결과: 덧셈 결과를 리턴 

def add(a, b):
    result = a + b
    return result

# 함수 사용 (함수 호출 : Function call)
# 함수 이름(인자값들...)  * 인자값 : 매개변수에 넘겨줄 값들

result = add(10,20)  # add함수 호출, 매개변수에 10,20 넘겨줌
print('result=',result)
print('result=',add(100,400))

result = add(10+20,add(30,40))
print('result=',result)

print('-'*30)

def sayName(name):
    print("안녕하세요")
    print('제 이름은 ',name,'입니다.')
    # return 값이 없는 경우, 끝에 자동으로 return하게 된다.
    # return None
    
sayName("김만기")
sayName('이주영')
sayName('마이클')

print()

def sayAge(age):
    print('제 나이는요...')
    print(age,'살 입니다')
    
sayAge(100)
sayAge(30)
sayAge(77)

# 함수가 함수를 호출할 수 있다.
def sayHello(name,age):
    print('--'*10)
    sayName(name)
    sayAge(age)
    print('--'*10)
    
sayHello('김오영',24)
sayHello('한병인',48)

# 함수 호출 시 매개변수 명시 가능!
# 순서 바꿔도 동작 한다!
sayHello(name = '정승희',age = 25)
sayHello(age = 25,name = '정승희')

# return 값
# -- 함수종료
# -- 호출한쪽으로 값을 돌려준다.

print(sayHello(age = 25,name = '정승희')) 
 # None 리턴

filter_list = ['바보','멍청이']

def say_nick(nick):
    if nick in filter_list:
        return # 함수종료
    print('나의 별명은 %s 입니다'%nick)
    
say_nick('아이언맨')
say_nick('바보')
say_nick('토르')
























