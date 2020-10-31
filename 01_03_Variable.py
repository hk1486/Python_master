""" print(100)
 print(200)
 print(300)
print(400)
print(500)
print(600)"""
# 'IndentationError', 파이썬은 들여쓰기 열을 맞춰야함

# 변수 (Variable): 데이터를 담아두는 공간
# '변수이름'을 붙여 담아둔다. 데이터는 언제든지 변경 가능

# 변수 사용법
# 변수이름 = 값

# = : 대입 연산자를 사용하여 변수에 값을 저장.
# 변수에 어떠한 타입의 어떠한 값이 담겨있는지 놓치면 안됨!! ★ 
# 변수이름은 대소문자 구별함.

a = 10   # a라는 변수선언후 정수값 10을 대입한다.
print("a 값은",a,"입니다.")
b=5
print(a+b)
print(a,"+",b,"=",a+b)  # ,(콤마) 사용시 문자 중간에 띄어쓰기 들어감
# print(c)    # NameError, 선언한적 없는 변수 사용불가

myName = "김만두"
print("제 이름은",myName,"입니다.")
print("제 이름은 "+myName+" 입니다.")

age = 10
print("제 나이는",age,"살 입니다.")
# print("제 나이는 "+age+" 살 입니다.")    # TypeError, 정수와 문자열 덧셈연산 불가.

# 형 변환 함수들
# 각 타입별로 형변환할 수 있는 함수
# int(), str(), float() ...
print(age,type(age))
print(str(age),type(str(age)))
print("제 나이는 "+str(age)+" 살 입니다.")  # int를 str로 형변환

num1 = "100"
print(int(num1) + 200)  # str을 int로 형변환
