class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        t, b = 0, len(matrix) - 1
        l, r = 0, len(matrix[0]) - 1
        
        while t<=b:
            c = t + ((b-t)//2)
            if matrix[c][0] > target:
                b = c - 1
            elif matrix[c][-1] < target:
                t = c + 1
            else:
                break

        while l<=r:       
            m = l + ((r - l) // 2)

            if matrix[c][m] > target:
                r = m - 1
            elif matrix[c][m] < target:
                l = m + 1
            else:
                return True
        return False