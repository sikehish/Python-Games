import random

class Player:
  def __init__(self, name):
    self.name=name

  def make_move():
    pass


class Human(Player):
  pass

class Computer(Player):
  pass

class RockPaperScissors:
  pass

def main():
  player1=input("Enter your name")
  game = RockPaperScissors(player1)

  game.play_game()

main()

