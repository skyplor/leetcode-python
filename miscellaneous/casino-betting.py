class Solution:
    def get_min_rounds(self, n: int, k: int) -> int:
        res = 0
        while n > 1 and k > 0:
            if n % 2 != 0:
                n -= 1
            else:
                n //= 2
                k -= 1
            res += 1
            
        res += n - 1
        return res
        
sol = Solution()
n = 8
k = 2
output = sol.get_min_rounds(n, k)
print(f'output: {output}')
