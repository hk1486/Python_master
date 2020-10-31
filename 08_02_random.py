import random

# 실수
for i in range(10):    
    print(random.random()) # 0.0 <=  < 1.0 난수값 리턴

# 정수
for i in range(5):    
    print(random.randint(1, 10)) # 1 <=  <=  10 정수난수값 리턴
 
    
print('-'*30)    

# 중복되지않는 정수값 랜덤 추출
data = [1,2,3,4,5]

def random_pop(d):
    number = random.randint(0, len(d)-1)
    return d.pop(number)

while data:
    print(random_pop(data))
    
#----------------------
print('-'*30)    
# 연습
# 로또 번호 추출
# 1 ~ 45 까지의 숫자중 6개 랜덤 추출

data = [i + 1 for i in range(45)]

for i in range(6):
    print(random_pop(data))
    
#----------------------
print('-'*30)    
# random.shuffle()

data = ['dog','cat','bird']
print(data)
random.shuffle(data)  # 주어진 데이터를 섞는다
print('shuffle 후', data) 


# 로또 번호 추출 셔플 사용
print()
data = [ i +1 for i in range(45)]
random.shuffle(data)
print(data[:6]) 












