"""
연습: 단위 변환
1야드(yd)는 91.44cm이고 1인치(in)는 2.54cm이다.
처음에는 야드를 입력받고, 두번째는 인치를 입력받아 
각각 cm로 변환하여 다음 형식에 맞추어 소수 둘째자리까지 출력하시오.​
예)
yard 입력: 23.45
inch 입력: 41.273
23.45 yard 는 2144.27cm
41.27 inch 는 104.83cm

"""

a=float(input("yard 입력:"))
b=float(input("inch 입력:"))
c=a*91.44
d=b*2.54
print("%.2f yard는 %.2f cm" %(a,c))
print("%.2f inch는 %.2f cm" %(b,d))