"""
연습: 
# 세 개의 정수를 입력받아 합과 평균을 출력하는 프로그램을 작성하시오.
# (단 평균은 소수 이하를 버림하여 정수 부분만 출력한다.)
예]
3개의 정수 입력:10  20 44
합= 74
평균= 24

"""

a,b,c = map(int,input("3개의 정수 입력:").split())
print("합= {}",format(a+b+c))
print("평균= {}",format(((a+b+c)/3)))