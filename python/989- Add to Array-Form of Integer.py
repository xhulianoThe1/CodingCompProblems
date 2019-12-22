class Solution(object):
    def addToArrayForm(self, A, K):
        a = list(str(int("".join(map(str, A))) + K))
        return [x for x in a]
