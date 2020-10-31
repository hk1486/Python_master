# '택시'에는 승객들에게 공통적으로 적용되는 자료
# - 택시 요율 (거리당 요금)
# - 기본 요금
# - 최초 기본 주행 거리

# 택시 객체 생성시 승객별로 돈과, 거리를 받아서 생성

# 거리에 따른 요금 계산 메소드 정의
# 거리에 따른 잔돈 계산 메소드 정의

# 기본요금 : 3000
# 기본주행거리 : 2 km
# 거리당 요율 : 700  (거리 1km당 요금)


class Taxi:
    fare_rate = 700 # 택시 요율 (거리당 요금)
    basic_rate = 3000 # 기본 요금
    basic_distance = 2 # 최초 기본 주행 거리
    
    # 생성자(돈,주행거리)
    def __init__(self,money,distance):
        self.money = money      # 승객이 지불한 돈
        self.distance = distance  # 승객의 이동거리
    
    # 택시요금 계산
    def calculate_rate(self):
        cost = 0        
        cost = Taxi.basic_rate + (( self.distance - Taxi.basic_distance )* Taxi.fare_rate if self.distance >= Taxi.basic_distance else 0 )
        return cost
    # 잔돈계산
    def get_change(self):
        change = self.money - self.calculate_rate()
        return change
    
passenger1 = Taxi(20000,1) # 20000원을 가지고 거리 1km 이동하는 경우
    # 승객1의 비용은? 3000
    # 잔돈은? 17000
print(passenger1.calculate_rate())
print(passenger1.get_change())

passenger2 = Taxi(30000, 10)   # 30000원을 가지고 거리 10km 이동하는 경우
print(passenger2.calc_cost()) # passenger2 의 비용은 ? → 8600
print(passenger2.get_change()) # passenger2 의 잔돈은 ? → 21400










































