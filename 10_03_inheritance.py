# 클래스의 상속 (Inheritance)
# 기존의 만들어진 클래스를 상속받아 새로운 클래스 정의 가능

# 상속받아 만들어진 클래스는 기존의 클래스의 메소드, 객체변수 를 그대로 가지고 있다.
# 상속받은뒤, 새로운 객체변수, 메소드 추가 할수 있다.
# 상속받은뒤, 상속받은 메소드 재정의 가능 (오버라이딩)

# 상속의 장점: 
#    기존의 코드를 다시 재작성 할 필요 없이. 새로이 변경 추가 되는 코드에만 집중할수 있기 때문에 생산성 향상

# 기존의 클래스 상속하여 새로운 클래스 정의하는 구문
#    class 새클래스명(기존의 클래스명)

# 기존의 클래스를 '부모클래스(parent class)' 라고 하고  (혹은 super class,  base class ...)
# 상속받은 클래스를 '자식클래스(child class) 라고 한다  (혹은 sub class, derived class ...)

#-------------------------------------
# 원

import math

class Circle:
    def __init__(self,radius=0):
        self.radius = radius
        
    def getArea(self):
        return math.pi * self.radius ** 2
    
    def getPerimeter(self):
        return 2 * math.pi * self.radius
    
    
c1 = Circle(10)
print(c1.getArea())
print(c1.getPerimeter())

# Circle 을 상속받아서 Sphere(구) 객체를 만들기
class Sphere(Circle):
     pass
 
# 기존의 Circle 변수, 매소드 사용 가능!
s1 = Sphere()
print(s1.__dict__)
s1 = Sphere(20)
print(s1.__dict__)

print(s1.getArea(), s1.getPerimeter())

# 상속 받은 뒤 새로 추가되는 매소드
# 부피 구하기!
class Sphere(Circle):
    # Sphere에서 추가되는 매소드
    def getVolume(self):
        return (4/3) * math.pi * self.radius ** 3

s2 = Sphere(4)
print(s2.getVolume())

# 매소드 오버라이딩 (overriding)
# 부모로부터 상속받은 매소드 재정의
print(Sphere.__dict__)
print(Circle.__dict__)

# '구' 와 '원'은 다르다
# 기존의 Circle 의 getArea() 를 재정의 (오버라이딩) 해주어야 한다

# 구의 겉넓이 공식  :  4 x pi x r ** 2

class Sphere(Circle):
    # Sphere에서 추가되는 매소드
    def getVolume(self):
        return (4/3) * math.pi * self.radius ** 3

    def getArea(self): # 매소드 오버라이딩
        return 4 * math.pi * self.radius ** 2
    
s3 = Sphere(4)
print(s3.getArea())

print(Sphere.__dict__)















