# 파이썬 기본 입력 :  input()
# 키보드로부터 입력받아 문자열(str) 결과 리턴

# a = input()
# print("입력하신 값은", a)

# b = input()  # 결과값은 str, 산술연산불가!
# print("b+100=",b+100)

#b = input()
#b = int(b) # 형변환 함수로 산술연산 가능
#print("b+100 =",b+100)

#b= int(input())
#print("b+100=",b+100)

# prompt 를 사용하여 input 입력
height = float(input("키를 입력하세요 cm:"))
height /= 100
print("키는 %f m 입니다" %(height))
