# List Comprehension 구문
# [표현식 for 항목 in 반복가능객체 (if 조건)]

# 주어진 리스트의 원소 데이터를 각각 * 3 적용한
# 새로운 리스트를 작성하기 

a = [1,2,3,4]  # -> [3,6,9,12] 로 만들기
# print(a*3)

result = []     # 새로운 리스트 만들고 num변수로 3곱한 다음 저장
for num in a:
    result.append(num*3)
print(result)

# List comprehension 사용
result = [ num * 3 for num in a]        # 기가 막힘...
print(result)

#  [1, 2, 3, 4]
# 짝수에만 3을 곱하여 담은 새로운 리스트 생성
#    ↓    ↓
#    [6, 12]


a = [1,2,3,4]
result = []
for num in a :
    if num % 2 == 0:
        result.append(num*3)
print(result)

# List comprehension 사용
result = [num * 3 for num in a if num % 2 == 0]
print(result)

result = [
    num * 3
    for num in a
    if num % 2 == 0
    ]


# for문 2개 이상 사용도 가능

# [표현식 for 항목1 in 반복가능객체1 if 조건1
#         for 항목2 in 반복가능객체2 if 조건2
#         ...
#         for 항목n in 반복가능객체n if 조건n]


result = [
    dan
    for dan in range(2, 10)
    ]
print(result)

result = [
    mul
    for mul in range(1,10)
    ]
print(result)

result = [
    "%d x %d = %d" % (dan,mul,dan * mul)
    for dan in range(2,10)
    for mul in range(1,10)
    ]
print(result)


#-------------------------------
print()
a = [10,20,30,-20,-3,50,-70]

#위 리스트에서 양수만 뽑아내어 새로운 리스트 만들기
# List comprehension
# 결과 -> [10,20,30,50]

result = [num for num in a if num > 0]
print(result)

# n개의 0으로 초기화된 리스트 생성
n = 10
result = [0 for i in range(n)]
print(result)

# 주어진 dataset 에서 
# 제곱의 결과가 10보다 큰 결과만 담은 list 작성
# [16, 25]

dataset = [1, -2, 3, -4, 5]

result = [num**2 for num in dataset if (num**2) > 10 ]
print(result)

print('-'* 30)

# set comprehension
result = [num %3 for num in range(10)]  # [0, 1, 2, 0, 1, 2, 0, 1, 2, 0]
print(result)

result = {num %3 for num in range(10)}  # 중복을 허용안함 {0, 1, 2}
print(result)

print('-'* 30)

# Dict comprehension
 # { key : value for ~ in ~ [if ~] }

result = {
     n : n**2
     for n in range(5)
     }
print(result)

result = {
    x : list(range(x))
    for x in [1,2,3,4,5]
    }
print(result)



# 튜플 conprehension 은 없습니다.





























