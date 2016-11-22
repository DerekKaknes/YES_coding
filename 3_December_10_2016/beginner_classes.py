import random as r
"""
In this file, you are going to create a couple classes, assign attributes and 
methods to those classes, and then create objects as instances of those classes.
"""

# Create a BasketballPlayer class

class BasketballPlayer:
    # Create an __init__ method with attributes name, height and vertical_leap
    def __init__(self, name, height, vertical_leap, shooting_pct):
        # Assign the value of each attribute to the input provided
        self.name = name # name of the player
        self.height = height # the player's height (in inches)
        self.vertical_leap = vertical_leap # the player's vertical leap (in inches)
        self.shooting_pct = shooting_pct # the players shooting percentage (between 0.00 and 1.00)

    # define a method called shoot that determines whether the player's shot goes in based upon their shooting percentage
    def shoot(self):
        if r.random() <= self.shooting_pct: # r.random() will generate a random number between 0 and 1, if the number is less than the shooting_pct, the shot goes in
            print "Swish! {}'s shot goes in.".format(self.name)
            return True
        else:
            print "Clang! {}'s shot misses.".format(self.name)
            return False

    # Define a method called block that determines whether a player successfully blocks another players shot
    def block(self, shooter):
        my_peak_jump = self.height + self.vertical_leap
        shooter_peak_jump = shooter.height + shooter.vertical_leap
        if my_peak_jump >= shooter_peak_jump:
            print "Rejected! {} blocks {}'s shot.".format(self.name, shooter.name)
            return True
        else:
            print "Whiff! {} get's the shot off cleanly".format(shooter.name)
            return False

if __name__ == '__main__':
    mj = BasketballPlayer("Michael Jordan", 78, 42, .6)
    shaq = BasketballPlayer("Shaquille O'Neil", 98, 30, .4)
    mj.shoot()
    shaq.shoot()
    shaq.block(mj)



