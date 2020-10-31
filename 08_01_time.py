# time 모듈 함수들

import time
result = time.time()     # time모듈안에 있는 time()함수 호출
                        # 타임스탬프 값을 리턴,
                        # 1970.1.1 00:00:00 기준으로 경과된 시간(초)
print(result)

result = time.localtime()   # 현재 지역시간 정보
print(result)
print(result.tm_year, result.tm_mon, result.tm_mday)

# timestamp를 str로 바꾸기

result = time.strftime('%x',time.localtime())
print(result,type(result))      # 04/23/20 <class 'str'>

result = time.strftime('%c',time.localtime())
print(result,type(result))      # Thu Apr 23 19:19:01 2020 <class 'str'>

result = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
print(result,type(result))      # 2020-04-23 19:21:10 <class 'str'>

# 일정 시간 딜레이 주기 : sleep()

# 경과시간 측정
start_time = time.time()    # 시작시간 기록

for i in range(5):
    print(i)
    time.sleep(2) # 2초의 딜레이주기, 단위:초

end_time = time.time()  # 종료시간 기록

lap_time = end_time - start_time # 경과시간
print('경과시간:',lap_time)

# 경과시간을 시:분:초  로 나타내려면?

# 물론 일일히 계산 할수도 있다.. 3600 나눈몫이 경과 시간이고..
# 다시 나머지로... 분, 초 계산하고

# 그러나, 파이썬에서는 이를 위한 timedelta 함수가 있다
# 활용할수 있으면 활용하자

import datetime
print(datetime.timedelta(seconds = 3000))































