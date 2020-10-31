# break
# 순환문 (while, for) 안 에서 순환문을 강제로 종료시키는 키워드
# break 는 감싸고 있는 가장 가까운 순환문을 종료합니다

# continue
# 다시 순환문 처음으로 돌아가기

n = 1
while True: #무한루프
    print (n)
    
    if n == 100:
        break
    
    n += 1
print('while문 종료')

print("*" * 30)

####################################

num = 0
while num <= 10:
    num += 1
    
    if num % 2 == 1: continue

    print(num)

print("while종료")

    
# 정수를 계속해서 입력 받다가 0이 입력되면 그때까지의 '정수의 합'과 '평균'을 출력

print("*" * 30)


print("정수를 입력하세요")

total = 0 #합
cnt = 0 #개수

while True:
    n = int(input())
    total += n # 합계 누적 합산
    cnt += 1 # 개수 1증가
    if n == 0: break
print("합계는 ",total)
print("평균은 %.1f" % (total / cnt))










































