import random
import getpass
import google.generativeai as genai
# Used to securely store your API key
from google.colab import userdata

GOOGLE_API_KEY=userdata.get('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')

class Player:
    def __init__(self, name):
        self.name=name
    
    def make_move(self):
        pass


choice_map={1: 'Rock ✊', 2: 'Paper ✋', 3: 'Scissors ✌️'}
            
class Human(Player):
    def __init__(self, name):
        super().__init__(name)
        
    def make_move(self):
        print(f"\n{self.name}, it's your turn!")
        print("Chose your move")
        for key, val in choice_map.items():
            print(f"{key}. {val}")
        move=getpass.getpass(prompt="Enter your chooooooice: ")
        
        while move not in ["1","2", "3"]:
            print("Error! Chose a valid option!")
            move=maskpass.askpass(prompt="Enter your chooooooice: ", mask="#")
            # move=input("Enter your choice: ")
        
        return int(move)

class Computer(Player):
    def __init__(self, name="Computer"):
        super().__init__(name)
        
    def make_move(self):
        print("It's Computer's turn")
        print("Computer's thinking....")
        return random.choice([1,2,3]) #random.randint(1,3)
 
class RPS:
    def __init__(self, player1, player2="Computer"):
        self.player1=Human(player1)
        self.player2=Human(player2)
    
    def play_game(self):
        print("\nLet's play RPS!\n")
        while True:
            move1=self.player1.make_move()
            move2=self.player2.make_move()
            
            print(f"\n{self.player1.name} chose {choice_map[move1]}.")
            print(f"{self.player2.name} chose {choice_map[move2]}.\n")
            
            print(self.check_winner(move1, move2))

            response = model.generate_content("GIve some interesting info about rock paper scissors, or some motivation to win the game(1 line please)")
            print("Thought: ", response.text)
            
            play_again=input("\nDo you want to play again? [Y/n]").lower() or "y"
            print()
            if(play_again=="n"):
                print("The End!")
                break
        
    
    def check_winner(self, move1, move2):
        if move1==move2:
            return "It's a tie"
        elif (move1==1 and move2==3) or (move1==2 and move2==1) or (move1==3 and move2==2):
            return f"{self.player1.name} wins!"
        else:
            return f"{self.player2.name} wins!"
        
def main():
    player1=input("Enter player 1 name: ")
    player2=input("Enter player 2 name: ")
    rps=RPS(player1, player2)
    rps.play_game()
    

if __name__=="__main__":
    main()
        

    