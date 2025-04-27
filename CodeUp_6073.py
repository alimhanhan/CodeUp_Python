n = int(input()) # 정수 1개 입력

# 입력받은 수에서 1을 뺀 값부터 시작
# 예: 입력이 5이면 4부터 시작
count = n - 1

# count 값이 0보다 크거나 같을 동안 반복
while count >= 0:
  print(count) # 현재 count 값을 출력
  count -= 1   # count 값을 1 감소