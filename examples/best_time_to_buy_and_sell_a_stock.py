# Best Time to Buy and Sell Stock

# You are given an array prices where prices[i] represents the price of a given stock on the i-th day.
#
# You want to maximize your profit by:
#
# Choosing a single day to buy one stock.
# Choosing a different day in the future to sell that stock.
# Return:
# The maximum profit you can achieve from this transaction.
# If no profit can be achieved, return 0.

def max_profit(prices):

    #     max_profit = 0
    #
    #     # Greedy case
    #     # for i in range(len(prices)):
    #     #     for j in range(i + 1, len(prices)):
    #     #         diferenca = prices[j] - prices[i]
    #     #         if diferenca > max_diff:
    #     #             max_diff = diferenca
    #
    #     # return max_diff


    if not prices:
        return 0  # Se a lista estiver vazia, lucro é 0

    min_price = float('inf')  # Inicializa com um valor muito alto
    max_profit = 0  # Inicializa o lucro como 0

    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)

    return max_profit

# Exemplo de uso
prices = [7, 1, 5, 3, 6, 4]
print(max_profit(prices))  # Saída esperada: 5 (comprar por 1, vender por 6)





