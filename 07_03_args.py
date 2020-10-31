# 가변 매개변수 *args
# 가변매개변수(various arguments) 함수 구문

# def 함수이름(*매개변수): 
#     <수행할 문장>
#     ...

# 함수 호출시 전달된 복수개의 매개변수는 tuple 의 형태로 다루어진다
# args <-- arguments

def var_args(*args):
    print(type(args),':',len(args),args)
    
var_args(10)
var_args(10,20)
var_args(10,20,30)
var_args()  # 튜플이므로 가능하다
var_args([10,20],[30,40],[50,60])


def sum_many(*args):
    total = 0
    for num in args:
        total = total + num
    return total

print(sum_many(10,20,30))
print(sum_many(10,20,30,40,50,60))
print(sum_many(0.1,10.4,3.123,-44))


# 가변매개변수는 다른 (고정) 매개변수와  혼합 사용 가능.
# 그러나! 가변 매개변수는 다른 매개변수 뒤에 정의되는것을 ㅊㅊ


def sum_mul(operator,*args):
    result = None
    
    if operator == 'sum':
        result = 0
        for i in args:
         result += i
         
    elif operator == 'mul':
        result = 1
        for i in args:
            result *= i
            
    return result

print(sum_mul('sum', 10,20,30))
print(sum_mul('mul', 10,20,30))
    

def sum_mul(*args,operator):   #순서바꿔보기
    print(args,operator)

# print(sum_mul('sum', 10,20,30))  # 불가
print(sum_mul( 10,20,30,operator='sum'))  #가능은 하나, 비추천...


#--------------------------
# 키워드 매개변수  **kwargs
# kwargs : keyword argument 약자

# 함수호출시 함수의 인수로 key = value 형태로 주어지면
# 함수에선 kwargs 가 '딕셔너리' 형태로 받아옴  

def function(**kwargs):
    print(type(kwargs),len(kwargs),kwargs)
    
function(name = 'john')
function(name = 'john',age = 32)
function()  # 키밸류없는 딕셔너리도 가능
function(a=1,b=2,c=3,d=4)


# *args, **kwargs 혼용 가능

def func(*args,**kwargs):
    print(len(args),args)
    print(len(kwargs),kwargs)
    
func(1,2,3,name = 'pooh',age = 4)
































































































