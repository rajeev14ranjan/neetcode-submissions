# Valid Sudoku
# You are given a 9 x 9 Sudoku board board, Return true if the Sudoku board is valid, otherwise return false
# Note: A board does not need to be full or be solvable to be valid. Empty cells have "."

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        check_row = [set() for _ in range(9)]
        check_col = [set() for _ in range(9)]
        check_box = [set() for _ in range(9)]

        for r in range(len(board)):
            for c in range(len(board[r])):
                
                s = board[r][c]
                if s == ".": continue

                # validate rows
                if s in check_row[r]:
                    return False
                else: 
                    check_row[r].add(s)
                
                # validate cols
                if s in check_col[c]:
                    return False
                else: 
                    check_col[c].add(s)

                # check box
                box = c//3 + 3*(r//3)
                if s in check_box[box]:
                    return False
                else: 
                    check_box[box].add(s)
        
        return True


