# print() 기본 출력(output) 함수

print(10)  # print() : 출력후 줄바꿈 발생
print(20)
print()
print(10, 20, 30)

# end 옵션 (parameter)
print("hello", end='----') # 줄바꿈 대신 end 문자 출력
print("Mike")
print(2020,end="-")
print(2,end="-")
print(14)

# 이스케이프 문자(escapde character)

# '문자열' 내에서 특수한 문자 출력할때 사용
# \와 조합하여 출력

# 많이 사용되는 이스케이프 코드 
#    \n : 줄바꿈
#    \t : 탭
#    \\ : 역슬래시
#    \' : 홀따옴표
#    \" : 쌍따옴표

# He says "I'm fine"  을 출력하려면?
print("He says \"I'm fine\"")
print("Winter \nis coming")
# Korea\Japan 을 출력하려면?
print("Korea\\Japan")

#-------------------------------
# 문자열 포매팅 (formatting)

# 방법1 % 연산자 사용
# 서식문자(format specifier) 를 포함한 문자열과, 
# 각 '서식문자'에 대응하는 데이터들을 연결하여 문자열 완
# 구문)
#    "서식문자포함문자열" % ( 데이터 튜플 )

# format specifier
#  https://docs.python.org/2/library/string.html

# %d   십진수 정수
# %f   실수
# %s   문자열

myStr = "Hello %s, %s is Fun"
print(myStr)
print(myStr %("파이썬","Python"))

name = "박수진"
age = 10
myFormat = "제 이름은 %s이고 나이는 %d 입니다."
print(myFormat %(name,age))
print(myFormat %("이해강",33))
print(myFormat %("김용",26))

pi = 3.141592
print("원주율은 %f 입니다" %(pi))
# 소숫점 이하 자리수 지정 
print("원주율은 %.1f 입니다" %(pi))
print("원주율은 %.2f 입니다" %(pi))
print("원주율은 %.3f 입니다" %(pi))

# %d : 자리수 명시 기능
a,b,c,d = 10,100,1000,10000
print("%d:%d:%d:%d" %(a,b,c,d))
print("%5d:%5d:%5d:%5d" %(a,b,c,d))  # 5칸씩 폼을 잡고 우측정렬해서 출력
print("%-5d:%-5d:%-5d:%-5d" %(a,b,c,d))  # 5칸씩 폼을 잡고 좌측정렬해서 출력


# 방법2 : format() 함수 사용 (이름을찾아가서 사용가능)
myStr = "My name is {}, I'm {} years old".format("배트맨",60)
print(myStr)

myStr = "My name is {name}, I'm {age} years old".format(name="배트맨",age=60)
print(myStr)

myStr = "My name is {name}, I'm {age} years old".format(age=60,name="슈퍼맨")
print(myStr)

# 방법3 : f문자열 (파이썬 3.6 이상 사용 가능), (외부에 있는 변수까지 사용할 수 있음)
lang = "Python"
author = "귀도 반 로썸"

myStr = f'언어:{lang}, 제작자:{author}'
print(myStr)






























