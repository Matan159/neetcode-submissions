class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        t, b = 0, len(matrix)-1
        l, r = 0, len(matrix[0])-1

        while t<=b:
            c = t+((b-t)//2)
            num1, num2 = matrix[c][0], matrix[c][-1]
            if num1 <= target <= num2:
                break
            elif num1 > target:
                b = c-1
            else:
                t = c+1
            

        while l<=r:
            m = l+((r-l)//2)
            num = matrix[c][m]
            if num == target:
                return True
            elif num < target:
                l = m+1
            else:
                r = m-1
            
        return False