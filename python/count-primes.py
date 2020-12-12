# question can be found on leetcode.com/problems/count-primes/


class Solution:
    def countPrimes(self, n: int) -> int:
        holder = [1] * n
        holder[0] = holder[1] = 0

        for number in range(2, int(n**0.5)+1):
            if holder[number] == 1:
                for n in range(number**2, n, number):
                    holder[n] = 0
        
        return sum(holder)
