# for문 안에서 break와 continue 쓰기


# for문으로 1부터 20까지 합 구하기
# 합이 100 이상이면 종료
total = 0

for i in range(1, 21):
    if total >= 100:
        break
    total += i        
print("합:", total) #결과 합: 105



# for문으로 1부터 10까지 출력
# 짝수만 출력
for i in range(1,11):
    if i%2 == 1:
        continue
    print(i) #결과: 2 4 6 8 10

