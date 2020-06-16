# Dijkstra for the problem: 
# s-> Source node
# d-> Destination node
# a-> Maximum weight of roads to be A from source
# b-> Minimum weight of roads to be B from destination
# Goal: To find the mimumum weighted path that satisfies above conditions, or -1 if no such path exists.

from queue import PriorityQueue

INF = 10000000000000
n, m = map(int, input().split())
adj = [[] for i in range(n + 5)]
pq = PriorityQueue()

for we in range(m):
    u_i, v_i, w_i = map(int, input().split())
    adj[u_i].append([v_i, w_i])
    adj[v_i].append([u_i, w_i])
s, t, a, b = map(int, input().split())
d1 = [INF for i in range(n + 5)]
d2 = [INF for i in range(n + 5)]
d1[s] = 0
d2[t] = 0
pq.put((d1[s], s))

while pq.qsize() != 0:
    y = pq.get()
    d1[y[1]] = y[0]
    for x in adj[y[1]]: 
        if d1[x[0]] > y[0] + x[1] and x[1] <= a:
            d1[x[0]] = y[0] + x[1]
            pq.put((d1[x[0]], x[0]))
pq.put((d2[t], t))

while pq.qsize() != 0:
    y = pq.get()
    d2[y[1]] = y[0]
    for x in adj[y[1]]:
        if d2[x[0]] > y[0] + x[1] and x[1] >= b:
            d2[x[0]] = y[0] + x[1]
            pq.put((d2[x[0]], x[0]))

ans = INF
for i in range(1, n + 1):
    ans = min(ans, d1[i] + d2[i])
if ans >= INF:
    ans = -1
print(ans)
