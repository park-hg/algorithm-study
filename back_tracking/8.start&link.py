import sys
import math
import itertools

sys.stdin = open('input.txt', 'r')

N = int(sys.stdin.readline())
S = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

ans = math.inf

for team in itertools.combinations(range(N), N//2):
    if 0 in team:
        team_1 = team   
        ability_1 = 0
        for i, j in itertools.combinations(team_1, 2):
            ability_1 += S[i][j]+S[j][i]
       
        team_2 = [member for member in range(N) if member not in team_1]
        ability_2 = 0
        for i, j in itertools.combinations(team_2, 2):
            ability_2 += S[i][j]+S[j][i]

        ans = min(ans, abs(ability_1-ability_2))

print(ans)