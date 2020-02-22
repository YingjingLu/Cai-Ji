class Solution:
    def maxSatisfied(self, customers, grumpy, X):
        if len(grumpy) <= X:
            return sum(customers)

        dp = [sum([customers[i] * grumpy[i] for i in range(X)])]
        for i in range(1, len(grumpy) - X + 1):
            dp.append(dp[i - 1] + customers[i + X - 1] * grumpy[i + X - 1] - customers[i - 1] * grumpy[i - 1])

        return max(dp) + sum([(grumpy[i] ^ 1) * customers[i] for i in range(len(grumpy))])