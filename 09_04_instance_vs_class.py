# 클래스 매소드 vs 인스턴스 매소드
# 클래스 변수 vs 인스턴스 변수

#------------------------------
print("클래스 매소드 vs 인스턴스 매소드")

class Foo:
    # 클래스 매소드
    # self 가 안붙은 매소드, 클래스 이름으로 사용
    def func1():    
        print('function1')
        
    # 인스턴스 매소드    
    # self가 붙은 매소드, 인스턴스 생성하여 사용
    def func2(self):
        print('function2')
        

f1 = Foo()  # f1은 Foo 인스턴스
# f1.func1()  # 에러(self가 빠져서)
f1.func2()  # 인스턴스 사용하여 인스턴스 매소드인 func2() 호출

Foo.func1() # 클래스 매소드는 클래스 이름으로 호출

print('-' *30)
#------------------------------
print('클래스 변수 vs 인스턴스 변수')
# self.변수이름 : <-- 인스턴스 변수
#   인스턴스 변수는 인스턴스 마다 생성
#
# 클래스 내부에서 선언된변수 <-- 클래스 변수 (self가 안붙음)
# 사용하려면 클래스이름.변수이름 으로 사용해야 함
#       클래스 변수는 클래스에 딱 하나 생성

# 계좌 객체 정의
class Account:
    
    num_accounts = 0    # 클래스 변수
    
    def __init__(self,name):    # 생성자
        print("Account({}) 생성".format(name))
        self.name = name #  self.name 인스턴스 변수
        Account.num_accounts += 1 
        
    def __del__(self):  # 소멸자
        print("Account({}) 소멸".format(self.name))
        Account.num_accounts -= 1 

print('Account.num_accounts = ',Account.num_accounts)
acc1 = Account('회사')
acc2 = Account('홍길동')
acc3 = Account('아이언맨')
print('Account.num_accounts = ',Account.num_accounts)

# 인스턴스 삭제는???
del(acc1) # 삭제됨.
print('Account.num_accounts = ',Account.num_accounts)





