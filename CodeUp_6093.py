n = int(input())            # 부른 횟수
a = input().split()         # 부른 번호들을 문자열 리스트로 입력받음

for i in range(n):
    a[i] = int(a[i])        # 정수로 변환

d = [0] * 24                # 0번 인덱스는 사용하지 않음 (1~23번까지 사용)

for i in range(n):
    d[a[i]] += 1            # 해당 번호에 대한 카운트 증가

for i in range(1, 24):      # 1번부터 23번까지 출력
    print(d[i], end=' ')