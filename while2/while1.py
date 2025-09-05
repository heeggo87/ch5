# 반복문 복습

# 1부터 10까지 출력
i=1
while i<11:
    print(i)
    i+=1


# 반가워요 3번 출력
i=0
while i<3:
    print('반가워요')
    i+=1


# 2 4 6 8 10 짝수 5개 출력
i=0
while i<5:
    print((i+1)*2)
    i+=1


# 3부터 6까지 출력
i=3
while i<7:
    print(i)
    i+=1


# hello 5번 출력
i=0
while i<5:
    print('hello')
    i+=1


# 1부터 7까지 출력
i=1
while i<8:
    print(i)
    i+=1


# 1 3 5 7 9 홀수 5개 출력
i=0
while i<5:
    print((i*2)+1)
    i+=1


# 11부터 20까지 출력
i=11
while i<21:
    print(i)
    i+=1


# 1부터 5까지 합 구하기 
i=1
sum=0 #합을 저장할 변수 필요
while i<=6:
    sum=sum+i
    i+=1
    print('합계:',sum)



# 리스트의 요소를 하나씩 출력
num = [10,20,30]

i=0
while i<3:
    print(num[i])
    i+=1


# 1부터 20까지 더한 합 구하기
# 100넘어가면 종료
i=1
sum=0
while i<=20:
    if sum>100:
        break
    sum=sum+i
    i+=1
    print('합계:',sum)


# 요소 하나씩 출력
# 77을 만나면 break 사용해 종료
lis = [100,77,-5,10]

i=0
while i<4:
    if lis[i]==77:
        break
    print(lis[i])
    i+=1


# 1부터 10까지 출력
# 3의 배수 만나면 break 사용해 종료
i=1
while i<=10:
    if i%3==0:
        break
    print(i)
    i+=1


# 요소 하나씩 출력
# 문자열의 길이가 4를 넘으면 종료
lis = ['aa','bbb','ccccc','dd']

i=0
while i<4:
    if len(lis[i])>4:
        break
    print(lis[i])
    i+=1


# 1부터 10까지 출력
# 짝수 건너뛰고 홀수만 출력
i=1
while i<=10:
    if i%2==0: #짝수면
        i+=1 #짝수 제외하고 i 증가후 다음 반복으로 
        continue #건너뜀
    print(i) #홀수면 출력
    i+=1

# 요소 하나씩 출력
# 단 숫자를 만나면 continue를 사용해 건너뛰기
lis = [10,'a',True,20,'b'] #int, str, bool, int

i=0
while i<5:
    if type(lis[i]) == int: #타입이 int인지 확인
        i+=1
        continue 
    print(lis[i])
    i+=1









