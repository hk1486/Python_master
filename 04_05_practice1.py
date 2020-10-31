# 국어 , 영어, 수학 3개의 점수(정수)를 입력받아서 
# 총점 출력
# 평균 출력(소숫점 1자리까지)
# 등급 출력
# 평균이 
#   90이상이면 A
#   80이상이면 B
#   70이상이면 C
#   60이상이면 D
#   60미만이면 F

# if ~ else ~.. ~else 사용

a = int(input("국어 점수를 입력하세요"))
b = int(input("수학 점수를 입력하세요"))
c = int(input("영어 점수를 입력하세요"))

total = a + b + c
print('총점은',total,'입니다')

avg = float((a+b+c)/3)
print("평균은 %.1f 입니다" %(avg))

print('등급: ', end='')
if avg >= 90:
    print('등급은 A입니다')
elif avg >= 80:
    print('등급은 B입니다')
elif avg >= 70:
    print('등급은 C입니다')
elif avg >= 60:
    print('등급은 D입니다')
else: 
    print('등급은 F입니다')










































