class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows= len(grid)
        isls=0
        dir= [(1,0),(0,1),(-1,0),(0,-1)]
        cols= len(grid[0])
        visited= set()
        def dfs(row,col):
            visited.add((row,col))
            for sr,sc in dir:
                nc= sc+col
                nr= sr+row
                if (0<=nr<rows and 0<=nc<cols and (nr,nc) not in visited and grid[nr][nc]=="1"):
                    dfs(nr,nc)
        for row in range(rows) :
            for col in range(cols):
                if (row,col) not in visited and grid[row][col]=="1":
                    dfs(row,col)
                    isls= isls+1
        

        return isls






        
        
        