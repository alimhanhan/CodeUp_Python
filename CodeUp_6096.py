# 바둑판 상태 입력 받기 (19줄)
board = [list(map(int, input().split())) for _ in range(19)]

# 뒤집기 횟수 입력
n = int(input())

# n개의 좌표 입력 받아 처리
for _ in range(n):
    x, y = map(int, input().split())
    
    x -= 1  # 0-based index로 맞춤
    y -= 1

    # 가로 줄 뒤집기
    for i in range(19):
        board[x][i] = 1 - board[x][i]  # 0 ↔ 1

    # 세로 줄 뒤집기
    for i in range(19):
        board[i][y] = 1 - board[i][y]  # 0 ↔ 1

# 출력
for row in board:
    print(' '.join(map(str, row)))