# week01-3.py 厩策璸礶 Array/String 材2肈
# LeetCode 1071. Greatest Common Divisor of Strings
# 程そ计 gcd ﹃
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # 蛤程そ计 gcd Τ闽
        N1, N2 = len(str1), len(str2)
        N = gcd(N1, N2)
        ans = str1[:N]

        if ans*(N1//N) != str1: return ""
        if ans*(N2//N) != str2: return ""
        return ans
