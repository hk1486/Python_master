# 순환문 (Loop)

# 특정 코드를 일정 회수 반복수행하는 경우 사용하는 구문
# 순환문(loop) 혹은 반복문(iteration) 이라고 한다

# 파이썬에는 while, for 구문이 순환문을 수행합니다

#------------------------
# while  순환문

# while 순환문 구조,  조건문이 '참' 인 동안 수행문장을 반복수행

# while <조건문>:
#     <수행할 문장1>
#     <수행할 문장2>
#     <수행할 문장3>
#     ...
# else:
#      순환문 빠져나오기 전에 수행

num = 0
while num < 10:
    print(num, end = ',')
    num += 1 

print('while 종료 후 num=',num)


# 순환문에서 중요한 것은
# 1. 몇번 순환을 하는가?
# 2. 순환하는 동안 변수값의 변화 범위는?
# 3. 순환문 종료후 변수값은?

# 위 순환문의 경우
# 1. 총 10번 순환을 했고
# 2. 순환하는 동안 num 변수값은 0 부터 9 까지 변화
# 3. 순환문 종료후 num 값은 10

i , j = 0 ,10
while i < j:
    print("i값은",i,"j값은",j)
    i += 2
    j -= 1
    
print("while 종료 후  i=",i,",j=",j)

print("-" * 20)


"""
2 x 1 = 2

2 x 2 = 4

2 x 3 = 6

2 x 4 = 8

2 x 5 = 10

2 x 6 = 12

2 x 7 = 14

2 x 8 = 16

2 x 9 = 18

"""

n = 1
while n <= 9 :
    print("2 x",n,"=",2*n)
    n += 1
    
print("2단 출력 종료")

# 증감식이나 종료조건이 없으면 무한루프에 빠지게 됨.







































