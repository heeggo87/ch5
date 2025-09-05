lis = ['a','b','c','d','e']

# for문으로 리스트 요소 하나씩 출력 -> for문 기본구조
for ch in lis: # for 변수 in 자료구조
    print(ch)


# while문과 for문의 차이
# while: 조건을 만족하는 동안 실행
# for: 자료구조(리스트, 튜플 등)을 순회


# 딕셔너리 생성
# key:value (과일:가격)
dic = {"apple": 1200, "banana": 800, "orange": 1500}

# 딕셔너리 안에 모든 아이템 꺼내기
items = dic.items() 

# 딕셔너리 안에 요소 하나씩 꺼내기 -> tuple
for t in items:
    print(t)

# 튜플을 키와 값으로 분리 (구조분해)
for key, value in items:
    print(key, value)

# 딕셔너리 안에 값만 꺼내기
values = dic.values()
print(values) #dict_values([1200, 800, 1500])

# 값 하나씩 출력
for value in values:
    print(value) #1200 800 1500


# iterable
# 예) dict_keys, dict_values, dict_items

# for문의 구조
# for 변수 in 자료구조 또는 iterable


