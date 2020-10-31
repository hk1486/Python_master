# dict : 딕셔너리

# dictionary 데이터 타입은  key-value 쌍으로 저장되는 데이터 집합이다.

# {Key1:Value1, Key2:Value2, Key3:Value3 ...}
# "이름" = "홍길동", "생일" = "몇 월 몇 일"   과 같은 자료형 담음

# 기존의 list, tuple 등은 value 중심
# 그러나 이 또한 알고 보면 key-value 쌍으로 구성

# 순서는 고정이 안된다

student = {
        "name":"최현진",
        "email":"@naver.com"
        }
print(student)
print(type(student))    # dic
print(len(student))     # 2 (키,밸류 쌍 개수)

# value 접근하기
print(student["name"])  # 최현진(밸류값) 방법1
print(student.get("name"))  # 최현진(밸류값) 방법2
# 차이점 : 존재하지 않는 key의 경우 달라짐
# print(student["age"])   # keyerror
print(student.get("age"))   # None을 리턴함. 에러나지는 않음
# get() 을 사용하면 예외적인 상황에서도 동작가능하게 처리할 수 있다.

print(student.get('age',20))    # 20 .... age 키가 없으면 20으로 리턴하도록 처리. 

 # 수정하기
student["name"] = '이민규'
print(student)

# 추가하기
student['address']='논현동'
print(student)

# 삭제하기
del(student['email'])
print(student)

# key 값은 중복된 값 불가!
# value 는 같은 값 가능!
 



















