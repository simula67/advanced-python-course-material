__author__ = 'ravi'
from random import  randint


class GuessMe(object):
    max_chance = 10

    def __init__(self):
        self.rand_value = randint(1, 1000)
        self.play()

    def play(self):
        current_chance = 1
        while current_chance <= GuessMe.max_chance:
            caption = "Chance: {}\nEnter the predict: ".\
                format(current_chance)
            user_input = int(raw_input(caption))

            if user_input == self.rand_value:
                print "you won :)"
                break
            elif user_input < self.rand_value:
                print "{}: entered value is lesser".format(user_input)
            elif user_input > self.rand_value:
                print "{}: entered value is greater".format(user_input)

            current_chance += 1
        else:
            print "you lost :( "
            exit(1)

if __name__ == '__main__':
    GuessMe()