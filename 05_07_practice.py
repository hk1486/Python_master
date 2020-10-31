"""
100 이하의 자연수 n을 입력받고 
n개의 정수를 입력받아 평균을 출력하는 프로그램을 작성하시오.
(평균은 반올림하여 소수 둘째자리까지 출력하도록 한다.)


입력 예]
3
99
65
30

출력 예]
64.67

"""

n = int(input())

total = 0

#for i in range(n):
 #   total += int(input())

#map의 결과를 for문에서 사용가능
cnt = 0
for i in map(int,input().split()):
    total += i
    cnt += 1
    if cnt == n: break
    
print("{:.2f}".format(total/n))






















