# #403: Frog Jump - with memorization
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        n = len(stones)
        if stones[1] !=1:
            return False
        mp = {}
        for i in range(n):
            if stones[i] not in mp:
                mp[stones[i]] = i
        
        t = [[-1 for _ in range(2002)] for _ in range(2002)]
        def jump(cur_idx, prev_jump):

            if cur_idx == n-1:
                return True

            if t[cur_idx][prev_jump] != -1 :
                return t[cur_idx][prev_jump]
            
            result = False
            for next_jump in range(prev_jump-1,prev_jump+2):
                if next_jump>0:
                    next_stone = stones[cur_idx] + next_jump
                    if next_stone in mp:
                        result = result or jump(mp[next_stone], next_jump)
            
            t[cur_idx][prev_jump] = result
            return result

        return jump(0,0)