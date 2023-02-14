from random import randint


class Die:

    def __init__(self, sides):
        self.sides = sides

    def roll_die(self):
        print(randint(1, self.sides))


cube = Die(6)
cube.roll_die()
cube.roll_die()
cube.roll_die()
cube.roll_die()
cube.roll_die()
cube.roll_die()
cube.roll_die()
cube.roll_die()
cube.roll_die()
cube.roll_die()
cube.roll_die()
print('\n\n')

cube = Die(10)
cube.roll_die()
cube.roll_die()
cube.roll_die()
cube.roll_die()
cube.roll_die()
cube.roll_die()
cube.roll_die()
cube.roll_die()
cube.roll_die()
cube.roll_die()
cube.roll_die()
print('\n\n')

cube = Die(20)
cube.roll_die()
cube.roll_die()
cube.roll_die()
cube.roll_die()
cube.roll_die()
cube.roll_die()
cube.roll_die()
cube.roll_die()
cube.roll_die()
cube.roll_die()
cube.roll_die()
print('\n\n')
