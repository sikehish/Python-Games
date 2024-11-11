import random

consumed_tiles=set()

class Player:
    def __init__(self, symbol):
        self.symbol = symbol

    def make_move(self, board):
        raise NotImplementedError("Subclasses must implement this method.")


class Human(Player):
    def __init__(self, symbol):
        super().__init__(symbol)

    def make_move(self, board):
        while True:
            try:
                move = int(input(f"Enter your move (1-9) for {self.symbol}: "))
                if board.is_valid_move(move):
                    return move
                else:
                    print("Invalid move. The cell is already occupied.")
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 9.")


class Comp(Player):
    def __init__(self, symbol):
        super().__init__(symbol)

    def make_move(self, board):
        available_moves = board.get_available_moves()
        move = random.choice(available_moves)
        print(f"Computer chooses {move} for {self.symbol}")
        return move


class TicTacToe:
    def __init__(self):
        self.board = [i+1 for i in range(9)] 
        self.current_player = None
        self.is_game_over = False

    def display_board(self):
        board = "\n"
        for i in range(0, 9, 3):
            board += f"{self.board[i]} | {self.board[i + 1]} | {self.board[i + 2]}\n"
            if i < 6:
                board += "--+---+--\n"
        print(board)

    def is_valid_move(self, move):
        return 1 <= move <= 9 and self.board[move - 1] not in ['X', 'O']

    def get_available_moves(self):
        return [i+1 for i in range(9) if i+1 not in consumed_tiles]

    def make_move(self, move, symbol):
        consumed_tiles.add(move)
        self.board[move - 1] = symbol

    def check_winner(self):
        win_conditions = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8), 
            (0, 4, 8), (2, 4, 6)           
        ]
        for condition in win_conditions:
            if self.board[condition[0]] == self.board[condition[1]] == self.board[condition[2]] != " ":
                return self.board[condition[0]]
        return None  

    def check_draw(self):
        return len(consumed_tiles)==9

    def play_game(self, player1, player2):
        self.current_player = player1
        while not self.is_game_over:
            self.display_board()
            move = self.current_player.make_move(self)
            self.make_move(move, self.current_player.symbol)

            winner = self.check_winner()
            if winner:
                self.display_board()
                print(f"Player {winner} wins!")
                self.is_game_over = True
                break

            if self.check_draw():
                self.display_board()
                print("It's a draw!")
                self.is_game_over = True
                break

            self.current_player = player1 if self.current_player == player2 else player2


def main():
    print("Welcome to Tic-Tac-Toe!")
    player_symbol = input("Choose your symbol (X or O): ").upper()

    while player_symbol not in ["X", "O"]:
        player_symbol = input("Invalid symbol. Please choose X or O: ").upper()

    if player_symbol == "X":
        human = Human("X")
        computer = Comp("O")
    else:
        human = Human("O")
        computer = Comp("X")

    game = TicTacToe()
    game.play_game(human, computer)

if __name__ == "__main__":
    main()
