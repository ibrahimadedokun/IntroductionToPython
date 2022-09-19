import random as R

if True:
    print('This is true.')

firstInteger = int(5)
firstString = str(5)

print(type(firstInteger))
print(type(firstString))

colors = ["red", "green", "blue"]
r, g, b = colors
print(r + g + b)

def colorNamesPrinter(p):
    print(p)
    print(colors)
    print(type(p))
    print("The parameter when cast to string is: " + str(p))
    print("Now I am about to change the colors")
    #global colors
    #colors = ["cyan","yellow","magenta","k-whatever"]
    print(p)
    print(colors)
    print("Length of colors list is " + str(len(colors)))

colorNamesPrinter(colors)

print("Random number is " + str(R.randrange(1, 10)))

# When unassigned, it's a comment
'''We are the world,
we are the children
we are the ones'''

print('''We are the world,
    we are the children
        we are the ones''')