import random
import matplotlib.pyplot as plt

# Функція для симуляції кидків двох кубиків і підрахунку сум
def monte_carlo_simulation(num_simulations):
    results = [0] * 13  # Можливі суми від 2 до 12
    for _ in range(num_simulations):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        sum_dices = dice1 + dice2
        results[sum_dices] += 1
    
    probabilities = [count / num_simulations for count in results]
    return probabilities[2:]  # Повертаємо ймовірності від 2 до 12

# Вхідні дані
num_simulations = 1000000

# Симуляція Монте-Карло
monte_carlo_probs = monte_carlo_simulation(num_simulations)

# Аналітичні розрахунки (за теоретичними значеннями)
analytical_probs = [1/36, 2/36, 3/36, 4/36, 5/36, 6/36, 5/36, 4/36, 3/36, 2/36, 1/36]

# Виведення результатів з різницею
print(f"Number of simulations: {num_simulations}")
print(f"{'Sum':<4} {'Monte Carlo Probability':<25} {'Analytical Probability':<25} {'Difference':<10}")
for sum_value in range(2, 13):
    monte_carlo_prob = monte_carlo_probs[sum_value - 2]
    analytical_prob = analytical_probs[sum_value - 2]
    difference = abs(monte_carlo_prob - analytical_prob)
    print(f"{sum_value:<4} {monte_carlo_prob:.4%} {' '*(23-len(f'{monte_carlo_prob:.4%}'))} {analytical_prob:.4%} {' '*(23-len(f'{analytical_prob:.4%}'))} {difference:.4%}")

# Побудова графіку для порівняння
sums = list(range(2, 13))
plt.plot(sums, monte_carlo_probs, label='Monte Carlo', marker='o')
plt.plot(sums, analytical_probs, label='Analytical', marker='x')
plt.xlabel('Sum of dice')
plt.ylabel('Probability')
plt.title('Comparison of Dice Sums Probabilities')
plt.legend()
plt.grid(True)
plt.show()
