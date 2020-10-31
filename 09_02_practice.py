# 연습 : 원에 대한 객체 정의

#  클래스 정의 Circle
#  객체변수는 반지름  (radius)

#  생성자 

#  원의 넓이 계산하여 리턴하는 메소드  getArea()
#  원의 둘레 계산하여 리턴하는 메소드  getPerimeter()

# 원주율은 3.141592 로 하자  (후에 math 모듈을 배우면 math.pi 로 사용하면 된다)


# 클래스 정의, 인스턴스 정의, 동작 시켜보기
import math

class Circle:
    
    def __init__(self,radius):
        self.radius = radius
        
    def getArea(self):
        area = math.pi * (self.radius ** 2)
        return area
        
    def getPerimeter(self):
        perimeter = 2 * math.pi * self.radius
        return perimeter


r1 = Circle(10)

print("넓이:",r1.getArea())
print("둘레:",r1.getPerimeter())

#------------------------------------------------------
# 연습 : 2차원 상의 좌표 객체 정의

#  클래스 정의 Point2D

#  객체변수는 x, y

#  생성자 

#  원점에서 부터 거리 계산 getDistance()

# 파이썬에서 root 구하는 함수는
# import math 후
# math.sqrt(x) 사용   혹은   x ** 0.5

class Point2D:
    
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def getDistance(self):
        return  ((self.x**2)+(self.y**2)) ** 0.5
        
p1 = Point2D(1, 2)
print(p1.getDistance())






