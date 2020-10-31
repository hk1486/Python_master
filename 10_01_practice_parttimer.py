# 연습 : Parttimer 설계
# '매 직원(PartTimer)'에 공통적으로 적용되는 자료
# - 시급 : 8500
# - 전체 직원수

# 각 직원별 객체 생성시 직원별로 '별칭'과 '근무지' '급여총액' 초기화 (속성)
#   '근무지' 생략시 '113동' 으로 지정
#   직원별로 '급여총액'  0으로 초기화

# 직원의 급여 계산하기(동작)
#    '몇시간 근무',  '+상여금'  에 따른 직원급여 계산
#   '상여금' 은 지정안하면 0 으로 처리


# 예]
# park = PartTimer('라이언')   // park 은 ‘라이언’ 이라는 닉네임의 직원으로 등록

# park 이 4시간 일한 급여 총액은?  → 34400
# park 이 2시간 일한 급여 총액은? → 17200
# park 이 2시간 일한 급여 + 상여급 2000 총액은? → 19200


class Parttimer:
    
    hour_rate = 8500    # 시급
    total_part_timers = 0 #전체 직원수
    
    def __init__(self,nickname,workplace = '113동'):
        self.nickname = nickname  # 별칭
        self.workplace = workplace # 근무지
        self.total_wage = 0 #급여총액
        Parttimer.total_part_timers += 1
        
        
    def calculate_wage(self,hour,bonus = 0):
        self.total_wage = Parttimer.hour_rate * hour + bonus
        return self.total_wage
        
park = Parttimer(('라이언')) 
lee = Parttimer('네오','127-1동')
        
print(park.__dict__)
print(lee.__dict__)

park.calculate_wage(4)
lee.calculate_wage(2)
        
print(park.total_wage)
print(lee.total_wage)

lee.calculate_wage(10,42000)
print(lee.total_wage)
        
        
        
        