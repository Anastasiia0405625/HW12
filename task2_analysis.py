import numpy as np

# Income of three departments for ten months
income = np.array([
    [10000, 11000, 12000, 13000, 14000, 15000, 16000, 17000, 18000, 19000],
    [15000, 15500, 16000, 16500, 17000, 17500, 18000, 18500, 19000, 19500],
    [20000, 21000, 22000, 23000, 24000, 25000, 26000, 27000, 28000, 29000]
])

average_income = np.mean(income, axis=1)
total_income = np.sum(income, axis=1)

for i in range(len(income)):
    print(f"Department {i + 1}:")
    print(f"  Average monthly income: {average_income[i]:.2f}")
    print(f"  Total income: {total_income[i]:.2f}")
