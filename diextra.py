vershin = int(input("Вершин: "))
reber = int(input("Ребер: "))

graf = [[] for i in range(vershin + 1)]

print("Введите (вершина1 вершина2 вес):")
for i in range(reber):
    a, b, ves = map(int, input().split())
    graf[a].append([b, ves])
    graf[b].append([a, ves])

start = int(input("Стартовая вершина: "))

dist = [1000000] * (vershin + 1)
visited = [False] * (vershin + 1)
dist[start] = 0

for i in range(vershin):
    min_dist = 1000000
    u = -1
    for j in range(1, vershin + 1):
        if not visited[j] and dist[j] < min_dist:
            min_dist = dist[j]
            u = j
    if u == -1:
        break
    visited[u] = True

    for v, ves in graf[u]:
        if dist[u] + ves < dist[v]:
            dist[v] = dist[u] + ves

print("Кратчайшие расстояния:")
for i in range(1, vershin + 1):
    print("До", i, ":", dist[i])