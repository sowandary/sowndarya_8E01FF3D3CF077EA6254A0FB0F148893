# Base class Player
class Player:
    def play(self):
        print("The player is playing cricket")

# Derived class Batsman
class Batsman(Player):
    def play(self):
        print("The batsman is batting")

# Derived class Bowler
class Bowler(Player):
    def play(self):
        print("The bowler is bowling")

# Program to test the Player, Batsman, and Bowler classes
if __name__ == "__main__":
    player = Player()
    batsman = Batsman()
    bowler = Bowler()

    print("Player:")
    player.play()

    print("\nBatsman:")
    batsman.play()

    print("\nBowler:")
    bowler.play()
