
def noOfLs(small, large):
    if small < 2 or large < 4:
        return 0
    return min(small, large//2) - 1

T = int(raw_input())
t = 1
while t <= T:
    res = 0
    rows, cols = list(map(int, raw_input().split()))
    grid = []
    for i in range(rows):
        grid.append(list(map(int, raw_input().split())))
    
    dp = []
    for r in range(rows):
        dp_row = []
        for c in range(cols):
            dp_row.append([[0, 0], [0, 0]])
        dp.append(dp_row)
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                if r-1 >= 0 and grid[r-1][c] != 0:
                    dp[r][c][0][0] = dp[r-1][c][0][0] + 1
                if c-1 >=0 and grid[r][c-1] != 0:
                    dp[r][c][0][1] = dp[r][c-1][0][1] + 1
    
    for r in range(rows-1, -1, -1):
        for c in range(cols-1, -1, -1):
            if r+1 < rows and grid[r+1][c] != 0:
                dp[r][c][1][0] = dp[r+1][c][1][0] + 1
            if c+1 < cols and grid[r][c+1] != 0:
                dp[r][c][1][1] = dp[r][c+1][1][1] + 1
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                # top is small
                res += noOfLs(dp[r][c][0][0]+1, dp[r][c][0][1]+1)
                res += noOfLs(dp[r][c][0][0]+1, dp[r][c][1][1]+1)
                # down is small
                res += noOfLs(dp[r][c][1][0]+1, dp[r][c][0][1]+1)
                res += noOfLs(dp[r][c][1][0]+1, dp[r][c][1][1]+1)
                # left is small
                res += noOfLs(dp[r][c][0][1]+1, dp[r][c][0][0]+1)
                res += noOfLs(dp[r][c][0][1]+1, dp[r][c][1][0]+1)
                # right is small
                res += noOfLs(dp[r][c][1][1]+1, dp[r][c][0][0]+1)
                res += noOfLs(dp[r][c][1][1]+1, dp[r][c][1][0]+1)
            
                
    
    
    print("Case #{}: {}".format(t, res))
    t += 1