
# 자연수 n을 입력받아서 n줄만큼 다음과 같이 출력하는 프로그램을 작성하시오.
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
a = int(input("0보다 큰 자연수를 입력하세요"))
n = 1
while n <= a:
    print ("*" * n)
    n += 1
print()

"""
# 자연수 n을 입력받아서 n줄만큼 다음과 같이 출력하는 프로그램을 작성하시오.
"""
[입력예]
3
[출력예]

*
**
***
**
*

"""

n = int(input("0보다 큰 자연수를 입력하세요"))

i = 1
while i <= n:
    j = 0
    while j < i :
        print("*", end = "")
        j += 1
    print()
    i += 1
    
i = n-1
while i > 0 :
    j = 0
    while j < i :
         print("*",end="")
         j+=1
    print()
    i -= 1











