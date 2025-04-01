# 두 개의 정수를 입력
a, b = map(int, input().split())

# 두 값이 모두 False일 때 True를 출력
# 정수 0은 False로 평가되므로, a와 b가 모두 0일 때 True를 출력
if not a and not b:
    print(True)
else:
    print(False)