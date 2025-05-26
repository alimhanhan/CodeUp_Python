# 입력 받기
r, g, b = map(int, input().split())

count = 0

# 모든 조합 출력
for i in range(r):
    for j in range(g):
        for k in range(b):
            print(i, j, k)
            count += 1

# 총 개수 출력
print(count)