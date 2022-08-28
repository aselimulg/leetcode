# 119. Pascal's Triangle II
# easy
# https://leetcode.com/problems/pascals-triangle-ii/


from typing import List
def getRow(rowIndex: int) -> List[int]:
    def factorial(n: int) -> int:
        total = 1
        while 0 < n:
            total *= n
            n -= 1
        return total
    i = 0
    output = []
    while i <= rowIndex:
        output.append(int(factorial(rowIndex) / (factorial(i) * factorial(rowIndex - i))))
        i += 1
    return output

print(getRow(3))