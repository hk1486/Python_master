# 함수작성 연습

# 반지름은 입력받아
# 원의 둘레를 계산하여 리턴하는 함수를 작성하세요

def calc_perimeter(radius):
    perimeter = 2 * 3.141592 * radius
    return perimeter

result = calc_perimeter(10)
print('둘레=',result)


# 반지름은 입력받아
# 원의 면적를 계산하여 리턴하는 함수를 작성하세요
# 정의, 호출 


def calc_area(radius):
    area = 3.141592 * (radius ** 2)
    return area

# print('면적 =', calc_area(10f))

# 직사각형 넓이 구하기
    
def calc_rect_area(width,height):
    return width*height
print('넓이=', calc_rect_area(10, 5))



# 직각삼각형의 '밑변'과 '높이'가 주어졌을때
# 빗변의 길이를 구하는 함수를 작성하세요
# 정의, 호출

def pitagoras(a,b):
    c = (a ** 2 + b ** 2) ** (1/2)
    return c

print('빗변의 길이는=',pitagoras(1, 1))








































































































