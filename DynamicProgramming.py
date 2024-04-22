def fiboMemoization(n,cache):
    if n in cache:
        return cache[n]
    
    if n<=1:
        cache[n]=n
    else:
        cache[n]=fiboMemoization(n-1,cache)+fiboMemoization(n-2,cache)    
    return cache[n]


def fiboTabulation(n):
    table=[0]*(n+1)
    table[1]=1
    
    if n<=1:
        return table[n]
    for i in range(2,n+1):
        table[i]=table[i-1]+table[i-2]
    return table[n]

def rodCutMemoization(price, n, memo):
    if memo[n] >= 0:
        return memo[n]
    
    if n == 0:
        return 0
    
    max_price = 0  # 0으로 초기화
    
    for i in range(1, n + 1):
        current_price = price[i] + rodCutMemoization(price, n - i, memo)
        if current_price > max_price:  # 최대값 갱신
            max_price = current_price
    
    memo[n] = max_price
    return max_price

def rodCutTabulation(price, n):
    dp = [0] * (n + 1)
    dp[0]=0
    for i in range(1, n + 1):
        max_price = float('-inf') # 0으로 초기화
        for j in range(1, i + 1):
            current_price = price[j] + dp[i - j]
            if current_price > max_price:  # 최대값 갱신
                max_price = current_price
        dp[i] = max_price
    
    return dp[n]

price = [0, 1, 2, 8, 2, 3]
arr = [-1] * (len(price) + 1)  # 메모이제이션용 배열 초기화

print(rodCutMemoization(price, 3, arr))
print("\n")
print(rodCutTabulation(price, 3))

arr=[0]*11
print(fiboMemoization(5,arr))
print("\n")
print(fiboTabulation(6))