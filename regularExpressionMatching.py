class Solution:
    # TC : O(m*n)
    # SC : O(m*n)
    def isMatch(self, s: str, p: str) -> bool:
        if s == p:
            return True
        m,n = len(s),len(p)
        dp = [[False]*(n+1)]*(m+1)
        dp[0][0] = True
        # fill  1st column
        for j in range(1,n+1):
            if p[j-1] == "*":
                dp[0][j] = dp[0][j-2]
        for i in range(1,m+1):
            for j in range(1,n+1):
                if s[i-1] == p[j-1] or p[j-1] == ".":
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == "*":
                    dp[i][j] = dp[i][j-2]
                    if p[j-2] == s[i-1] or p[j-2] == ".":
                        dp[i][j] = dp[i][j] or dp[i-1][j]
        return dp[m][n]
