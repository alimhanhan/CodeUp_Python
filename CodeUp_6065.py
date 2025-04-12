# 입력받기
a, b, c = input().split()

# 정수형으로 변환
a = int(a)
b = int(b)
c = int(c)

# 짝수 출력
if a % 2 == 0:
    print(a)

if b % 2 == 0:
    print(b)

if c % 2 == 0:
    print(c)