# Your algorithms have become so good at predicting the market that you now know what the share price of Wooden Orange Toothpicks Inc.
# (WOT) will be for the next number of days. Each day, you can either buy one share of WOT, sell any number of shares of
# WOT that you own, or not make any transaction at all. What is the maximum profit you can obtain with an optimum trading strategy?


def max_profit(prices):
    max_future_price = 0
    profit = 0

    # Percorrer os preços de trás para frente
    for price in reversed(prices):
        # Se encontramos um preço maior no futuro, atualizamos
        max_future_price = max(max_future_price, price)
        # Se tivermos ações compradas antes de um pico, podemos vendê-las agora
        profit += max_future_price - price

    return profit

# Exemplo de uso
prices = [1, 2, 100]
print(max_profit(prices))  # Saída esperada: 197

