# 1부터 20까지 더하다가
# 합이 100을 넘으면 while문 강제로 빠져나가기
#  break -> 중단
num = 1
total = 0

while num <= 20:   # 1~20까지만 반복
    total += num
    if total > 100:   # 합이 100을 넘으면 종료
        break
    num += 1

print("마지막 더한 숫자:", num)
print("합계:", total)


# 반복문을 사용해서 1부터 10까지 출력하기
# 단 숫자가 짝수일때만 출력
# continue -> skip
i = 1
while i < 11:
    if i%2 == 1:
        i += 1
        continue
    print(i)
    i=i+1