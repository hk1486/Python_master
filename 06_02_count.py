# 주어진 문자열을 알파벳별로 출현빈도 구하려면?

# 대소문자 구분없이 소문자로만

# 입력예
# "Gorilla"
# ↓
# {
#     "g": 1,
#     "o": 1,
#     "i": 1,
#     "l": 2,
#     "a": 1,
#     "r": 1
# }


data = 'Gorilla!'
data = data.lower() # 소문자로 변경

result = {}
for ch in data:
    if 'a' <= ch <= 'z': # 알파벳만 카운트
       if not result.get(ch):  # 첫 등장이면 1
           result[ch] = 1 
       else:
              result[ch] += 1   # 이미 등장한 알파벳은 +1
   
print(result)

result={}

for ch_code in range(ord('a'), ord('z') + 1):
    ch =  chr(ch_code)
    if ch in data.lower():
        result[ch] = data.lower().count(ch)
        
print(result)


# Dict comprehension 으로 만들기

result = {
    ch : data.lower.count(ch)
    for ch in 
    [chr(ch_code) for ch_code in range(ord('a'),ord('z')+1)]
    if ch in data.lower()
    }
print(result)