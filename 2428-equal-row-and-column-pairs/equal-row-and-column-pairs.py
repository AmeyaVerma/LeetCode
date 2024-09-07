class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        hashtable={}
        count=0
        for row in grid:
            row_tuple=tuple(row)
            hashtable[row_tuple]=hashtable.get(row_tuple,0)+1
        for col in zip(*grid):
            col_tuple=tuple(col)
            count+=hashtable.get(col_tuple,0)
        return count