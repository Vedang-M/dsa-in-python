class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            if matrix[i][0]<=target and matrix[i][-1]>=target:
                if matrix[i][0]==target or matrix[i][-1]==target:
                    return True
                
                else:
                    for j in range(len(matrix[i])):
                        if matrix[i][j]==target:
                            return True
                    
                    return False
        
        return False