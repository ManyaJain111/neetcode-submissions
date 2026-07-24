class Solution:
    def dfs(self,r,c,rows,cols,grid,visited): 
        dir= [(1,0),(0,1),(-1,0),(0,-1)]   
        for sr,sc in dir:
            nr= sr+ r
            nc= sc+ c
            if ((0<=nr<rows) and (0<=nc<cols) and grid[nr][nc]=="1"and (nr,nc) not in visited):
                visited.add((nr,nc))
                self.dfs(nr,nc,rows,cols,grid,visited)

                
    def numIslands(self, grid: List[List[str]]) -> int:
        
        rows= len(grid)
        count=0
        cols= len(grid[0])
        visited= set()
        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visited and grid[r][c]=="1":
                    count= count+1
                    self.dfs(r,c,rows,cols,grid,visited)
        return count

        