# tuple : 튜플
# 콤마 , 로 구분된 집합 데이터 타입

#1. list   :  순서있다.  중복허용,  mutable
#2. tuple  :  순서있다,  중복허용,  immutable
#3. set : 순서없다,  중복허용안함
#4. dict : key, value 쌍으로 구성, 순서없다.

animals = 'dog','cat','bird','fish'
print(type(animals))    # tuple

student = ('이','김','박')    # 괄호 사용 가능
print(student)
print(type(student))

print(len(animals))
print(len(student))

# 데이터원소 하나짜리 튜플을 만드려면...
animals = ('dog') # <- 문자열!!

# 콤마 하나 붙여주세요...
animals = 'dog',
student = '김이박',
print(animals, type(animals))
print(student, type(student))

# tuple은 순서가 있다 ---> index, slice 가능
animals = ('dog','dog','cat','bird')
print(animals)
print(animals[0], animals[1])   # dog dog

# tuple은 immutable 즉, 값 변경불가!
# animals[0] = 'puppy' 에러
# animals.append('puppy') <-- 내용 변경하는 동작 없음

# +,* 연산 가능
print(animals + ('fish' , 'turtle')) # -> 연산만 되고 값은 바뀌지 않음 ('dog', 'dog', 'cat', 'bird', 'fish', 'turtle')
print(animals)  # ('dog', 'dog', 'cat', 'bird')
print(animals *2)

# tuple 은 언제 사용하나?
# 1. 주로 변경되지 말아야 할 데이터들
# 2. 복수의 값 '전달' 목적으로. 

#ex) 사각형 : [가로, 세로] 값
# 리스트의 경우
rec = [100,200]
width = rec[0]
height = rec[1]
print(width,height)

# 튜플의 경우
rec = (333,500)
width, height = rec # 한번에 여러개 대입 가능
print(width,height)

a,b,c = [111,222,333]
print(a,b,c)    # 111 222 333

a,b,c = 'XYZ'
print(a,b,c)     # X Y Z































































