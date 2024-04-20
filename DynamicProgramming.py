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
    # 메모이제이션: 이미 계산된 값이 있다면 반환
    if memo[n] >= 0:
        return memo[n]
    
    # 기저 사례: 길이가 0이면 가격은 0
    if n == 0:
        return 0
    
    max_price = float('-inf')
    
    # 모든 자르는 위치에 대해 최대 가격을 구함
    for i in range(1, n + 1):
        max_price = max(max_price, price[i] + rodCutMemoization(price, n - i, memo))
    
    # 결과를 메모이제이션
    memo[n] = max_price
    return max_price

def rodCutTabulation(price, n):
    # 최대 가격을 저장할 배열 초기화
    dp = [0] * (n + 1)
    
    # 각 길이에 대한 최대 가격 계산
    for i in range(1, n + 1):
        max_price = float('-inf')
        # 모든 자르는 위치에 대해 최대 가격을 구함
        for j in range(1, i + 1):
            max_price = max(max_price, price[j] + dp[i - j])
        dp[i] = max_price
    
    # 최종 최대 가격 반환
    return dp[n]