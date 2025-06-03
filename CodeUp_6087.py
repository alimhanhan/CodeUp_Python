n = int(input())  # 입력 받기

s = 0  # 합을 저장할 변수
c = 1  # 더할 수를 나타내는 변수

while True:
    s += c
    c += 1
    if s >= n:
        break

print(s)