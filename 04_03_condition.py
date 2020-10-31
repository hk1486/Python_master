# 조건식의 참 / 거짓 판정 

# 조건문,  순환문 등에 사용되는  '조건식' 은 참, 거짓이 판정되어야 하는데
# 파이썬에서는 bool 타입 외에도 조건식에서 참, 거짓 판정이 된다.

#           │     참     │   거짓
# ───────────────────
# bool 타입 :     True         False
# 숫자 타입 :  0 아닌 숫자      0
# str  타입 :      "abc"        ""   빈문자열
# list 타입 :    [1, 2, 3]      []
# tuple 타입 :   (1, 2, 3)      ()
# dic 타입 :    {"name":"john"}    {}

# None 타입 :   무조건 거짓

data = 100  # T
data = 0    # F
data = 'Python' # T
data = ""   # F
data = " "   # T : 공백도 문자다!
data = [1,2,3]  # T
data = []   # F
data = ()   # F
data = {}   # F
data = None   # F


if data:
    print(type(data),data,'참입니다')
else:
    print(type(data),data,'거짓입니다')


print('-' * 20)
######################################

#논리 연산자 and, or 표현식과의 관계
#참, 거짓 판정에 이어 논리연산자의 결과는 
# expression 값 short-circuit evalutation, 
# lazy evalutation 

print('SCE: short-circuit evalutation')
# or
# 왼쪽이 참인경우 왼쪽 값 리턴
# 왼쪽이 거짓이면 오른쪽 값 리턴

data = True or False    # T (왼쪽값)
data = False or True    # T (오른쪽값)

# and
# 왼쪽이 참인경우 오른쪽 값 리턴
# 왼쪽이 거짓이면 왼쪽 값 리턴

data = True and False # F (오른쪽값)
data = False and True # F (왼쪽값)

data = 0 or 100 # 100
data = 'Hello' or 'Python' # Hello
data = 'Hello' and 'Python' # Python
data = [] and 'Python' # []


if data:
    print(type(data),data,'참입니다')
else:
    print(type(data),data,'거짓입니다')
    
    
n = 5
(n % 5 == 0)  and print(n,'은 5의 배수입니다')
(n % 5 == 0)  or print(n,'은 5의 배수가 아닙니다')

print('-' * 20)

#######################################
# in, not in
# 파이썬 언어에서의 독특한 조건식
#    in               not in
#  x in 문자열    x not in 문자열
#  x in 리스트    x not in 리스트
#  x in 튜플      x not in 튜플
#  x in 세트      x not in 세트
#  x in 딕셔너리  x not in 딕셔너리      <-- key 값의 존재 유무

# 타입 확인 연산자 is
a = 3.14
a = "py"
a = 10

print(type(a))

if type(a) is int:
    print("int 타입이다")
else:
    print('int 타입이 아니다')
    
# pass 키워드
# 아무일도 하지않는 블록에 꼭! 지정
    
if 'a' in ['a','b','c','d']:
    pass # 아무것도 없는 블록을 만드려면 반드시!! pass! 명시
else:
    print('없습니다')






















