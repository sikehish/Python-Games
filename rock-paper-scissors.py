import random

class Player:
    def __init__(self, name):
        self.name = name

    def make_move(self):
        pass

class Hooman(Player):
    def __init__(self, name):
        super().__init__(name)

    def make_move(self):
        print(f"\n{self.name}, it's your turn! 🕹️")
        print("Choose your move:")
        print("1. Rock ✊")
        print("2. Paper ✋")
        print("3. Scissors ✌️")
        move = input("Enter your choice (1, 2, or 3): ")

        while move not in ['1', '2', '3']:
            print("Invalid input! Please choose 1, 2, or 3.")
            move = input("Enter your choice (1, 2, or 3): ")

        return int(move)

class Comp(Player):
    def __init__(self, name):
        super().__init__(name)

    def make_move(self):
        print("\nComputer is thinking... 🤖")
        move = random.choice([1, 2, 3])
        return move

class RockPaperScissors:
    def __init__(self, human_name, computer_name="Computer"):
        self.human_player = Hooman(human_name)
        self.computer_player = Comp(computer_name)
        self.move_mapping = {1: 'Rock ✊', 2: 'Paper ✋', 3: 'Scissors ✌️'}

    def play_game(self):
        print("\nWelcome to Rock, Paper, Scissors! ✊✋✌️")
        while True:
            human_move = self.human_player.make_move()
            computer_move = self.computer_player.make_move()

            print(f"{self.human_player.name} chose {self.move_mapping[human_move]}")
            print(f"{self.computer_player.name} chose {self.move_mapping[computer_move]}")

            winner = self.determine_winner(human_move, computer_move)

            if winner == "tie":
                print("\nIt's a tie! 🤝")
            else:
                print(f"\n{winner} wins! 🎉")

            play_again = input("\nDo you want to play again? (y/n): ").lower() or 'y'
            if play_again != 'y':
                print("Thanks for playing! 👋")
                break

    def determine_winner(self, human_move, computer_move):
        if human_move == computer_move:
            return "tie"
        #dif winning combinations
        elif (human_move == 1 and computer_move == 3) or \
             (human_move == 2 and computer_move == 1) or \
             (human_move == 3 and computer_move == 2):
            return self.human_player.name
        else:
            return self.computer_player.name

def main():
    human_name = input("Enter your name: ")
    game = RockPaperScissors(human_name)

    game.play_game()

if __name__ == "__main__":
    main()
