# 파일의 단어 빈도수 구하기
# 오로지 알파벳만. 검증하기
# 대소문자 구문없이 비교
# 글자수 2개 이상인 단어만 카운트 하기
# 빈도수 100회 이상인 단어만 카운트

"""
[출력예]
the 1642
and 872
to 729
it 595
she 553
of 514
said 462
you 411
alice 398
in 369
...
"""

# 1. 파일 읽기
data = None
with open("data/alice30.txt", "r") as f:
    data = f.read()
    #print(data)

# 알파벳 대/소문자 변환
data = data.lower()

# 알파벳 아닌거 제거
data2 = ''
for ch in data:
    if 'a' <= ch <= 'z':
        data2 += ch
    else:
        data2 += ' '
#print(data2)

# 단어 추출 (2글자 이상인 단어만)
words = [
        word
        for word in data2.split()   
        if len(word) > 1
        ]        
# print(words)      

# 등장 빈도 계수 06_02 참조
result = {}
for word in words:
    if result.get(word):
        result[word] += 1
    else:
        result[word] = 1 
    
#print(result)

# 100번이상 등장한것만 출력
result2 = {
        word : result[word]
        for word in result
        if result[word] >= 100
        }

#print(result2)

# 빈도수 정렬, 내림차순 정렬까지 한다면?
# dict에서 value순으로 정렬하기
sorted_keys = sorted(result2, key=result2.get, reverse=True)
for key in sorted_keys:
    print(key,result2[key])


# 정규표현식 + split() 사용하면 단어 쉽게 분리 가능
import re
# print(re.findall("[a-z]{2,}",data))

#[a-z]{2,} <- 알파벳에서 2글자이상인 단어






































