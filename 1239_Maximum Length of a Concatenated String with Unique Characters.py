import collections


class Solution(object):

    def maxLength(self, arr):
        # Backtracking. LTE
        self.mx = float('-inf')
        
        def isUnique(s):
            return len(s) == len(set(s))

        def bc(r, idx):
            self.mx = max(self.mx, len(r))
            for i in range(idx, len(arr)):
                if isUnique(r + arr[i]):
                    r += arr[i]
                    bc(r, idx + 1)
                    r = r[:-len(arr[i])]
        
        bc('', 0)
    
        return self.mx if self.mx != float('-inf') else 0


s = Solution()
#print(s.maxLength(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p"]))
print(s.maxLength(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k"]))
