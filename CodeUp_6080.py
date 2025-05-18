# n, m 입력 받기
n, m = map(int, input().split())

# 두 개의 주사위 조합 출력
for i in range(1, n + 1):
    for j in range(1, m + 1):
        print(i, j)