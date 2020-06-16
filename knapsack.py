def knapsack(w, v, W, n):
    if n==0 or W==0:
        return 0
    if w[n-1]>W:
        return knapsack(w, v, W, n-1)
    if w[n-1]<=W:
        return max(v[n-1] + knapsack(w, v, W - w[n-1], n-1), knapsack(w, v, W, n-1))

print(knapsack([10, 20, 30, 40], [7, 6, 9, 4], 70, 4))
