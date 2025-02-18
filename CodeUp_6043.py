# 두 개의 실수를 입력받아 공백을 기준으로 분리한 후, float형으로 변환
f1, f2 = map(float, input().split())

# f1을 f2로 나눈 값을 계산
result = f1 / f2

# 계산된 결과를 소숫점 넷째자리에서 반올림하여 소숫점 셋째 자리까지 출력
print("{:.3f}".format(result))
