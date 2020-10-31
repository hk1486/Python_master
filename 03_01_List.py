# 여러개의 데이터를 담는 집합 데이터 타입들..
#1. list   :  순서있다.  중복허용,  mutable(데이터 변경가능한것)
#2. tuple  :  순서있다,  중복허용,  immutable(데이터 불변)
#3. set : 순서없다,  중복허용안함
#4. dict : key, value 쌍으로 구성, 순서없다.

"""
list

# list 는   [   ]  으로 만든다
# 데이터(원소) 들은 , 콤마로 구분한다
# 각 데이터(원소) 들은 어떠한 타입도 가능하다
"""

animals = ["dog","cat","bird","bear","wolf"]
print(animals)
print(type(animals))

# 인덱싱 (indexing)
print(animals[0])  # index 첫번째 데이터 원소, 0부터 시작
print(animals[1])
print(animals[2])
print(animals[3])
print(animals[4])
# print(animals[5]) # 인덱스에 데이터가 없으면 에러남

# 음수 인덱싱 기능
print(animals[-1])

# 리스트 안의 원소의 개수 : len() 함수
print(len(animals)) # 5

# append() : 데이터 원소를 리스트 끝에 추가
animals.append("tiger")
print(animals)

# 데이터 원소 삭제 : del()
del(animals[1])
print(animals)

# 데이터 변경 (기존 데이터를 덮어씀)
animals[1] = "eagle"
print(animals)

# mutable 하다! - 데이터의 변경, 추가, 삭제 등이 가능
# -------------------------------------------------

# list의 연산들
colors = [] # 빈(empty) List
print(len(colors))
colors = ['white', 'blue' ,'red']

# list + list
print(animals + colors)

# list * list
print(colors * 2)

# list.extend()
animals.extend(['shark', 'fish']) # animals에 원소 추가가능, list 안에 원소들이 추가(append와의 차이)
print(animals)

animals.append(['aaa','bbb']) # list 하나 추가
print(animals)

myList = [10,20,30]
myList.append([40,50,60])
print(myList)
print(len(myList))       # 리스트가 추가되었기 때문에 길이가 4 

myList = [10,20,30]
myList.extend([40,50,60])
print(myList)
print(len(myList))      # 원소 3개가 추가되었기 때문에 길이가 6

# List의 각 데이터 원소는 어떠한 데이터의 (타입)도 가능하다!
myList = [100,200,"John",0.29,False,None]
# 따라서 List 의 원소가 List일 수도 있다!

myList = [
        [10,20,30],
        [40,50,60],
        [70,80,90]
        ]
print(len(myList))
print(myList[0])    # [10,20,30]
print(myList[0][1]) # 20
print(myList[2][1]) # 80
print(myList[1][2]) # 60

# 인덱스를 이와같이 2개 쓰는 리스트를 2차원 리스트
# --> 1차원 리스트를 원소로 하는 리스트 

# 따라서, 3차원 리스트의 원소는 2차원 리스트
# 100차원 리스트의 원소는 99차원 리스트

myList = [
        [
                [1,2,3],
                [4,5,6],                    
                [7,8,9],
                ]
        ,
        [
                [10,20,30],
                [40,50,60],
                [70,80,90]
                ]
        ]
        
print(myList[0][1][1])  # 5
print(myList[1][0][0])  # 10
print(myList[1][2][1])  # 80

# slicing 
# 리스트의 일부분만 '추출'함 (원소 ':' 원소)
myList = [10,20,30,40,50,60,70,80,90,100]
print(myList)
print(myList[0:3]) # 0부터 시작해서 ~ 3이전까지 추출 [10,20,30]
print(myList[1:6]) # 1부터 6이전까지 [20,30,40,50,60]
print(myList[:5])   # 처음부터 5이전까지 [10,20,30,40,50]
print(myList[5:])   # 5부터 끝까지 [60,70,80,90,100]

# step
print(myList[0:9:2]) # 0부터 9까지 2칸씩 건너뜀 [10, 30, 50, 70, 90]
print(myList[:])    # 처음부터 끝까지~
print(myList[::3])  # 처음부터 3칸씩 건너뜀 [10, 40, 70, 100]
print(myList[::-1]) # 역순정렬효과, 끝에서 부터 출력 [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]
print(myList[::-2]) # 뒤에서부터 2칸씩 띄고 출력 [100, 80, 60, 40, 20]

# Str도 slicing, step 가능
myStr = 'Hello Python'
print(myStr[0:5])
print(myStr[::-1]) # 역순정렬 nohtyP olleH

# Index vs slice
myList = [10,20,30,40,50]
myList[2] = ['a','b']
print(myList)       # [10, 20, ['a', 'b'], 40, 50] 리스트가 통채로 들어감

myList = [10,20,30,40,50]
myList[2:3] = ['a','b']
print(myList)       # [10, 20, 'a', 'b', 40, 50] 원소가 하나씩 들어감


# index(value) : 값으로 인덱스 찾기
animals = ['dog','cat','bird','fish'] 
print(animals.index('cat')) # 1
# print(animals.index('냥냥이')) # 리스트에 없으므로 에러

# pop() : 리스트 맨뒤의 원소가 리턴, 리스트에서는 제거됨
a = animals.pop()
print(a)    # fish
print(animals)  # fish가 사라짐['dog', 'cat', 'bird']
animals.pop()
animals.pop()
print(animals)  # dog 하나 남음

# pop(n) : n 번째 원소 나옴
animals = ['dog','cat','bird','fish'] 
print(animals.pop(2))   # bird
print(animals)

# sort() : 데이터정렬,
# reverse() : 뒤짚기
animals = ['dog','cat','bird','fish'] 
print(animals)
animals.sort()  # 오름차순 정렬(알파벳순)
print(animals)  # ['bird', 'cat', 'dog', 'fish']

animals.sort(reverse = True)    # 내림차순 정렬
print(animals)  # ['fish', 'dog', 'cat', 'bird']

animals.reverse()   # 뒤짚기
print(animals)  # ['bird', 'cat', 'dog', 'fish']

print(animals[::-1])    # 데이터 변경하는게 아님 ['fish', 'dog', 'cat', 'bird']
print(animals)          # ['bird', 'cat', 'dog', 'fish']



















































