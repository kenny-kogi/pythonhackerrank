class ArithmeticInterface:
    def getDivision(self, n):
        pass

class Solution(ArithmeticInterface):
    def getDivision(self, n):
        summ = 0
        for i in range(1, n + 1):
            if (n % i == 0):
                summ += i
        return summ


n = int(input())
myobj = Solution()
result = myobj.getDivision(n)
print(result)

