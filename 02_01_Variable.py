#변수명규칙
# 알파벳, 숫자, _  등 사용 가능
# 숫자로는 시작할수 없다
# 변수명에 띄어쓰기 불가
# 특수문자 불가
# 파이썬의 예약어(reserved word)는 변수명으로 사용불가
#      and,  as,  assert,  break,  class,  continue,  def,  del,  elif,  else,  except,  is,  
#      finally,  for, from,  global,  if,  import,  in,  lambda,  nonlocal,  
#      not,  or,  pass,  raise,  return,  try,  while,  with, yield

# 가용한 변수
laptime = 10.2
abc2020 = 10
_value23 = 3.14
my_name = "hello"

# 불가능한 변수
""" 
55num = 33
%$@ = 44
my-name = "hello"
"""
# 여러개의 변수를 한줄에 선언 가능(세미콜론으로 구분)
a = 10; b = 20; c = 30
print(a,b,c)
# 파이썬 다운 방법: 한줄에 여러 변수 선언하기
a,b,c=100,200,300
print(a,b,c)

# 기존의 변수의 값을 일정량 증가, 감소...(변화)
a=10
# 기존의 a값에 1 증가
a=a+1
print("a=",a)
a=a*2
print("a=",a)
a=a-1
print("a=",a)
a=a/7
print("a=",a) #파이썬에서 나눗셈의 결과는 무조건 실수타입으로 출력

# 복합대입연산자
a,b,c = 100,10,7
a += 10  # a=a+10
b /= 2  # b=b/2
c %= 2  # c=c%2
print(a,b,c)

# 변수의 값을 서로 바꾸기
a=11; b=33
print(a,b)
# 일반적인 프로그래밍 언어 방법
temp=a
a=b
b=temp
print(a,b)
# 파이썬 다운 방법!
a, b = b, a
print(a,b)

# None 타입
# 아무 값도 타입도 없는 데이터
k = None # k 변수 존재, 값이 없음
print("k=", k, type(k))

# 변수삭제
del(a) # 변수 a 삭제
# print(a) 삭제 후 출력하면 에러남


