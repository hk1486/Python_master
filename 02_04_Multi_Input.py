# 여러개의 값을 한번에(한줄에) 입력받기 ....
a,b,c = 10,20,30

#a,b,c = input("3개를 입력하세요")  # 여러개 입력 불가 (입력값이 문자열이기 때문)

# 방법1 : input().split() <- 공백으로 구분하여 여러개 입력

#a,b,c = input("3개를 입력하세요").split()
#print("입력값은:",a,b,c)

#hour, minute, second = input("시:분:초 입력").split(":")  # split 문자 기준으로 쪼개서 입력가능
#print(hour,"시",minute,"분",second,"초")

#print("합계는",int(hour)+int(minute)+int(second))  # 입력값이 str이기 때문에 정수로 형변환을 해줘야함

# map() 함수 사용하여 입력값들 전부다 int 값 변환하기
# ex) int값으로 변환하기
# 변수1, 변수2 .. = map(int, input().split()) <- 쪼개진 개별데이터를 int로 형변환

#a,b,c = map(int, input("3개 정수 입력: ").split())
#print("합계는 =",a+b+c)

height, weight = map(float,input("키와 몸무게 입력: ").split())
print("키:",height,"몸무게:",weight)









