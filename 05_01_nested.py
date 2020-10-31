# 조건문안의 순환문,
# 순환문안의 조건문,
# 순환문안의 순환문...

# 1 ~ n 까지의 숫자 중에서
# 3과 7의 공배수만 출력하기
n =200
i = 1
while i <= n:
    if i % 3 == 0 and i % 7 == 0:     
        print(i)
    i += 1
    
# 순환문안의 순환문, 중첩 순환문(nested loop)
# 구구단 
# 2단 ~ 9단 
    
"""
2 x 1 = 2
2 x 2 = 4
...
2 x 9 = 18
3 x 1 = 3
..
3 x 9 = 27
..
..
9 x 9 = 81
"""

print("구구단","*" * 20)

#2단 부터 9단 순환
dan = 2
while dan <= 9 :
    
    print(dan,"단")
    # x1 ~ x9 순환
    mul = 1
    while mul <= 9:
        print(dan,"x",mul,"=",dan*mul)
        mul += 1
        
    print()
    dan += 1
print("출력 종료")











































