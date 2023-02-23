def maxProfit(prices):
    buy = 0
    sell = 1
    max_profit = 0
    
    while sell < len(prices):
        current_profit = prices[sell] - prices[buy]

        if prices[sell] > prices[buy]:
            max_profit = max(current_profit, max_profit)
        else:
            buy = sell
        sell += 1

    return max_profit

prices = [7,2,1,4]
profit = maxProfit(prices)
print(profit)