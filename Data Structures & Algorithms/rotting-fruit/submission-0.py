from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows= len(grid)
        visited=set()
        cols= len(grid[0])
        minutes=0
        q= deque()
        for r in range(rows):
            for c in  range(cols):
                if grid[r][c]==2:
                    q.append((r,c))

        dir= [(1,0),(0,1),(-1,0),(0,-1)]
        while q:
            changed= False
            for _ in range(len(q)):
                noder,nodec= q.popleft()
                for dr,dc in dir:
                    nr= dr+noder
                    nc= dc+nodec
                    if (0<=nr<rows and 0<=nc<cols and grid[nr][nc]==1):
                        grid[nr][nc]=2
                        visited.add((nr,nc))
                        q.append((nr,nc))
                        changed= True
                        
            if changed:
             minutes =minutes+1
            
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    return -1
        return minutes

            

            
