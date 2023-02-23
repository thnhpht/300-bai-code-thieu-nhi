def coinChange(coins, amount):
    if amount == 0:
        return 0
    
    val1 = [0]
    val2 = []
    visited =  [False] * amount
    visited[0] = True
    count = 0

    while val1:
        count += 1
        for n in val1:
            for coin in coins:
                new_val = n + coin
                if new_val == amount:
                    return count
                elif new_val > amount:
                    continue
                elif not visited[new_val]:
                    visited[new_val] = True
                    val2.append(new_val)
        val1, val2 = val2, []

coins = [186,419,83,408]
amount = 6249
print(coinChange(coins, amount))