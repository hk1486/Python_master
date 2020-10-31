4# 자연수 n을 입력받아서 n줄만큼 다음과 같이 출력하는 프로그램을 작성하시오.
# for문을 사용하여
"""
[입력예]
5

[출력예]

*
**
***
****
*****

"""
"""
a = int(input("자연수 하나를 입력하시오"))
n = 1
for n in range(a+1):
        print('*' * n)
"""
n = int(input("자연수 하나를 입력하시오"))
for i in range(n):
    for j in range(i+1):
        print('*',end="")
    print()
    
    


















