## 1404. Number of Steps to Reduce a Number in Binary Representation to One
## Given the binary representation of an integer as a string s, return the number of steps to reduce it to 1 under the following rules:

## If the current number is even, you have to divide it by 2.

## If the current number is odd, you have to add 1 to it.

## It is guaranteed that you can always reach one for all test cases.

class Solution:
    def numSteps(self, s: str) -> int:
        cnt = 0
        nbr = int(s, 2)
        while nbr != 1:
            cnt = cnt + 1
            if(nbr%2==0):
                nbr = nbr//2
            else:
                nbr = nbr + 1
        return cnt