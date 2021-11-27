import sys

input = sys.stdin.readline  #입력 형식을 간소화하기 위한 축약 선언

def lcs_length(x, y, m, n): #lcs의 길이를 구하기 위한 재귀함수
    if m == 0 or n == 0:    #m이나 n 중 하나라도 0이면 lcs는 무조건 0
        dp[n][m] = 0
        return dp[n][m] #바로 0 반환
    elif x[m - 1] == y[n - 1]:  #맨 끝이 서로 같으면 무조건 포함되므로 1이 최소 길이
        if dp[n - 1][m - 1] == -1:  #아직 dp에 연산된 값이 없는 상태일 경우
            dp[n - 1][m - 1] = lcs_length(x, y, m - 1, n - 1)   #dp에 연산값 담기
        return 1 + dp[n - 1][m - 1] #dp의 연산값에 1 더한 값이 lcs 길이
    else:   #같은값이 나올때까지 맞추기 위해 x, y의 끝을 각각 하나씩 줄여 더 긴 lcs 길이가 나오는 것을 찾음
        if dp[n - 1][m] == -1:
            dp[n - 1][m] = lcs_length(x, y, m, n - 1)
        if dp[n][m - 1] == -1:
            dp[n][m - 1] = lcs_length(x, y, m - 1, n)
        return max(dp[n - 1][m], dp[n][m - 1])  #두 개 중 더 큰 값이 lcs 길이

m, n = map(int, input().split())    #m, n을 띄어쓰기로 구분해 입력받음
x = list(map(str, input().split())) #x 리스트에 해당하는 값을 띄어쓰기로 구분해 입력받음
y = list(map(str, input().split())) #y 리스트에 해당하는 값을 띄어쓰기로 구분해 입력받음

dp = [[-1] * (m + 1) for _ in range(n + 1)] #메모이제이션을 하기 위한 dp를 (m + 1) * (n + 1)크기로 선언

print(lcs_length(x, y, m, n))