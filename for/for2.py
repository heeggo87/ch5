# 10부터 20까지 연속된 숫자 반환
nums = range(10,21) #마지막숫자 포함 안함
print(nums)

for n in nums:
    print(n)

# 0부터 9까지 연속된 숫자 반환
nums = range(10)

for n in nums:
    print('안녕하세요') #10번 출력

# 변수가 필요하지 않을 때는 _로 표시
for _ in nums: 
    print('안녕하세요')


# input: 키보드를 통해 값을 입력받는 함수
# 숫자 3번 입력 받고 합 구하기
total = 0  # 합을 저장할 변수 초기화

for _ in range(3):  # 3번 반복
    num = int(input("숫자를 입력하세요: "))  # 사용자로부터 숫자 입력받기
    total += num  # 입력받은 숫자를 누적 합계에 더함

print("합계:", total)  # 합계 출력




