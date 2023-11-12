#Turn your if-else chain from Exercise 5-4 into an if-elifelse chain.
#•	 If the alien is green, print a message that the player earned 5 points.
#•	 If the alien is yellow, print a message that the player earned 10 points.
#•	 If the alien is red, print a message that the player earned 15 points.
#•	 Write three versions of this program, making sure each message is printed for the appropriate color alien.

def print_alien_color_message(alien_color):
    if alien_color == 'green':
        print('You just earned 5 points for shooting the alien!')
    elif alien_color == 'yellow':
        print('You just earned 10 points for shooting the alien!')
    elif alien_color == 'red':
        print('You just earned 15 points for shooting the alien!')
    else:
        print('Invalid alien color.')

print_alien_color_message('green')

def print_alien_color_message(alien_color):
    if alien_color == 'yellow':
        print('You just earned 10 points for shooting the alien!')
    elif alien_color == 'red':
        print('You just earned 15 points for shooting the alien!')
    elif alien_color == 'green':
        print('You just earned 5 points for shooting the alien!')
    else:
        print('Invalid alien color.')

print_alien_color_message('yellow')

def print_alien_color_message(alien_color):
    if alien_color == 'red':
        print('You just earned 15 points for shooting the alien!')
    elif alien_color == 'green':
        print('You just earned 5 points for shooting the alien!')
    elif alien_color == 'yellow':
        print('You just earned 10 points for shooting the alien!')
    else:
        print('Invalid alien color.')

print_alien_color_message('red')