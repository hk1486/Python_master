# for 와 tuple

a = [(1,2),(3,4),(5,6)]

print(len(a))

# x에 tuple 이 담기는 경우
for x in a:
    print(x)
    
print()

for x in a:
    print(x[0],x[1])
    
print('*' * 30)
print()

# 파이썬다운 방법
    
for x,y in a:
    print(x,y)
    
# 예제 연습
# 학생들의 점수가 아래와 같이 주어졌다고 하자
# 총점과 평균을 출력해보세요
# 예시)
# 학생수: 5 명
# 총점: 327 점
# 평균: 65.4 점

total = 0
avg = 0.0
scores = [88, 34, 98, 74, 33]  

for x in scores:
    total = total + x
     
print("학생수:",len(scores),'명')
print("총점:",total,'점')
print('평균:',total / len(scores),'점')


print('*' * 30)

#for와 dic

student = {
    'name':'홍반장',
    'email':'@naver.com',
    'address':'역삼역'
    }

for key in student:
    print(key,':',student[key])
print()

# dict.items()
# k-v 쌍을 tuple로 iterate 한다.
# [('name','홍반장'),('email','@naver.com'),('address','역삼역')]

for key, value in student.items():
    print(key,":",value)
























