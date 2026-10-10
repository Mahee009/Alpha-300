def maximum_wealth(accounts):
    richest = 0
    for customer in accounts:
        wealth = 0
        for money in customer:
            wealth += money
        if wealth > richest:
            richest = wealth
    return richest


print(maximum_wealth([[1, 2, 3], [3, 2, 1]]))
print(maximum_wealth([[1, 5], [7, 3], [3, 5]]))
