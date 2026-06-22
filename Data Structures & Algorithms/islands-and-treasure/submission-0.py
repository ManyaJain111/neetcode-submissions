class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows= len(grid)
        cols= len(grid[0])
        def dfs(r,c,dist):
            if (not 0<=r<rows or not 0<=c<cols or grid[r][c]==-1 or grid[r][c]<dist):
                return
            grid[r][c]= dist
            dfs(r+1,c,dist+1)
            dfs(r-1,c,dist+1)
            dfs(r,c+1,dist+1)
            dfs(r,c-1,dist+1)
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==0:
                    dfs(r,c,0)
        