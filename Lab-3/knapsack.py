import random

class Item:
    def __init__(self, index, weight, profit):
        self.index = index
        self.weight = weight
        self.profit = profit
        self.ratio = profit / weight

def greedy_by_weight(weights, profits, capacity):
    # Create a list of indices sorted by weight
    item_indices = sorted(range(len(weights)), key=lambda i: weights[i])
    total_profit = 0.0
    remaining_capacity = capacity
    items_taken = []
    ratios = [0] * len(weights)

    for i in item_indices:
        if remaining_capacity == 0:
            break
        amount_taken = min(weights[i], remaining_capacity)
        ratio = amount_taken / weights[i]
        total_profit += ratio * profits[i]
        remaining_capacity -= amount_taken
        items_taken.append((i, weights[i], amount_taken))
        ratios[i] = ratio

    return total_profit, items_taken, tuple(ratios)

def greedy_by_profit(weights, profits, capacity):
    # Create a list of indices sorted by profit
    item_indices = sorted(range(len(profits)), key=lambda i: profits[i], reverse=True)
    total_profit = 0.0
    remaining_capacity = capacity
    items_taken = []
    ratios = [0] * len(weights)

    for i in item_indices:
        if remaining_capacity == 0:
            break
        amount_taken = min(weights[i], remaining_capacity)
        ratio = amount_taken / weights[i]
        total_profit += ratio * profits[i]
        remaining_capacity -= amount_taken
        items_taken.append((i, weights[i], amount_taken))
        ratios[i] = ratio

    return total_profit, items_taken, tuple(ratios)

def optimal_solution(weights, profits, capacity):
    # Create a list of Item objects with indexes
    items = [Item(i, weights[i], profits[i]) for i in range(len(weights))]
    items.sort(key=lambda x: x.ratio, reverse=True)
    total_profit = 0.0
    remaining_capacity = capacity
    items_taken = []
    ratios = [0] * len(weights)

    for item in items:
        if remaining_capacity == 0:
            break
        amount_taken = min(item.weight, remaining_capacity)
        ratio = amount_taken / item.weight
        total_profit += amount_taken * item.ratio
        remaining_capacity -= amount_taken
        items_taken.append((item.index, item.weight, amount_taken))
        ratios[item.index] = ratio

    return total_profit, items_taken, tuple(ratios)

def main():
    # Input number of items
    n = int(input("Enter the number of items: "))

    # Generate random weights and profits
    weights = [random.uniform(1, 100) for _ in range(n)]
    profits = [random.uniform(10, 500) for _ in range(n)]

    # Input the capacity of the knapsack
    capacity = float(input("Enter the capacity of the knapsack: "))

    # Display the randomly generated weights and profits
    print("\nRandomly generated weights and profits:")
    for i in range(n):
        print(f"Item {i+1}: Weight = {weights[i]:.2f}, Profit = {profits[i]:.2f}")

    # Calculate the results
    max_profit_weight, items_taken_weight, ratios_weight = greedy_by_weight(weights, profits, capacity)
    max_profit_profit, items_taken_profit, ratios_profit = greedy_by_profit(weights, profits, capacity)
    max_profit_optimal, items_taken_optimal, ratios_optimal = optimal_solution(weights, profits, capacity)
    
    # Output the results
    print(f"\nGreedy by Weight:")
    print(f"Maximum profit: {max_profit_weight:.2f}")
    print("Items taken (index, weight, amount taken):")
    for item in items_taken_weight:
        print(f"Index: {item[0]}, Weight: {item[1]}, Amount taken: {item[2]}")
    print(f"Ratios of items taken: {ratios_weight}")

    print(f"\nGreedy by Profit:")
    print(f"Maximum profit: {max_profit_profit:.2f}")
    print("Items taken (index, weight, amount taken):")
    for item in items_taken_profit:
        print(f"Index: {item[0]}, Weight: {item[1]}, Amount taken: {item[2]}")
    print(f"Ratios of items taken: {ratios_profit}")

    print(f"\nOptimal Solution:")
    print(f"Maximum profit: {max_profit_optimal:.2f}")
    print("Items taken (index, weight, amount taken):")
    for item in items_taken_optimal:
        print(f"Index: {item[0]}, Weight: {item[1]}, Amount taken: {item[2]}")
    print(f"Ratios of items taken: {ratios_optimal}")

if __name__ == "__main__":
    main()
