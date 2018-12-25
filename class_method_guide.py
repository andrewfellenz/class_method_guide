# This program was written with the goal of explaining how class methods work.
# The original context for the variables was based on a question about a
# game related to rolling dice.


class Hand:

    @classmethod
    def roll(cls):
        return 10


input('Press "Enter" after each example to proceed to the next.\n\n')

input('First, the program defines two variables, in two different ways.\n'
      'In the first example, we define test1 using the @classmethod roll() '
      'during the declaration of the variable name.This appears as the '
      'following:\n\n'
      'test1 = Hand().roll()\n\n'
      'In the second example, we define our variable with Hand() first and '
      'then call the roll() calss method on it afterwords.'
      'That looks like the following:\n\n'
      'test2 = Hand()\n'
      'test2.roll()\n\n')

test1 = Hand().roll()
test2 = Hand()
test2.roll()

input('Let\'s examine these variables a bit now.\n')

print('This is the ouput of the print() '
      'function being run on the value of test1:', test1)
input()

print('This is the output of type(test1):', type(test1))
input('Notice that it\'s an int, not an instance of an object at all.\n')

print('This is the output of the print() '
      'function being run on the value of test2:', test2)
input()

print('This is the output of type(test2):', type(test2))
input('It\'s an instance of a "Hand" object.\n')

print('This is the print() function being run on the already existing '
      'instance of test2, with the method call .roll() being called '
      'on it. test2.roll():', test2.roll())
input('This @classmethod when run on an instance of hand produces an int.\n')

print('This is the output of type(test2.roll()):', type(test2.roll()))
input('It\'s an int.\n\n')

print('Just to demonstrate one last time, this is what happens if I try '
      'printing the value of test2 again, without calling the roll() '
      'method on it.\n', test2)
input('It\'s still an instance of Hand. It\'s not an int. This is because '
      'when we set "test2 = Hand()" at the beginning, we insantiated it.\n')

input('On the other hand (no pun intended), calling "test1 = Hand().roll() '
      'never actually instantiated anything at all.\nThe @classmethod of '
      'Hand().roll() only does one thing: it returns an integer of 10.\n')

input('There are ways to create an instance with an @classmethod, but '
      'simply setting a variable as equal to the output of a class method '
      'does not do this automatically.\nIt simply sets the variable as equal '
      'to the output of the class method.')

input('The other variable, which we have identified as actually being a real '
      'instance of the class "Hand", has the ability to call the class method '
      'roll(), because it is an instance of the "Hand" class, but doesn\'t do '
      'anything with that value of 10 returned to it.\n'
      'This is because the class method is not specifying what to do with the '
      'value, it is only programmed to pass a number back.\n'
      'The result of this is that while calling test2.roll() returns a value '
      'of 10, that value isn\'t stored anywhere and doesn\'t modify '
      'the instance at all.')

input('Thank you for watching my little @classmethod tutoria.\n'
      'I hope class methods make more sense now!')
