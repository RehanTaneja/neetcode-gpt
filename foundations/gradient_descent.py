class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        i = 0
        curr = init
        while i < iterations:
            curr -= 2*learning_rate*curr
            i+=1
        return round(curr,5)   