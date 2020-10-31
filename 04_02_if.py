# 조건문, 반복문에 대해 작용
# 조건문 (if ~ elif ~ else)

# if 조건식:
#    참일때 수행 구문 블록  (블록이란 문장들의 집합)


# if 조건식:
#    참일때 수행 구문 블록
# else:
#    거짓일때 수행 구문 블록


# if 조건식1:
#    조건식1 참일때 수행 구문 블록
# elif 조건식2:
#    조건식2 참일때 수행 구문 블록
# elif 조건식3:
#    조건식3 참일때 수행 구문 블록
# else:
#    어떤 조건식도 거짓일때 수행 구문 블록


# 각 블록은 반드시 동일한 인덴트로 작성되어야 한다

# 조건식에는 비교연산자와 논리연산자 등을 잘 활용해야 한다
# 비교연산자 <, >, ==, !=, >=, <=
# 논리연산자 and, or, not

###################################
a = 1

if a>0:
    print('변수 a 값은',a)
    print('a는 양수입니다.')
    
    
    
print('종료')

print('-' * 20)

####################################
print('if - else')

print('짝수 혹은 홀수')

a = 9

if a % 2 == 0 :
    print('a값은',a)
    print('짝수입니다')
else:
    print(a,'는 홀수입니다')

print('-종료-')

print('-' * 20)

#####################################
print('음수 , 0 , 양수 구분하기')
a = -2

if a > 0:
    print('양수입니다')
elif a == 0:
    print('0입니다')
else:
    print('음수입니다')
    
print('종료')

print('-' * 20)

######################################

# 조건식에 사용가능한 비교연산자, 논리연산자
# 비교연산자 : >, >=, <, <=, !=, ==
# 논리연산자 : and, or, not, ^ (xor)
# 위 연산자들의 결과값은 항상 True / False

d = 10

data = d > 2    # T
data = d > 10   # F
data = d <= 100 # T
data = d <= 10  # T
data = d == 100/10 # T 
data = d != 10  # F

# and : 양쪽 모두 참일때만 결과가 참
# or : 한쪽만 참이어도 결과가 참
# not : 결과를 뒤짚기, 반대로
# xor : 같으면 F, 다르면 T

data = True and True # T
data = True and False # F
data = True or False # T
data = False or False # F
data = not True # F
data = True ^ True # F
data = False ^ False # F
data = True ^ False # T

data = d % 2 == 0 and d % 3 == 0    # F
data = d % 2 == 0 or d % 3 == 0     # T
data = (d % 2 == 0) ^ (d % 3 == 0)  # T
data = not d % 2 == 0               # F

if data:
    print(data,'참입니다')
else:
    print(data,'거짓입니다')
    
print('-' * 20)

print('주어진 숫자가 0<=     <=100 범위인가')

num1 = 105

if 0 <= num1 and num1 <= 100:
    print('유효한 정수 입니다')
else:
    print('이것은 올바른 정수가 아닙니다')
    
# 파이썬에서는 아래와 같이 범위값 표현가능
    
if 0 <= num1 <= 100:
    print('이것은 올바른 정수입니다')
else:
    print('이것은 올바른 정수가 아닙니다')
    
    
if 'py' in 'python':
    print('py를 찾았습니다')
else:
    print('py가 없습니다.')
    



















    



        











































