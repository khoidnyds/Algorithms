def RecursiveFibonacci(size):
    if size == 0:
        return 0
    if size == 1:
        return 1
    return RecursiveFibonacci(size-1) + RecursiveFibonacci(size-2)


def DynamicProgrammingFibonacci(size):
    dp = [0]*(size+1)
    dp[1] = 1
    for i in range(2, size+1):
        dp[i] = (dp[i-1]+dp[i-2]) % 10
    return dp[size]


size = 91239
print(DynamicProgrammingFibonacci(size))
