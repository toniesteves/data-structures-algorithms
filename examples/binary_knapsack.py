# An investor has saved some money and wants to invest in the stock market.
# There are a number of stocks to choose from, and they want to buy at most 1 share in any company.
# The total invested cannot exceed the funds available. A friend who is a stock market expert has predicted
# the value of each stock after 1 year. Determine the maximum profit that can be earned at the end of the year
# assuming the predictions come true.



def selectStock(saving, currentValue, futureValue):
    n = len(currentValue)
    profits = [futureValue[i] - currentValue[i] for i in range(n)]

    print(f"Profits: {currentValue}")
    print(f"Profits: {profits}")

    dp = [0] * (saving + 1)

    for i in range(n):
        curr_val, profit = currentValue[i], profits[i]
        print(f"Curr Val/Profit: {curr_val} - {profit}")
        if profit > 0:
            for w in range(saving, curr_val-1, -1):
                print(f"{w}: max Between: {dp[w]} and {profit + dp[w - curr_val]}")
                dp[w] = max(dp[w], profit + dp[w - curr_val])

    return dp[saving]

def main():

    saving        = 250
    current_value = [175, 133, 109, 201, 97]
    future_value  = [200, 125, 128, 228, 133]

    # saving        = 10
    # current_value = [3, 2, 5, 7]
    # future_value  = [8, 6, 7, 10]


    print(selectStock(saving, current_value, future_value))

if __name__ == "__main__":
    main()