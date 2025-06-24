# 미로 입력 받기
maze = [list(map(int, input().split())) for _ in range(10)]

# 개미 시작 위치 (2,2) → (1,1) (0-based index)
x, y = 1, 1

while True:
    if maze[x][y] == 0:
        maze[x][y] = 9
    elif maze[x][y] == 2:
        maze[x][y] = 9
        break

    # 오른쪽 먼저 보기
    if maze[x][y + 1] != 1:
        y += 1
    # 오른쪽이 벽이면 아래로
    elif maze[x + 1][y] != 1:
        x += 1
    # 둘 다 벽이면 종료
    else:
        break

# 결과 출력
for row in maze:
    print(' '.join(map(str, row)))
