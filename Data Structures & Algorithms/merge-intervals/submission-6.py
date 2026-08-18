class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        res = []

        intervals = sorted(intervals,key= lambda x: x[0])
        
        for i in range(len(intervals)):
            
            s, e = intervals[i][0], intervals[i][1] #1,4

            if not res or res[-1][1]<s: 
                res.append([s,e]) #1,4
            else:
                res[-1][1] = max(e,res[-1][1])

        return res

