#size of given matrix is m x n
M = 6
N = 6

# A recursive function to replace previous  
# value 'prevV' at '(x, y)' and all surrounding 
# values of (x, y) with new value 'newV'. 
def floodFillUtil(mat, x, y, prevV, newV): 
  
    # Base Cases 
    if (x < 0 or x >= M or y < 0 or y >= N): 
        return
  
    if (mat[x][y] != prevV): 
        return
  
    # Replace the color at (x, y) 
    mat[x][y] = newV 
  
    # Recur for north, east, south and west  
    floodFillUtil(mat, x + 1, y, prevV, newV) 
    floodFillUtil(mat, x - 1, y, prevV, newV) 
    floodFillUtil(mat, x, y + 1, prevV, newV) 
    floodFillUtil(mat, x, y - 1, prevV, newV) 
  
# Returns size of maximum size subsquare 
#  matrix surrounded by '2' 
def replaceSurrounded(mat): 
  
    # Step 1: Replace all '1's with '-' 
    for i in range(M): 
        for j in range(N): 
            if (mat[i][j] == '1'): 
                mat[i][j] = '-'
  
    # Call floodFill for all '-'  
    # lying on edges 
     # Left Side 
    for i in range(M): 
        if (mat[i][0] == '-'): 
            floodFillUtil(mat, i, 0, '-', '1') 
      
    # Right side 
    for i in range(M):  
        if (mat[i][N - 1] == '-'): 
            floodFillUtil(mat, i, N - 1, '-', '1') 
      
    # Top side 
    for i in range(N):  
        if (mat[0][i] == '-'): 
            floodFillUtil(mat, 0, i, '-', '1') 
      
    # Bottom side 
    for i in range(N):  
        if (mat[M - 1][i] == '-'): 
            floodFillUtil(mat, M - 1, i, '-', '1') 
  
    # Step 3: Replace all '-' with '2' 
    for i in range(M): 
        for j in range(N): 
            if (mat[i][j] == '-'): 
                mat[i][j] = '2'
  
# Driver code 
if __name__ == '__main__': 
  
    mat = [ [ '0', '1', '2', '1', '1', '0' ],  
            [ '0', '1', '2', '0', '1', '2' ],  
            [ '2', '2', '1', 'O', '2', '1' ],  
            [ '1', '0', '1', '0', '2', '0' ],  
            [ '0', '2', '1', '0', '1', '0' ],  
            [ '1', '2', '0', '2', '1', '2' ] ];  
  
    replaceSurrounded(mat) 
  
    for i in range(M): 
        print(*mat[i]) 
