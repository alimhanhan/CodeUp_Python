# 입력받기
a, b, c = map(int, input().split())

# 3항 연산자를 사용하여 가장 작은 값 찾기
smallest = (a if a < b else b) if ((a if a < b else b) < c) else c

# 결과 출력
print(smallest)