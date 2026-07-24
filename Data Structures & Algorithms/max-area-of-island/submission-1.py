class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxarea = 0 
        visited = set() 
        valid_coord = lambda x,y : x < len(grid) and y < len(grid[0]) \
         and x >= 0 and y >= 0 

        def findarea(a,b) :
            dirs = {(-1,0) , (1,0) , (0,1) , (0,-1)}
            area = grid[a][b]
            if area == 0 :
                return 0 
            for dx , dy in dirs :
                nr = a+dx 
                nc = b+dy
                if valid_coord(nr,nc) and (nr,nc) not in visited :
                    visited.add((nr,nc))
                    area += findarea(nr,nc)
            return area 


        for x, r in enumerate( grid ) :
            for y , c in enumerate( r ) :
                if (x, y) not in visited :
                    visited.add((x,y))
                    k = findarea(x,y)
                    maxarea = max( maxarea , k )
                    print(k)

        return maxarea
        