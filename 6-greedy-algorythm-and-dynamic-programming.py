# Дані про їжу
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

# Жадібний алгоритм для вибору страв
def greedy_algorithm(items, budget):
    # Сортування страв за зменшенням співвідношення калорій до вартості
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    selected_items = []
    total_cost = 0
    total_calories = 0

    for item, details in sorted_items:
        if total_cost + details['cost'] <= budget:
            selected_items.append(item)
            total_cost += details['cost']
            total_calories += details['calories']

    return selected_items, total_cost, total_calories

# Алгоритм динамічного програмування для вибору страв
def dynamic_programming(items, budget):
    # Кількість страв
    n = len(items)
    # Імена страв
    names = list(items.keys())
    # Вартість і калорії кожної страви
    costs = [items[name]['cost'] for name in names]
    calories = [items[name]['calories'] for name in names]

    # Ініціалізація таблиці DP (dynamic programming)
    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]

    # Заповнення таблиці DP
    for i in range(1, n + 1):
        for w in range(1, budget + 1):
            if costs[i - 1] <= w:
                dp[i][w] = max(calories[i - 1] + dp[i - 1][w - costs[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    # Зворотний прохід для визначення вибраних страв
    selected_items = []
    w = budget
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(names[i - 1])
            w -= costs[i - 1]

    total_calories = dp[n][budget]
    total_cost = sum(items[item]['cost'] for item in selected_items)
    selected_items.reverse()

    return selected_items, total_cost, total_calories

# Приклад використання
budget = 100

# Використання жадібного алгоритму
greedy_items, greedy_cost, greedy_calories = greedy_algorithm(items, budget)
print("Greedy Algorithm:")
print("Selected items:", greedy_items)
print("Total cost:", greedy_cost)
print("Total calories:", greedy_calories)

# Використання алгоритму динамічного програмування
dp_items, dp_cost, dp_calories = dynamic_programming(items, budget)
print("\nDynamic Programming:")
print("Selected items:", dp_items)
print("Total cost:", dp_cost)
print("Total calories:", dp_calories)
