# 정사각형(Square)
# |_ 정육면체(Cube)

# '정사각형' 객체 정의 
#  클래스 이름 : Square
#  생성자 : '한 면의 길이(side)'를 받아서 초기화
#  면적을 계산하여 리턴하는 메소드 : getArea()

# '정육면체' 객체 정의 <-- Square 상속받아 정의
#  클래스 이름 : Cube
#  getArea() : 정육면체의 총 면적 (한면 곱하기 6)
#  getVolume() : 정육면체의 부피 게산 (한면의 길이의 세제곱)


import math

class Square:
    
    def __init__(self,side):
        self.side = side
        
    def getArea(self):
        return self.side ** 2
    
    # 상속
class Cube(Square):
    
    # 오버라이딩
    def getArea(self):
        return (self.side ** 2) * 6
    
    # 추가되는 매소드
    def getVolume(self):
        return self.side ** 3
    
s1 = Square(4)
print(s1.getArea())
c1 = Cube(4)
print(c1.getArea())
print(c1.getVolume())

print(Cube.__dict__)







































