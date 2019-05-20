from typing import List

def buildEmptyGrid(s: str, p: str):
    """
    Build empty grid for DP solution. Rows represent
    characters in the string and columns represent
    characters in the pattern. 
    """
    grid = list()
    for _ in range(len(p)):
        grid.append([None] * len(s))
    return grid

def fillFirstRowCol(grid: List[List[int]], s: str, p: str):
    # Top left corner
    i = 0
    j = 0
    if p[i] == '*':
        grid[i][j] = 1
    elif p[i] == '?':
        grid[i][j] = 1
    elif p[i] == s[i]:
        grid[i][j] = 1
    else:
        grid[i][j] = 0

    # Top row
    Ls = len(s)
    for j in range(1, Ls):
        if p[i] == '*':
            grid[i][j] = 1
        else:
            grid[i][j] = 0

    # Leftmost column
    Lp = len(p)
    j = 0
    for i in range(1, Lp):
        if not grid[i-1][j]:
            grid[i][j] = 0
        else:
            if p[i-1] == '*' and (p[i] == s[j] or p[i] == '?'):
                grid[i][j] = 1
            elif p[i] == '*':
                grid[i][j] = 1
            else:
                grid[i][j] = 0
    return grid

def printGrid(grid: List[List[int]]):
    for line in grid:
        print(line)


def checkDiag(grid, i, j, s, p):
    """
    Check if diagonal move works.
    """
    if not grid[i-1][j-1]:
        return 0
    if p[i] in set([s[j], '?', '*']):
        return 1
    else: 
        return 0

def checkDown(grid, i, j, s, p):
    """
    Check if down move works.
    """
    if not grid[i-1][j]:
        return 0
    if p[i] == '*':
        return 1
    if p[i-1] != '*':
        return 0
    if p[i] in set([s[j], '?', '*']):
        if p[i] != '*' and p[:i+1].replace('*','') != s[:j+1].replace('*',''):
            return 0
        return 1
    else:
        return 0

def checkRight(grid, i, j, s, p):
    """
    Check if right move works.
    """
    if not grid[i][j-1]:
        return 0
    if p[i] != '*':
        return 0
    if p[i] in set([s[j], '?', '*']):
        return 1
    else:
        return 0

def isReachable(grid, i, j, s, p):

    if not (grid[i-1][j-1] or grid[i-1][j] or grid[i][j-1]):
        return 0
    if p[i] in set([s[j], '?', '*']):
        return 1
    return 0

def isReachable2(grid, i, j, s, p):
    diag = checkDiag(grid, i, j, s, p)
    down = checkDown(grid, i, j, s, p)
    right = checkRight(grid, i, j, s, p)
    return max([diag, down, right])

def fillRow(grid, row, s, p):
    
    Ls = len(s)
    for col in range(1, Ls):
        grid[row][col] = isReachable2(grid, row, col, s, p)
    return grid

def fillGrid(s: str, p: str):
    grid = buildEmptyGrid(s, p)
    grid = fillFirstRowCol(grid, s, p)
    Lp = len(p)
    for row in range(1, Lp):
        grid = fillRow(grid, row, s, p)
    return grid

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        grid = fillGrid(s, p)
        if grid[-1][-1]:
            return True
        else:
            return False

