import matplotlib.pyplot as plt


def price_ways(n, d):
    if n <= 0:
        return 0

    price = [0] * (n + 1)
    for i in range(1, n + 1):
        price[i] = price[i - 1] + d

    dp = [0] * (n + 1)
    dp[1] = price[1]
    dp[2] = price[2] + dp[1]
    dp[3] = min(dp[2], dp[1]) + price[3]

    path = [[] for _ in range(n + 1)]
    path[1] = [1]
    path[2] = [1, 2]
    path[3] = [1, 3]

    for i in range(3, n + 1):
        dp[i] = min(dp[i - 1], dp[i - 3]) + price[i]
        if dp[i - 1] < dp[i - 3]:
            path[i] = path[i - 1] + [i]
        else:
            path[i] = path[i - 3] + [i]
        if i % 2 == 0:
            if dp[i // 2] + price[i] < dp[i]:
                dp[i] = dp[i // 2] + price[i]
                path[i] = path[i // 2] + [i]

    price_optimal_path = [price[i] for i in path[n]]
    ind_optim_path = path[n]

    return dp[n], price_optimal_path, ind_optim_path


n = int(input('Введите значение n: '))
d = int(input('Введите значение d: '))
result, prices, indices = price_ways(n, d)

full_price = [0] * len(prices)

for i in range(len(full_price)):
    full_price[i] = full_price[i - 1] + prices[i]

print(f'Минимальная сумма достигала {n}: {result}')
print('Цены за выбранные ступеньки:', full_price)
print('Индексы выбранных ступенёк:', indices)
print('Полная цена за выбранные ступеньки:', full_price)

x = indices
y = full_price


plt.scatter(x, y, color='brown', marker='*', label='Выбранные ступеньки')
plt.plot(x, y, color='burlywood')
plt.xlabel('Индексы ступенек')
plt.ylabel('Минимальная цена')
plt.title('Оптимальные решение')
plt.legend()
plt.show()