class Solution(object):
    # Solution 1. 递归求combo(n-1)然后和n代表的数字组合
    # Solution 2. 非递归求combo(n-1)然后和n代表的数字组合
    # Solution 3. 递归逐次求COMBO
    # Solution 4. Backtracking (DFS)
    
    
    def letterCombinations(self, digits):
        if not digits: return []
        
        nums = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv","9":"wxyz"}
        result = []
        
        def combine(s, digits):
            if not digits:
                result.append(s)
                return
            else:
                for n in nums[digits[0]]:
                    combine(s+n, digits[1:])
        
        combine("", digits)
        return result
    
    def letterCombinationsNonRecurExtraSpace(self, digits):
        nums = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv","9":"wxyz"}
        prev = []
        for d in digits:
            if not prev: 
                prev.extend(list(nums[d]))
            else:
                r = []
                for c in nums[d]:
                    for s in prev:
                        r.append(s+c)
                prev = r
        
        return prev
                        
            
    def letterCombinationsDFS(self, digits):
        if not digits: return []
        
        nums = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv","9":"wxyz"}
        result = []
        def bc(i, s):
            for c in nums[digits[i]]:
                s += c
                if i == len(digits)-1:
                    result.append(s)
                else:
                    bc(i+1, s)
                s = s[:-1]
        
        bc(0, "")
        
        return result
                
    def letterCombinationsRecurExtraSpace(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        d = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv","9":"wxyz"}
        
        if not digits: return []
        if len(digits) == 1:
            return list(d[digits[0]])
        else:
            r = []
            prev = self.letterCombinations(digits[:-1])
            for s in prev:
                for c in d[digits[-1]]:
                    r.append(s+c)
            
            return r
        