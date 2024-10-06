t = int(input())

def find_min_cost(n, price_list):
    dp = [float('inf')] * (n + 1)
    dp[0] = 0 
    for i in range(1, n + 1):
        for bundle_size, price in price_list:
            if i >= bundle_size:
                dp[i] = min(dp[i], dp[i - bundle_size] + price)
    return dp[n]

for i in range(t):
    n, prices_count = map(int, input().split())
    prices = list(map(int, input().split()))
    price_list = [(i + 1, prices[i]) for i in range(prices_count)]
    min_cost = find_min_cost(n, price_list)
    print(min_cost)







