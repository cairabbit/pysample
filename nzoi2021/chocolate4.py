import logging

logging.basicConfig(level=logging.DEBUG)

L, R = map(int, input().split())
N = int(input())
dp = [[[None for i in range(R+1)] for j in range(L+1)] for k in range(N)]
students = []
for x in range(N):
    students.append(list(map(int, input().split())))

def solve(idx, left, right):
    if idx == N:
        return 0

    logging.debug(f'results: {dp}')
    if dp[idx][left][right] is not None:
        logging.debug(f'hit: idx: {idx}, result: {dp[idx][left][right]}')
        return dp[idx][left][right]

    dp[idx][left][right] = -999999999

    if students[idx][1] > 0 and left >= students[idx][0]:
        dp[idx][left][right] = max(dp[idx][left][right], solve(idx + 1,left - students[idx][0], right) + students[idx][1])
    if students[idx][2] > 0 and right >= students[idx][0]:
        dp[idx][left][right] = max(dp[idx][left][right], solve(idx + 1,left, right - students[idx][0]) + students[idx][2])

    return dp[idx][left][right]

print(solve(0, L, R) if solve(0, L, R) > -1 else "Camp is cancelled")