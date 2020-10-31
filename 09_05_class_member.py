# 클래스의 객체변수, 매소드들.. 클래스의 멤버라고 함
# 멤버변수, 멤버매소드...

# 클래스의 멤버(뱐수, 매소드)는 클래스 정의 후에도
# 추가, 삭제 가능!

class Myclass:
    
    count = 0
    
    def __init__(self,num):
        self.num = num
        
    def disp(self):
        print(Myclass.count, self.num)


m1 = Myclass(10)

# __dict__
print(m1.__dict__)

m1.disp()

m1.name = 'hong'    # 클래스 정의 후 멤버 (인스턴스 변수 )추가 가능

print(m1.__dict__)

print(Myclass.__dict__)

Myclass.addr = 'SEOUL'  # 클래스 정의 후에 멤버 ( 클래스 변수 )추가 가능
print(Myclass.__dict__)

del(Myclass.addr) # 멤버 삭제는 del
del(m1.num) # self.num 인스턴수 변수도 삭제 가능
# m1.disp() # self.num 값이 삭제되어 에러!

m2 = Myclass(100)
m3 = Myclass(200)

print(m2.__dict__)
print(m3.__dict__)

m2.age = 20
m3.addr = 'pusan'
del(m3.num)

print(m2.__dict__)
print(m3.__dict__)

