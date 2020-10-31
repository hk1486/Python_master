"""
연습: 
# 키(cm) 와 몸무게(kg) 를 입력받아 bmi 를 계산하여 출력
# bmi = 몸무게(kg) /  (키(m) x 키(m))
# bmi는 소숫점 한자리까지 출력

예]
키(cm) 와 몸무게(kg) 를 입력하세요183 93
BMI 는 27.8 입니다

"""
height, weight = map(float,input("키(cm)와 몸무게(kg)를 입력하세요").split())
height /= 100
bmi = weight / (height ** 2)
print("bmi는 {:.1f} 입니다.".format(bmi))

