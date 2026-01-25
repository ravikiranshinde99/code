# #3447: Assign Elements to Groups with Constraints
# store each factor in hashmap
class Solution:
    def assignElements(self, groups: List[int], elements: List[int]) -> List[int]:
        mp = {}
        max_num = max(groups) 
        for i, e in enumerate(elements):
            num = e
            if e not in mp:
                while e <= max_num:       #This iterates over every multiple of elements (1e,2e,3e...) and stores that in map
                    if e not in mp:
                        mp[e] = i
                    e += num

        res = []
        for e in groups:             # n complexity
            if e not in mp:          # log(n) complexity
                res.append(-1)
            else:
                res.append(mp[e])
                
        return res