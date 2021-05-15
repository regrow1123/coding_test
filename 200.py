class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid[0])
        n = len(grid)
        visited = [[0]*m for _ in range(n)]

        st = []
        label = 1
        for i in range(n):
            for j in range(m):
                if visited[i][j] or grid[i][j] == '0':
                    continue
                
                st.append([i,j])

                while st:
                    pos = st.pop()
                    if visited[pos[0]][pos[1]] or grid[pos[0]][pos[1]] == '0':
                        continue
                        
                    visited[pos[0]][pos[1]] = label
                    if pos[0]-1 >= 0:
                        st.append([pos[0]-1,pos[1]])
                    if pos[0]+1 < n:
                        st.append([pos[0]+1,pos[1]])
                    if pos[1]-1 >= 0:
                        st.append([pos[0],pos[1]-1])
                    if pos[1]+1 < m:
                        st.append([pos[0],pos[1]+1])

                label += 1
        return label-1