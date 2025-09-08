# 반복문: while, for
# while: 조건이 참인 동안 반복 수행
# for: 자료구조에서 요소를 하나씩 꺼내면서 반복 수행


lis = ['a', 'b', 'c', 'd', 'e']
# 리스트의 크기만큼 반복 수행
# 리스트의 요소를 하나씩 꺼내서 변수에 저장후 사용
for ch in lis:
    print(ch)

# 딕셔너리 생성 (key값:value값)
dic = {'apple':1200, 'banana':800, 'orange':1500}

# for문으로 딕셔너리 안에 요소 하나씩 꺼내기
for k in dic:
    print(k)

# 값 꺼내기
# 딕셔너리에서 dict_values 객체 추출
print(dic.values())

# for 변수 in 리스트, 튜플, 딕셔너리, iter
# iterable(이터러블): 순회가 가능한 객체
for v in dic.values():
    print(v)


# dic.items:키, 값 모두 가지고 있는 객체
for key, value in dic.items():
    print(key, value)

# range: 연속된 숫자를 만드는 객체
# range(개수)
for n in range(10): #마지막숫자는 생략
    print(n)

for n in range(1,11): #시작과 끝, 마지막숫자는 생략
    print(n)

for n in range(10):
    print('안녕하세요') #10번 출력

for _ in range(10):
    print('안녕하세요') #변수 언더바 _ 로 대체 가능












