#define the base class Player
class Player:
  def play(self):
    print("The player is playing cricket.")


#define the derived class Batsman
class Batsman(Player):
  def play(self):
    print("The Batsman is batting.")


#define the derived class Bowler
class Bowler(Player):
  def play(self):
    print("The Bowler is bowling.")


#Create objects of Batsman and Bowler classes
batsman = Batsman()
bowler = Bowler()

#call the play() method for each object
batsman.play()
bowler.play()
