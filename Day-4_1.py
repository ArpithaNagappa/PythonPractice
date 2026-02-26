## 1356. Sort Integers by The Number of 1 Bits
## You are given an integer array arr. Sort the integers in the array in ascending order by the number of 1's in their binary representation and in case of two or more integers have the same ## number of 1's you have to sort them in ascending order.

## Return the array after sorting it.


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        data = {}
        pairs=[]
        ints_sorted=[]
        arr=sorted(arr)
        for n in arr:
            pairs.append((n,format(n, '08b').count('1')))
        sorted_pairs = sorted(pairs, key=lambda x: x[1])
        for key, value in sorted_pairs:
            ints_sorted.append(key)
        return ints_sorted