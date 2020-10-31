"""
1부터 전달받은 수까지의 합을 출력하는 함수를 작성하고 
1000 이하의 자연수를 입력받아 작성한 함수로 전달하여 출력하는 프로그램을 작성하시오. 
(함수를 작성하세요)
입력예]
100

출력예]
5050
"""
def sum_(a):
    total = 0
    for num in range(1,a+1):
        total += num
    return total
b = sum_(100)
print(b)


"""
n개의 정수를 입력받아 각 정수의 절대값의 합을 출력하는 프로그램을 작성하시오. 
(함수를 작성하세요)

입력예]
35 -20 10 0 55

출력예]
120
"""
def ab(*args):
    total = 0
    for num in args:
        if num > 0:
            total += num
        elif num < 0:
            total += (-num)
        
    return total
c = ab(35,-20,10,0,55)
print(c)



"""
자연수를 입력받아 아래와 같은 사각형을 화면 출력하는 프로그램을 작성하시오. 
주어지는 수는 100이하의 자연수이다.
(함수를 작성하시오.) 

입력예]
3

출력예]
1 2 3
2 4 6
3 6 9

"""
def cube(n):
    for i in range(1,n+1):
        for j in range(n):
            print(i + j * i , end = ' ')
        print()
    
cube(3)
cube(4)













































