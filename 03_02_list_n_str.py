# list 와 str의 관계

# str.join() : list -> 하나의 str으로 묶어줌
animals = ['dog','shark','cat','bird']
'--'.join(animals)
result = '--'.join(animals)
print(result)  # dog--shark--cat--bird

myList = ['2020','04','09']
print('-'.join(myList)) # 2020-04-09


# str.split() : 하나의 str -> List로 쪼개줌
myStr = 'Hello Python 2020'
myList = myStr.split()  # 공백 단위로 문자열 쪼개어 List로 만듬
print(myList)   # ['Hello', 'Python', '2020']

myStr = '2020-04-09'
print(myStr.split('-')) # 하나의 문자열이 3개의 원소로 쪼개진 List ['2020', '04', '09']

myStr = '2020-04-09 20:40:32'
print(myStr.split()[0].split('-') + myStr.split()[1].split(':'))
# -----> ['2020', '04', '09', '20', '40', '32']

myStr = 'animals'        
print(list(myStr))  # 형변환 하면 글자 하나하나 담긴 list 만듬 ['a', 'n', 'i', 'm', 'a', 'l', 's']

# 'animals' 문자열을 --> 'a-n-i-m-a-l-s' 문자열로 바꿔보자
myStr = 'animals'
print('-'.join(list(myStr)))    # 리스트로 바꿔주고 조인으로 Str로

# (not) in 연산자
animals = ['dog','shark','cat','bird']
print('dog' in animals) # True
print('tiger' in animals) # False
print('eagle' not in animals) # True

myStr= 'Python'
print('t' in myStr)     # True
print('py' in myStr)    # False
print('Py' in myStr)    # True




