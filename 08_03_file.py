# 파일을 다루기 위해선 open(), close() 함수로 감싸여진다

# 파일객체 = open(파일 이름, 파일 열기 모드)
#   ... 파일객체사용 (읽기 or 쓰기)
#   ... 파일객체사용 (읽기 or 쓰기)
#   ... 파일객체사용 (읽기 or 쓰기)
# 파일객체.close()

# 파일 열기 모드
# r  읽기모드 - 파일을 읽기만 할 때 사용
# w  쓰기모드 - 파일에 내용을 쓸 때 사용.  해당 파일이 없으면 새로 생성. 해당파일이 있었으면 삭제하고 새로 생성 ★
# a  추가모드 - 파일의 마지막에 새로운 내용을 추가 시킬 때 사용.  해당 파일이 없으면 새로 생성

f=open('새파일.txt',"w")
f.close()

#--------------------------
#쓰기
#파일.write()

f = open("새파일.txt","w")

for i in range(1,11):
    data = "Line %d\n" % i
    f.write(data)
    
f.close()

#------------------------
#읽기
#한줄읽기 readline()

f = open("새파일.txt","r")

line = f.readline()
print(line)

line = f.readline()
print(line)

f.close()

#------------------------
#읽기
#파일의 모든 라인읽기 

#방법1 : readline()
f = open("새파일.txt","r")
while True:
    line = f.readline()     #더이상 읽을 라인이 없는경우 none리턴
    if not line: break
    print(line, end = "")
f.close()

#----------------------------
print()

#방법2 : readlines()
f = open("새파일.txt","r")
lines = f.readlines()   #각각의 line을 담은 list를 리턴
#for line in lines:
#    print(line,end="")
print(''.join(lines))
f.close()

#----------------------------
print()

#방법3 : for문
f = open("새파일.txt","r")

#파일 객체를 for에서 사용하면 한 라인씩 읽어들인다.
for line in f:
    print(line,end='')
    
f.close()

#----------------------------
print()

#방법4 : read() 사용
f = open("새파일.txt","r")
data = f.read() # 파일의 전체를 읽어옴
print(data)
f.close()

#----------------------------
# 추가
f = open("새파일.txt","a") # 추가모드 어팬드

for i in range(11,20):
    data = '%d Line appended\n' % i
    f.write(data)

f.close()

f = open("새파일.txt","r") 
print(f.read())
f.close()


print()
with open("새파일.txt","r") as f: #with로 하면 close까지 됨
    data = f.read()
    print(data)    



























