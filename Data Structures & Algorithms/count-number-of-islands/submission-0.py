class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        isls=0
        rows= len(grid)
        cols= len(grid[0])
        dir=[(1,0),(0,1),(0,-1),(-1,0)]
        visited= set()
        def dfs(r,c):
            visited.add((r,c))
            for sr,sc in dir:
                nr= sr+ r
                nc= sc+c
                if (0<=nr<rows and 0<=nc<cols and grid[nr][nc]=="1" and (nr,nc) not in visited):
                    dfs(nr,nc)
        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visited and grid[r][c]=="1":
                    isls= isls+1
                    dfs(r,c)
        return isls