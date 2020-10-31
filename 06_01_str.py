# 문자열 함수들

# 대표적으로 문자열(str)은 많은 함수(메소드)들을 갖고 있습니다.
# str 의 대표적인 함수들  ==>  split, join, replace, format

# https://docs.python.org/3/library/stdtypes.html#textseq


# upper(), lower() 대소문자 변환
str1 = 'apple'
print(str1, str1.upper(), str1.lower())

# str.join(), str.split() ---> 03_02 참조

#----------------------------------
# CSV : Comma Seperated Value
# TSV : TAB Seperated Value

data = "사과, 바나나, 파인애플, 포도, 복숭아"
print(data.split("'"))
print("\t".join(data.split()))

# replace 문자열 치환
data = '데이터 분석을 위한 파이썬 프로그래밍'
# 파이썬을 영어로 바꾸기
print(data.replace('파이썬', 'Python'))
# 문자열 원본은 변환되지 않는다.
print("replace 후 원본은 =>",data)

#split(), join() 으로 replace() 효과
print("Python".join(data.split('파이썬')))

print()
# index(), find()
#문자열 안에서 문자열 찾기
print("th" in "python")

data = "Hello Python"
# index() : 문자열을 발견한 위치 (인덱스)리턴
print(data.index('lo'))
# print(data.index('x'))  없는값을 찾으면 에러발생

print(data.find('lo'))
print(data.find('x'))   # 없는값을 찾으려고 하면 -1 리턴

# count()
# 문자열 내에서 특정 문자열 패턴의 반복 횟수
data = 'asdasdasdasdasd'
print(data.count('a'))
print(data.count('sd'))


# startswith(), endswith()
# 문자열이 특정 문자열로 시작/종료하는지 여부
url = "www.naver.com"
print(url.startswith("http"))  # F

if not url.startswith("http"):
    url = "https://" + url
    
print(url)

print(url.endswith('.com'))  # T


# ord() : 문자의 코드값(사전순)
# chr() : 코드의 문자값(사전순)
print(ord('a'))     # a의 문자값 출력 97 
print(chr(97))      # 97번 코드의 문자값 출력 a
print(ord('가'))     # 한글도 나옴 사전순서.. 44032


# 문자열에 대해 비교연산자 작동함
# 코드(사전순)으로 비교
print('a' < 'b')    # T
print('cable'<'bible')  # F
print('가마우지'<"까마귀") # T
print('aAaA'<'AaAa')    # F 대문자가 코드값이 더 작음

data = [
        'aAaA', #1
        'aaAA', #2
        'AAaa', #3
        'AaAa'  #4
        ]
print(sorted(data))        # ['AAaa', 'AaAa', 'aAaA', 'aaAA'] 사전순 정렬

# 알파벳 개수
print("알파벳 개수",ord('z')-ord('a')+1) # 알파벳 개수26
print("한글 개수",ord('힣')-ord('가')+1)  # 한글 개수 11172


# 연습
# 알파벳 소문자로 이루어진 리스트 작성
# List comprehension
# ['a','b',...'z']

alpa = [chr(i + ord('a')) for i in range(ord('z')-ord('a')+1)]
print(alpa) # ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


# 연습
word = "Alice in wonderland"

# 등장하는 알파벳의 개수 - > dict 결과 만들기
# Dict comprehension
# 대소문자 구분 안함
# hint : 알파벳 리스트, lower, upper, count

# 출력 예
# {'a': 2,
#  'c': 1,
#  'd': 2,
#  'e': 2,
#  'i': 2,
#  'l': 2,
#  'n': 3,
#  'o': 1,
#  'r': 1,
#  'w': 1}

result = {
    ch : word.lower().count(ch)         # 추출한 알파벳 : 워드.소문자변형.알파벳수
    for ch in [chr(i + ord('a'))
    for i in range(ord('z')-ord('a')+1)]  # 알파벳 리스트에서 a부터 z까지 추출
    if word.lower().count(ch) > 0       # 워드.소문자.알파벳수가 0보다 클때
     }
print(result)
















