class Robot:
    """Represent a robot,with a name."""
population =0
def __init__(self, name):
    """Initializes the data."""
    self.name =name
    print("(initialzing{})".format(self.name))
    Robot.population +=1
def die(self):
    """I am dying."""
    print("{} is being destroyed!".format(self.name))
    Robot.population -= 1
    if Robot.population == 0:
        print("{} was the last one.".format(self.name))
    else:
        print("There are still{:d} robots working.".format(Robot.population))
def say_hi(self):
    """Greeting by the robot.
    yeah, they can do that."""
    print("Greetings, my masters call me {}.".format(self.name))
@classmethod        
def how_many(cls):
    """prints the current population."""
    print("We have {:d} robots.".format(cls.population))
droid1 = Robot("R2-D2")
droid1.say_hi()
Robot.how_many()
droid2 = Robot("C-3PO")
droid2.say_hi()
Robot.how_many()
print("\nRobots can do some work here.\n")
print("Robots have finished their work. So let's destory them.")
droid1.die()
droid2.die()
Robot.how_many()
