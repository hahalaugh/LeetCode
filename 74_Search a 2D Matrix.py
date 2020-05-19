class Solution(object):
    def searchMatrix(self, matrix, target):
        #合并为一个排序的数组处理，二分查找
        if not matrix or not matrix[0]: return False
        
        i = 0
        j = len(matrix[0]) * len(matrix) - 1
        while i <= j :
            m = i + (j-i)/2
            x = m / len(matrix[0])
            y = m - x * len(matrix[0])
            if matrix[x][y] == target: return True
            elif matrix[x][y] > target:
                j = m - 1
            else:
                i = m + 1
    
        return False
    
    def searchMatrixBinaryStep(self, matrix, target):
        #x轴上递进到需要的行，二分查找列
        if not matrix or not matrix[0]:
            return False
        i = 0
        while i < len(matrix)-1 and matrix[i+1][0] <= target:
            i += 1
        
        l, r = 0, len(matrix[0])-1
    
        while l <= r:
            m = l + (r-l) / 2
            if matrix[i][m] == target: return True
            elif matrix[i][m] > target:
                r = m - 1
            else:
                l = m + 1
        
        return False
    
    def searchMatrixUpperRight(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        #从右上角开始，小于目标则删去整行，大于目标则删去整列，否则找到返回True
        if not matrix or not matrix[0]:
            return False
        
        i, j = 0, len(matrix[0])-1
        while i < len(matrix) and j >= 0:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                i += 1
            else:
                j -= 1
        
        return False