# 등급별 생존확률 계산하기

# 등급별 생존률 계산하기
"""
3등급] 총 491 명, 생존 119 명, 생존률 24.2%
1등급] 총 216 명, 생존 136 명, 생존률 63.0%
2등급] 총 184 명, 생존 87 명, 생존률 47.3%
"""


result = {}
with open('data/titanic.csv','r') as f:
#Line 별로 읽어들이기
    f.readline()    # 첫라인은 넘어감(파일에서 데이터가 아니라 헤드라인이기 때문)
    for line in f:
        psgr = line.split(',') #Line 을 콤마로 쪼개기
        #생존여부, 객실등급 확인 집계        
        survived = psgr[1]
        pclass = psgr[2]
        
        if result.get(pclass):
            result[pclass].append(survived)
        else:
            result[pclass] = [survived]

    # { "1" : [0,1,0,0,1 ...1], "2" : [], "3" : []}

    
#출력
for key in result:
    total = len(result[key]) # 객실별 총 탑승인원
    survived = int(result[key].count("1"))
    print("[%d등급] 총 %d 명, 생존 %d 명, 생존률 %.f퍼센트" % (int(key),total,survived, (survived/total)*100))
