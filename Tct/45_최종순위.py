from collections import deque

for tc in range(int(input())):
    n = int(input())
    # 모든 노드에 대한 진입차수는 0으로 초기화
    indegree = [0] * (n+1)
    # 각 노드에 연결된 간선 정보를 담기 위한 인접 행렬 초기화
    graph = [[False] * (n+1) for _ in range(n+1)]
    data = list(map(int, input().split()))
    for i in range(n):
        for j in range(i+1, n):
            graph[data[i]][data[j]] = True
            indegree[data[j]] += 1

    # 올해 변경된 순위 정보 입력
    m = int(input())
    for i in range(m):
        a, b = map(int, input().split())
        if graph[a][b]:
            graph[a][b] = False
            graph[b][a] = True
            indegree[a] += 1
            indegree[b] -= 1
        else:
            graph[a][b] = True
            graph[b][a] = False
            indegree[a] -= 1
            indegree[b] += 1

    result = []
    q = deque()

    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    certain = True  # 위상 정렬 결과가 오직 하나인지의 여부
    cycle = False   # 그래프 내 사이클이 존재하는지 여부

    for i in range(n):
        if len(q) == 0:  # 큐가 비어 있다면 사이클이 발생했다는 의미
            cycle = True
            break
        if len(q) >= 2:  # 큐의 원소가 2개 이상이라면 가능한 정렬 결과가 여러 개라는 의미
            certain = False
            break
        now = q.popleft()
        result.append(now)
        for j in range(1, n+1):  # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
            if graph[now][j]:
                indegree[j] -= 1
                if indegree[j] == 0:    # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
                    q.append(j)

    if cycle:   # 사이클이 발생하는 경우(일관성이 없는 경우)
        print("IMPOSSIBLE")
    elif not certain:   # 위상 정렬 결과가 여러 개인 경우
        print("?")
    else:   # 위상 정렬을 수행한 결과 출력
        for i in result:
            print(i, end=' ')
        print()
