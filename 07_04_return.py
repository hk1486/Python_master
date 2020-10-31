# 파이썬 함수는 여러개의 값을 리턴할수 있다??

# 결론적으로 말하자면 함수의 리턴 값은 오직 '하나' 다
# 그런데 파이썬에선 여러개의 값도 리턴이 가능했다!  어떻게 가능?  tuple 로 리턴하면 가능하다.
# 기술적으로는 tuple 하나 만 리턴했지만, tuple 안에 값이 여러개 있기 때문에
# 여러개의 값을 리턴한것과 같은 효과를 보는것이다


def sum_and_mul(a,b):
    return a+b , a*b   # 두개의 값을 담은 하나의 튜플을 리턴한것!
a = sum_and_mul(10,20)
print(a,type(a))
print(a[0],a[1])


s,m=sum_and_mul(10,20)
print(s,m)

#리턴값을 튜플로 하는 기본함수(내장함수)도 많다
result = divmod(10, 3) # 몫과 나머지를 리턴
print(result)

# 반지름은 입력받아
# 원의 '둘레'와 '면적'을 계산하여 리턴하는 함수를 작성하세요
# 정의, 호출 

import math
print(math.pi)   # 원주율 값

def calc_circle(radius):
    perimeter = 2 * math.pi * radius
    area = math.pi*(radius ** 2)
    return perimeter, area

p,a = calc_circle(10)
print(p,a)




































