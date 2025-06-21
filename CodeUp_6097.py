# 격자판 크기 입력
h, w = map(int, input().split())

# 격자판 초기화 (0으로)
grid = [[0] * w for _ in range(h)]

# 막대 개수 입력
n = int(input())

# 막대 정보 입력 및 배치
for _ in range(n):
    l, d, x, y = map(int, input().split())
    x -= 1  # 0-based 인덱스로 변환
    y -= 1

    for i in range(l):
        if d == 0:  # 가로 방향
            grid[x][y + i] = 1
        else:       # 세로 방향
            grid[x + i][y] = 1

# 결과 출력
for row in grid:
    print(' '.join(map(str, row)))
