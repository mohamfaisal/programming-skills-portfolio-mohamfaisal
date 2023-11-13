#Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value.
#As they enter each topping, print a message saying you’ll add that topping to their pizza.

while True:
    toppings=input('Enter the topping:(or type quit to finish:)' )
    if toppings=='quit':
        print('You have customized your pizza toppings')
        break
    else:
        print(f'we will add',(toppings),'to your pizza')