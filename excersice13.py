__author__ = 'antonjoj'

from random import randint

class GameGuess(object):

    def __init__(self):
        self.number = randint(1,1000)
        self.max_chances = 10

    def guess(self, guess):
        if(guess > self.number):
            print "Guessed value is greater"
        elif(guess < self.number):
            print "Guessed value is lesser"
        else:
            print "Congrats you got the correct number : {}".format(self.number)
            exit(0)

    def play(self):
        tries_left = self.max_chances
        while(tries_left > 0):
            guess = int(raw_input("Enter a guess ( tries left = {} ): ".format(tries_left)))
            self.guess(guess)
            tries_left -= 1
        else:
            print "Sorry all tries exhausted"
            print "Number was : {}".format(self.number)

if __name__ == '__main__':
    game_guess = GameGuess()
    game_guess.play()