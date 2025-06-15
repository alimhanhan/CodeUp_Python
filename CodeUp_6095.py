# 19x19 바둑판을 0으로 초기화
board = [[0 for _ in range(19)] for _ in range(19)]

n = int(input())  # 흰 돌의 개수 입력

for _ in range(n):
    x, y = map(int, input().split())  # 좌표 입력 (1~19)
    board[x - 1][y - 1] = 1  # 리스트는 0부터 시작하므로 -1 보정

# 바둑판 상태 출력
for i in range(19):
    for j in range(19):
        print(board[i][j], end=' ')
    print()