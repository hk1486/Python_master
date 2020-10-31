"""
10개의 정수를 입력받아 입력받은 수들 중 짝수의 개수와 홀수의 개수를 각각 구하여 출력하는 프로그램을 작성하시오.

입력 예]
10 20 30 55 66 77 88 99 100 15

출력 예]
even : 6
odd : 4

"""

n = map(int(input('10개의 정수를 입력하시오').split()))
even = 0 
odd = 0

for n in map(int(input.split())):
    if n % 2 == 0:
        even += 1
    else:
        odd += 1
    
print('even:',even)
print('odd',odd)
    










