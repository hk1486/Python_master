# 파이썬의 한줄 주석 (line comment)
# 프로그램의 실행과는 관계없음, 메모등을 남기는용도
# 적절한 주석을 남기는 것은 좋은 프로그래밍의 습관!^^

# 파이썬의 기본출력
# 숫자 (정수,실수)
# 소숫점이 없으면 정수 (int : integer)
# 소숫점이 있으면 실수 (float)

print (10)
print (10.0)
print (10.)  # 10.0
print (.1)   # 0.1

print (4*5)     # 20, '정수'와 '정수' 사이에 연산 결과는 '정수'입니다.
print (4*5.0)   # 20.0, '실수'와 연산결과는 '실수'입니다.
print (4/2)     # 2.0, 나눗셈의 연산 결과는 언제나 '실수'입니다. 

# 나눗셈 후 소숫점 이하 버리는 연산자 '//'
print(4//2)      # 2, 소숫점 이하는 버려버림.
print(4//2.0)    # 2.0, '실수'와의 연산결과는 '실수'입니다.
print(3.4//1.1)  # 3.0, 결과는 '실수'지만 소숫점 이하는 버려버린다.
# print(5/0)     # 0으로는 나누지 못함. "ZeroDivisionError" 
print("이건 실행이 될까요..?") # 에러난 이후로는 실행불가.

# 나머지 연산자 %
print(13%3)      # 1
print(12.5%4.1)  # 0.200000
# 프로그래밍에서 '실수' 계산은 언제나 오차가 존재할 수 있음, 무한히 많은 소숫점 표현불가.

# 제곱 연산자 **
print(2**4)      # 16
print(-3**3)     # -27
print(3**-3)     # 0.037037037037037035
print(10**-2)    # 0.01
print(2**(1/2))  # 1.4142135623730951(제곱해서 2가되는 수)
print(27**(1/3)) # 3

# 블록 주석 (block comment)
""" (쌍따옴표 3개)
이 안의 내용은 주석으로 처리됩니다.
"""

# 문자열 str (string)
""" 문자열 만드는 방법
1. 쌍따옴표
2. 홀따옴표
3. 쌍따옴표3개
4. 홀따옴표 3개 """
print("Life is short, You need Python")
print('Life is short, You need Python')
print("""Life is short, You need Python""")
print('''Life is short, You need Python''')

print("She's gone")
print('He says "Hi!"')
print('''He says "It's OK!" ''')

# 문자열 연산자 +
print("Hello" + "Python")   # 문자열 연결 연산
print("Hello" + " " + "Anaconda")   
# print(12 + "monkeys")       # 숫자와 문자열은 덧셈연산 불가능.

# 문자열 연산자 *
print("-" * 20)

# 문자열의 길이 Length (문자열 안의 문자개수)
# Len(문자열)
print(len("파이썬"))   # 3글자
print(len("Hello Python"))  # 공백포함 12글자

# type() 함수(명령)
print(type(10))    # 'int'
print(type(10.0))   # 'float'
print(type("10.0")) # 'str'

# bool 타입 (참 혹은 거짓, 'true' or 'false')
print(True)
print(False)
print(type(True))   # 'bool'

