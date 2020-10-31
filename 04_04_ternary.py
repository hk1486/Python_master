# 10 + 2  # 피연산자 2개 필요 --> 이항연산자
# -10 ,  not True  # 피연산자 1개 필요 --> 단항연산자

# 피연산자 3개 필요 --> 삼항연산자 (ternary operator)
# ( 참일때의 값 ) if (조건식) else (거짓일때의 값)

n = -1
result = '양수' if n > 0 else '음수 or 0'
print(result)

a = 10
b = 20
bigger = a if a > b else b
print('큰 수는',bigger,'입니다')

a = 77
b = 88
diff = a - b if a > b else b - a
print('차이값은',diff) 



