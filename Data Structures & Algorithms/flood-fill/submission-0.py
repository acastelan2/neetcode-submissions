class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def dfs(r, c):
            print(f"r:{r}, c:{c}")
            if min(r,c) < 0 or r == len(image) or c == len(image[0]):
                return
            if image[r][c] == color or image[r][c] != old_color:
                return
            
            image[r][c] = color

            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

            return

        old_color = image[sr][sc]
        dfs(sr, sc)
        return image

            