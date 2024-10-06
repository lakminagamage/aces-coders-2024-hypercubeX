def min_prefix_count(words, target):
    memo = {}
    
    def dfs(i):
        if i == len(target):
            return 0
        if i in memo:
            return memo[i]
        
        min_count = float('inf')
        
        for word in words:
            if target.startswith(word, i):
                result = dfs(i + len(word))
                if result != -1:
                    min_count = min(min_count, result + 1)
        
        memo[i] = min_count if min_count != float('inf') else -1
        return memo[i]
    
    return dfs(0)

n = int(input())
words = [input() for i in range(n)]
target = input()


print(min_prefix_count(words, target))
