class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        

        
        top, bottom = 0, len(matrix) - 1
        
        while top <= bottom:
            midrow = (top+bottom) // 2
        
            if target < matrix[midrow][0]:
                bottom = midrow - 1
            elif target > matrix[midrow][-1]: #last element in the row
                top = midrow + 1
            else:
                break
            

        if not (top <= bottom):
            return False
        row = (top + bottom) // 2

        l, r = 0, len(matrix[0]) - 1
        while l <= r:
            mid = (r+l) // 2
            
            if matrix[row][mid] < target:
                l = mid + 1
            elif matrix[row][mid] > target:
                r = mid - 1
            else:
                return True
            
        return False