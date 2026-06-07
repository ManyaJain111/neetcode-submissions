class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def search(row,matrix,target,left,right):
            if left>right:
                return False
            mid= (left+right)//2
            if matrix[row][mid]== target:
                return True
            else:
                if matrix[row][mid]<target:
                    return search(row,matrix,target,mid+1,right)
                else:
                    return search(row,matrix,target,left,mid-1)

        for row in range(len(matrix)):
            if matrix[row][0]== target :
                return True
            if matrix[row][-1]== target:
                return True
            elif matrix[row][0]<target and matrix[row][-1]>target:
                return search(row,matrix,target,0,len(matrix[row]) - 1)
        return False    
        