class Board:
    def __init__(self):
        self.grid = [[" " for _ in range(3)] for _ in range(3)]

    def draw_board(self):
        """
        Draw the board of Tic-Tac-Toe game
        """
        for row in range(len(self.grid)):
            print(" ---" * len(self.grid[row]))
            row_content = "|"
            for col in range(len(self.grid[row])):
                row_content += " " + self.grid[row][col] + " |"
            print(row_content)
        print(" ---" * len(self.grid[row]))

    def update_board(self, row: int, col: int, symbol: str) -> bool:
        """
        Update the game board based on location selected by player

        Args:
            row (int): row index of board
            col (int): column index of board
            symbol (str): symbol used by player
        """
        if self.grid[row][col] == " ":
            self.grid[row][col] = symbol
            return True
        return False

    def check_winner(self) -> str:
        """
        Check the winner of the current board

        Returns:
            str: The winning symbol ('X' or 'O') if there is a winner, else an empty string
        """
        for i in range(3):
            if self.grid[i][0] == self.grid[i][1] == self.grid[i][2] != " ": 
                return self.grid[i][0]
            elif self.grid[0][i] == self.grid[1][i] == self.grid[2][i] != " ":
                return self.grid[0][i]

        if self.grid[1][1] != " " and (self.grid[0][0] == self.grid[1][1] == self.grid[2][2] or self.grid[0][2] == self.grid[1][1] == self.grid[2][0]):
            return self.grid[1][1]

        return ""

    def is_full(self) -> bool:
        """
        Check if the current board is full or not

        Returns:
            bool: Boolean outcome indicating whether the board is full
        """
        return all(cell != " " for row in self.grid for cell in row)
