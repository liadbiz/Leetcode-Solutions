class Solution:
    def minSwapsCouples(self, row):
        """
        :type row: List[int]
        :rtype: int
        """
        # find circles
        par = [i + 1 if i % 2== 0 else i - 1 for i in range(len(row))]
        pos = [i if index == r for index in range(len(row)) for i, r in enumerate(row)]
        par_pos = [pos[i] for i in par] # pos of one's parterner
        visited = [0 for i in range(len(row))]
        res = []
        for r in row:
            if not visited[r]:
                t = 1
                tmp = par_pos[r]
                while not visited[par[tmp]]:
                    visited[tmp], visited[par[tmp]] = 1, 1
                    t += 1
                    tmp = par_pos[tmp]
                res.append[t - 1]
        return sum(res)
                    
                    
        