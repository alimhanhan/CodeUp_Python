# 두 개의 정수를 입력받습니다.
a, b = map(int, input().split())

# 입력된 정수를 불리언 값으로 변환합니다.
c = bool(a)
d = bool(b)

# 불리언 값이 서로 다를 경우 True를 출력하고, 그렇지 않으면 False를 출력합니다.
print(c != d)