scores = {'철수':80, '영희':95, '민수':70, '지연':100}


# 합계 구하기
sum = 0
for value in scores.values():
    sum += value

print('합계:', sum)


# 학생의 수 구하기
size = len(scores) #4


# 평균 구하기
avg = sum / size
print("평균 점수:", avg)


# 90점 이상 학생 수
cnt = 0
for value in scores.values():
    if value >= 90:
        print(value)
        cnt += 1

print('학생의 수:', cnt)




