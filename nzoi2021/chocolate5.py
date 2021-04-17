import logging

logging.basicConfig(level=logging.DEBUG)

L,R = map(int, input().split())
N = int(input())
students = []
cups = [0]
dp = [[None]*(L+1) for x in range(N+1)]
for x in range(N):
    students.append(list(map(int, input().split())))
    cups.append(cups[-1] + students[-1][0])

def solve(idx, left):
    if idx == N: return 0
    if dp[idx][left] is not None: return dp[idx][left]
    right = L + R - left - cups[idx]
    dp[idx][left] = -99999999999
    if students[idx][1] > 0 and left >= students[idx][0]:
        dp[idx][left] = max(dp[idx][left], solve(idx + 1, left - students[idx][0]) + students[idx][1])
    if students[idx][2] > 0 and right >= students[idx][0]:
        dp[idx][left] = max(dp[idx][left], solve(idx + 1, left) + students[idx][2])
    return dp[idx][left]

print("Camp is cancelled" if solve(0, L) < 0 else solve(0, L))
