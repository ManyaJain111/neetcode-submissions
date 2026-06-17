class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited= set()
        rows= len(grid)
        cols= len(grid[0])
        dir = [(1,0),(0,1),(0,-1),(-1,0)]
        
        
        maxarea=0
        def dfs(r,c):
            area=1
            visited.add((r,c))
            for sr,sc in dir:
                nr= sr+r
                nc= c + sc
                if (0<=nr<rows and 0<=nc<cols and grid[nr][nc]==1 and (nr,nc) not in visited):
                    
                    area= area+ dfs(nr,nc)
            return area        
        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visited and grid[r][c]==1:
                    maxarea=max(maxarea,dfs(r,c))
        return maxarea       

                    
            
                    