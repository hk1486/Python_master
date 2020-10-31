# self

class Foo:
    
    def __init__(self,name = 'noname'):
        self.name = name
    
    def func1(self):
        print('func1')
        
    def setName(self,name):
        print('이름변경',self.name, '->', name )
        self.name = name
        
f1 = Foo()
f2 = Foo()

# id (객체)
# 인스턴스 고유 식별 번호(주소)
print(id(f1), id(f2)) 

print(id(f1) == id(f2)) # 다른 인스턴스다
print(type(f1) == type(f2)) # 타입은 같다

print(f1.name, f2.name)
f1.setName('john')
f2.setName('susan')
print(f1.name, f2.name)

#-----------------------------
# self
f1.setName('john')
# 실제론 아래처럼 호출됨.
Foo.setName(f1,'john' ) # self 값에 f1 전달

# 아래 두 코드는 동일한 동작을 하는 코드 
f2.setName('susan')
Foo.setName(f2, 'susan') # self 값에 f2 전달




















