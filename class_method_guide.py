# This program was written with the goal of explaining how class methods work.
# The original context for the variables was based on a question about a
# game related to rolling dice.


import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


class Hand:

    @classmethod
    def roll(cls):
        return 10


clear_screen()
input('Press "Enter/Return" after each example to proceed to the next.\n\n')

clear_screen()
input('First, the program defines two variables, in two different ways.\n'
      'In the first example, we define test1 using @classmethod roll() '
      'during the declaration of the variable name. This appears as the '
      'following:\n\n'
      'test1 = Hand().roll()\n\n'
      'In the second example, we define our variable with Hand() first and '
      'then call the roll() class method on it afterwords.'
      'That looks like the following:\n\n'
      'test2 = Hand()\n'
      'test2.roll()\n')

test1 = Hand().roll()
test2 = Hand()
test2.roll()

input('Let\'s examine these variables a bit now.\n\n'
      'Press "Enter/Return" to continue.')
clear_screen()

input("""\n
test1 = Hand().roll()
test2 = Hand()
test2.roll()
""")

print('---------------------------------')
print('This is the ouput of the print() '
      'function being run on the value of test1:', test1)
print('-This is the output of type(test1):', type(test1))
input('-Notice that it\'s an int, not an instance of an object at all.\n')

print('This is the output of the print() '
      'function being run on the value of test2:', test2)
print('-This is the output of type(test2):', type(test2))
input('-It\'s an instance of a "Hand" object.\n')

print('This is the print() function being run on the already existing '
      'instance of test2, with the method call .roll() being called '
      'on it. test2.roll():', test2.roll())
print('-This is the output of type(test2.roll()):', type(test2.roll()))
input('-It\'s an int.\n')

print('Just to demonstrate one last time, this is what happens if I try '
      'printing the value of test2 again, without calling the roll() '
      'method on it.\n', test2)
input('It\'s still an instance of Hand. It\'s not an int. This is because '
      'when we set "test2 = Hand()" at the beginning, we insantiated it.\n')
print('---------------------------------')

input('On the other hand (no pun intended), calling "test1 = Hand().roll() '
      'never actually instantiated anything at all.\nThe @classmethod of '
      'Hand().roll() only does one thing: it returns an integer of 10.\n')

input('There are ways to create an instance with an @classmethod, but '
      'simply setting a variable as equal to the output of a class method '
      'does not do this automatically.\nIt simply sets the variable as equal '
      'to the output of whatever the class method returned.\n')

input('The other variable, which is an instance of the class "Hand", has '
      'the ability to call the class method, roll() '
      'It is still an instance of the "Hand" class.\n')

input('This is because the roll method is not specifying what to do with the '
      'value, it is only programmed to pass a number back.\n'
      'The result of this is that while calling test2.roll() returns a value '
      'of 10, that value isn\'t stored anywhere and doesn\'t modify '
      'the instance at all.\n')

input('Thank you for using my little @classmethod tutorial.\n'
      'I hope class methods make more sense now!')

input('\n\nPress "Enter/Return" to quit.')
clear_screen()
