# 리스트 생성
nums = [1,2,3,4]

# nums 사용해 새로운 리스트 생성
new_nums = []

# nums 각 요소에 *3 을 해서 [3,6,9,12] 만들기
for n in nums:
    new_nums.append(n*3)

# 위 코드를 '리스트 컴프리헨션' 이라는 문법으로 간단하게 작성하기
# 새로운리스트 = [변수 + 반복문]
new_nums = [n*3 for n in nums]
print(new_nums)


# 복습
nums = [1,2,3,4,5,6,7,8,9,10]
new_nums = []

for n in nums:
    if n%2 == 0:
        new_nums.append(n)

# 리스트 컴프리헨션 문법
new_nums = [n for n in nums if n%2 == 0]
print(new_nums)



strings = ['a', 'bb', 'ccc', 'dddd', 'e']
new_str =[]

# 문자의 크기가 2보다 큰 것을 찾고 대문자로 변환해서 담기
for ch in strings:
    # print(len(ch))
    if len(ch) > 2:
        # print(ch, len(ch), ch.upper())
        new_str.append(ch.upper())

# 리스트 컴프리헨션 문법
new_str = [ch for ch in strings if len(ch) > 2]
print('결과:', new_str)








