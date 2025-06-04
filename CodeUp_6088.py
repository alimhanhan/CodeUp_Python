n = int(input())  # 정수 입력 받기

for i in range(1, n + 1):
    if i % 3 == 0:
        continue  # 3의 배수는 건너뜀
    print(i, end=' ')  # 조건을 만족하지 않으면 출력