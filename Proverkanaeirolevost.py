vershin = int(input("Вершин: "))
reber = int(input("Ребер: "))

graf = [ [] for i in range(vershin + 1) ]

print("Введите каждое ребро ввида: вершина1 вершина2:")
for i in range(reber):
    a, b = map(int, input().split())
    graf[a].append(b)
    graf[b].append(a)

nechet = 0
for i in range(1, vershin + 1):
    stepen = len(graf[i])
    if stepen % 2 != 0:
        nechet = nechet + 1

print("Ответ:")
if nechet == 0:
    print("по циклу: все вершины четные и можно вернуться в начало.")
elif nechet == 2:
    print("По пути: ровно две нечетные вершины путь может быть.")
else:
    print("Путь не может быть так как нечетных вершин", nechet)