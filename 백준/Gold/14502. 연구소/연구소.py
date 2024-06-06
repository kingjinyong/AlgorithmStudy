import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs():
    queue = deque()
    c_graph = [row[:] for row in graph]  # deepcopy 대신 리스트 슬라이싱 사용

    for i in range(n):
        for j in range(m):
            if c_graph[i][j] == 2:
                queue.append((i, j))

    while queue:
        x, y = queue.popleft()

        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < n and 0 <= ny < m and c_graph[nx][ny] == 0:
                c_graph[nx][ny] = 2
                queue.append((nx, ny))

    return sum(row.count(0) for row in c_graph)

def wall(cnt, start):
    global answer
    if cnt == 3:
        answer = max(answer, bfs())
        return
    
    for i in range(start, n * m):  # 1차원으로 처리하여 중복을 줄임
        x, y = divmod(i, m)
        if graph[x][y] == 0:
            graph[x][y] = 1
            wall(cnt + 1, i + 1)  # 다음 시작점을 i+1로 설정
            graph[x][y] = 0

answer = 0
wall(0, 0)
print(answer)
