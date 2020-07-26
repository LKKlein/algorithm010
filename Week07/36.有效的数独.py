
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        table = {}
        n = 9
        for i in range(n):
            for j in range(n):
                if board[i][j] != ".":
                    if board[i][j] not in table:
                        table[board[i][j]] = {
                            "row": set(),
                            "col": set(),
                            "block": set(),
                        }
                    if i in table[board[i][j]]["row"]:
                        return False
                    if j in table[board[i][j]]["col"]:
                        return False
                    block = (i // 3) * 3 + j // 3
                    if block in table[board[i][j]]["block"]:
                        return False
                    table[board[i][j]]["row"].add(i)
                    table[board[i][j]]["col"].add(j)
                    table[board[i][j]]["block"].add(block)
        return True
