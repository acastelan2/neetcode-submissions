class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if row[-1] < target:
                continue
            elif row[-1] == target:
                return True
            else:
                low = 0
                high = len(row)-2
                while low <= high:
                    mid = low + ((high-low) // 2)
                    if row[mid] == target:
                        return True
                    elif row[mid] < target:
                        low = mid+1
                    else:
                        high = mid-1
        return False
