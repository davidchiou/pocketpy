# Piece(0) = (0, 0, 0) -> (x, y, z)
# Piece(1) = (1, 0, 0)
# Piece(2) = (0, 1, 0)
# Piece(3) = (1, 1, 0)
# Piece(4) = (0, 0, 1)
# Piece(5) = (1, 0 ,1)
# Piece(6) = (0, 1, 1)
# Piece(7) = (1, 1, 1)

class Piece(object):
    def __init__(self, num, color = None):
        self.num = num
        self.front = color[0]
        self.right = color[1]
        self.back = color[2]
        self.left = color[3]
        self.up = color[4]
        self.down = color[5]
class Cube(object):
    def __init__(self, current_cube):
        self.piece_0 = current_cube[0]
        self.piece_1 = current_cube[1]
        self.piece_2 = current_cube[2]
        self.piece_3 = current_cube[3]
        self.piece_4 = current_cube[4]
        self.piece_5 = current_cube[5]
        self.piece_6 = current_cube[6]
        self.piece_7 = current_cube[7]
    def get_status(self):
        return ' ' * 2 + self.piece_4.back + self.piece_6.back + '\n' + ' ' * 2 + self.piece_0.back + self.piece_2.back + '\n' + self.piece_4.left + self.piece_0.left + self.piece_0.down + self.piece_2.down + self.piece_2.right + self.piece_6.right + self.piece_6.up + self.piece_4.up + '\n' + self.piece_5.left + self.piece_1.left + self.piece_1.down + self.piece_3.down + self.piece_3.right + self.piece_7.right + self.piece_7.up + self.piece_5.up + '\n' + ' ' * 2 + self.piece_1.front + self.piece_3.front + '\n' + ' ' * 2 + self.piece_5.front + self.piece_7.front 

piece_0 = Piece(0, ['', '', 'B', 'W', '', 'O'])#Piece(0, ['', '', 'B', 'O', '', 'Y'])
piece_1 = Piece(1, ['R', '', '', 'G', '', 'Y'])#Piece(1, ['G', '', '', 'O', '', 'Y'])
piece_2 = Piece(2, ['', 'Y', 'R', '', '', 'B'])#Piece(2, ['', 'R', 'B', '', '', 'Y'])
piece_3 = Piece(3, ['W', 'R', '', '', '', 'G'])#Piece(3, ['G', 'R', '', '', '', 'Y'])
piece_4 = Piece(4, ['', '', 'W', 'R', 'B', ''])#Piece(4, ['', '', 'B', 'O', 'W', ''])
piece_5 = Piece(5, ['Y', '', '', 'O', 'G', ''])#Piece(5, ['G', '', '', 'O', 'W', ''])
piece_6 = Piece(6, ['', 'W', 'O', '', 'G', ''])#Piece(6, ['', 'R', 'B', '', 'W', ''])
piece_7 = Piece(7, ['O', 'B', '', '', 'Y', ''])#Piece(7, ['G', 'R', '', '', 'W', ''])

cube_test = Cube([piece_0, piece_1, piece_2, piece_3, piece_4, piece_5, piece_6, piece_7])
print cube_test.get_status()


def r_turn(cube):
    #print 'turn the right face'
    piece_0 = Piece(0, ['', '', '', '', '', ''])
    piece_1 = Piece(1, ['', '', '', '', '', ''])
    piece_2 = Piece(2, ['', '', '', '', '', ''])
    piece_3 = Piece(3, ['', '', '', '', '', ''])
    piece_4 = Piece(4, ['', '', '', '', '', ''])
    piece_5 = Piece(5, ['', '', '', '', '', ''])
    piece_6 = Piece(6, ['', '', '', '', '', ''])
    piece_7 = Piece(7, ['', '', '', '', '', ''])


    turned_cube = Cube([piece_0, piece_1, piece_2, piece_3, piece_4, piece_5, piece_6, piece_7])
    # right turn will influence piece_2, piece_3, piece_6, piece_7

    # piece_2 case:
    turned_cube.piece_2.front = ''
    turned_cube.piece_2.up = ''
    turned_cube.piece_2.left = ''
    turned_cube.piece_2.right = cube.piece_6.right
    turned_cube.piece_2.down = cube.piece_6.back
    turned_cube.piece_2.back = cube.piece_6.up
    
    # piece_3 case:
    turned_cube.piece_3.up = ''
    turned_cube.piece_3.left = ''
    turned_cube.piece_3.back = ''
    turned_cube.piece_3.right = cube.piece_2.right
    turned_cube.piece_3.down = cube.piece_2.back
    turned_cube.piece_3.front = cube.piece_2.down

    # piece_6 case:
    turned_cube.piece_6.front = ''
    turned_cube.piece_6.left = ''
    turned_cube.piece_6.down = ''
    turned_cube.piece_6.right = cube.piece_7.right
    turned_cube.piece_6.back = cube.piece_7.up
    turned_cube.piece_6.up = cube.piece_7.front

    # piece_7 case:
    turned_cube.piece_7.left = ''
    turned_cube.piece_7.back = ''
    turned_cube.piece_7.down = ''
    turned_cube.piece_7.right = cube.piece_3.right
    turned_cube.piece_7.front = cube.piece_3.down
    turned_cube.piece_7.up = cube.piece_3.front
    
    # others:
    turned_cube.piece_0 = cube.piece_0
    turned_cube.piece_1 = cube.piece_1
    turned_cube.piece_4 = cube.piece_4
    turned_cube.piece_5 = cube.piece_5
    return turned_cube

def l_turn(cube):
    #print 'turn the left face'
    piece_0 = Piece(0, ['', '', '', '', '', ''])
    piece_1 = Piece(1, ['', '', '', '', '', ''])
    piece_2 = Piece(2, ['', '', '', '', '', ''])
    piece_3 = Piece(3, ['', '', '', '', '', ''])
    piece_4 = Piece(4, ['', '', '', '', '', ''])
    piece_5 = Piece(5, ['', '', '', '', '', ''])
    piece_6 = Piece(6, ['', '', '', '', '', ''])
    piece_7 = Piece(7, ['', '', '', '', '', ''])


    turned_cube = Cube([piece_0, piece_1, piece_2, piece_3, piece_4, piece_5, piece_6, piece_7])
    # left turn will influence piece_0, piece_1, piece_4, piece_5

    # piece_0 case:
    turned_cube.piece_0.up = ''
    turned_cube.piece_0.front = ''
    turned_cube.piece_0.right = ''
    turned_cube.piece_0.left = cube.piece_1.left
    turned_cube.piece_0.down = cube.piece_1.front
    turned_cube.piece_0.back = cube.piece_1.down

    # piece_1 case:
    turned_cube.piece_1.up = ''
    turned_cube.piece_1.right = ''
    turned_cube.piece_1.back = ''
    turned_cube.piece_1.left = cube.piece_5.left
    turned_cube.piece_1.down = cube.piece_5.front
    turned_cube.piece_1.front = cube.piece_5.up

    # piece_4 case:
    turned_cube.piece_4.right = ''
    turned_cube.piece_4.front = ''
    turned_cube.piece_4.down = ''
    turned_cube.piece_4.left = cube.piece_0.left
    turned_cube.piece_4.back = cube.piece_0.down
    turned_cube.piece_4.up = cube.piece_0.back

    # piece_5 case:
    turned_cube.piece_5.right = ''
    turned_cube.piece_5.back = ''
    turned_cube.piece_5.down = ''
    turned_cube.piece_5.left = cube.piece_4.left
    turned_cube.piece_5.front = cube.piece_4.up
    turned_cube.piece_5.up = cube.piece_4.back

    # others:
    turned_cube.piece_2 = cube.piece_2
    turned_cube.piece_3 = cube.piece_3
    turned_cube.piece_6 = cube.piece_6
    turned_cube.piece_7 = cube.piece_7
    return turned_cube

def u_turn(cube):
    #print 'turn the up face'
    piece_0 = Piece(0, ['', '', '', '', '', ''])
    piece_1 = Piece(1, ['', '', '', '', '', ''])
    piece_2 = Piece(2, ['', '', '', '', '', ''])
    piece_3 = Piece(3, ['', '', '', '', '', ''])
    piece_4 = Piece(4, ['', '', '', '', '', ''])
    piece_5 = Piece(5, ['', '', '', '', '', ''])
    piece_6 = Piece(6, ['', '', '', '', '', ''])
    piece_7 = Piece(7, ['', '', '', '', '', ''])


    turned_cube = Cube([piece_0, piece_1, piece_2, piece_3, piece_4, piece_5, piece_6, piece_7])
    # up turn will influence piece_4, piece_5, piece_6, piece_7

    # piece_4 case:
    turned_cube.piece_4.right = ''
    turned_cube.piece_4.front = ''
    turned_cube.piece_4.down = ''
    turned_cube.piece_4.up = cube.piece_5.up
    turned_cube.piece_4.left = cube.piece_5.front
    turned_cube.piece_4.back = cube.piece_5.left

    # piece_5 case:
    turned_cube.piece_5.back = ''
    turned_cube.piece_5.right = ''
    turned_cube.piece_5.down = ''
    turned_cube.piece_5.up = cube.piece_7.up
    turned_cube.piece_5.front = cube.piece_7.right
    turned_cube.piece_5.left = cube.piece_7.front

    # piece_6 case:
    turned_cube.piece_6.left = ''
    turned_cube.piece_6.front = ''
    turned_cube.piece_6.down = ''
    turned_cube.piece_6.up = cube.piece_4.up
    turned_cube.piece_6.back = cube.piece_4.left
    turned_cube.piece_6.right = cube.piece_4.back

    # piece_7 case:
    turned_cube.piece_7.left = ''
    turned_cube.piece_7.back = ''
    turned_cube.piece_7.down = ''
    turned_cube.piece_7.up = cube.piece_6.up
    turned_cube.piece_7.right = cube.piece_6.back
    turned_cube.piece_7.front = cube.piece_6.right

    # others:
    turned_cube.piece_0 = cube.piece_0
    turned_cube.piece_1 = cube.piece_1
    turned_cube.piece_2 = cube.piece_2
    turned_cube.piece_3 = cube.piece_3
    return turned_cube

def d_turn(cube):
    #print 'turn the down face'
    piece_0 = Piece(0, ['', '', '', '', '', ''])
    piece_1 = Piece(1, ['', '', '', '', '', ''])
    piece_2 = Piece(2, ['', '', '', '', '', ''])
    piece_3 = Piece(3, ['', '', '', '', '', ''])
    piece_4 = Piece(4, ['', '', '', '', '', ''])
    piece_5 = Piece(5, ['', '', '', '', '', ''])
    piece_6 = Piece(6, ['', '', '', '', '', ''])
    piece_7 = Piece(7, ['', '', '', '', '', ''])


    turned_cube = Cube([piece_0, piece_1, piece_2, piece_3, piece_4, piece_5, piece_6, piece_7])
    # down turn will influence piece_0, piece_1, piece_2, piece_3

    # piece_0 case:
    turned_cube.piece_0.right = ''
    turned_cube.piece_0.front = ''
    turned_cube.piece_0.up = ''
    turned_cube.piece_0.down = cube.piece_2.down
    turned_cube.piece_0.back = cube.piece_2.right
    turned_cube.piece_0.left = cube.piece_2.back

    # piece_1 case:
    turned_cube.piece_1.back = ''
    turned_cube.piece_1.right = ''
    turned_cube.piece_1.up = ''
    turned_cube.piece_1.down = cube.piece_0.down
    turned_cube.piece_1.left = cube.piece_0.back
    turned_cube.piece_1.front = cube.piece_0.left

    # piece_2 case:
    turned_cube.piece_2.left = ''
    turned_cube.piece_2.up = ''
    turned_cube.piece_2.front = ''
    turned_cube.piece_2.down = cube.piece_3.down
    turned_cube.piece_2.back = cube.piece_3.right
    turned_cube.piece_2.right = cube.piece_3.front

    # piece_3 case:
    turned_cube.piece_3.up = ''
    turned_cube.piece_3.left = ''
    turned_cube.piece_3.back = ''
    turned_cube.piece_3.down = cube.piece_1.down
    turned_cube.piece_3.right = cube.piece_1.front
    turned_cube.piece_3.front = cube.piece_1.left

    # others:
    turned_cube.piece_4 = cube.piece_4
    turned_cube.piece_5 = cube.piece_5
    turned_cube.piece_6 = cube.piece_6
    turned_cube.piece_7 = cube.piece_7
    return turned_cube

def f_turn(cube):
    #print 'turn the front face'
    piece_0 = Piece(0, ['', '', '', '', '', ''])
    piece_1 = Piece(1, ['', '', '', '', '', ''])
    piece_2 = Piece(2, ['', '', '', '', '', ''])
    piece_3 = Piece(3, ['', '', '', '', '', ''])
    piece_4 = Piece(4, ['', '', '', '', '', ''])
    piece_5 = Piece(5, ['', '', '', '', '', ''])
    piece_6 = Piece(6, ['', '', '', '', '', ''])
    piece_7 = Piece(7, ['', '', '', '', '', ''])


    turned_cube = Cube([piece_0, piece_1, piece_2, piece_3, piece_4, piece_5, piece_6, piece_7])
    # front turn will influence piece_1, piece_3, piece_5, piece_7

    # piece_1 case:
    turned_cube.piece_1.right = ''
    turned_cube.piece_1.back = ''
    turned_cube.piece_1.up = ''
    turned_cube.piece_1.front = cube.piece_3.front
    turned_cube.piece_1.down = cube.piece_3.right
    turned_cube.piece_1.left = cube.piece_3.down

    # piece_3 case:
    turned_cube.piece_3.back = ''
    turned_cube.piece_3.left = ''
    turned_cube.piece_3.up = ''
    turned_cube.piece_3.front = cube.piece_7.front
    turned_cube.piece_3.right = cube.piece_7.up
    turned_cube.piece_3.down = cube.piece_7.right

    # piece_5 case:
    turned_cube.piece_5.right = ''
    turned_cube.piece_5.back = ''
    turned_cube.piece_5.down = ''
    turned_cube.piece_5.front = cube.piece_1.front
    turned_cube.piece_5.up = cube.piece_1.left
    turned_cube.piece_5.left = cube.piece_1.down

    # piece_7 case:
    turned_cube.piece_7.down = ''
    turned_cube.piece_7.left = ''
    turned_cube.piece_7.back = ''
    turned_cube.piece_7.front = cube.piece_5.front
    turned_cube.piece_7.right = cube.piece_5.up
    turned_cube.piece_7.up = cube.piece_5.left

    # others:
    turned_cube.piece_0 = cube.piece_0
    turned_cube.piece_2 = cube.piece_2
    turned_cube.piece_4 = cube.piece_4
    turned_cube.piece_6 = cube.piece_6
    return turned_cube

def b_turn(cube):
    #print 'turn the back face'
    piece_0 = Piece(0, ['', '', '', '', '', ''])
    piece_1 = Piece(1, ['', '', '', '', '', ''])
    piece_2 = Piece(2, ['', '', '', '', '', ''])
    piece_3 = Piece(3, ['', '', '', '', '', ''])
    piece_4 = Piece(4, ['', '', '', '', '', ''])
    piece_5 = Piece(5, ['', '', '', '', '', ''])
    piece_6 = Piece(6, ['', '', '', '', '', ''])
    piece_7 = Piece(7, ['', '', '', '', '', ''])


    turned_cube = Cube([piece_0, piece_1, piece_2, piece_3, piece_4, piece_5, piece_6, piece_7])
    # back turn will influence piece_0, piece_2, piece_4, piece_6

    # piece_0 case:
    turned_cube.piece_0.right = ''
    turned_cube.piece_0.front = ''
    turned_cube.piece_0.up = ''
    turned_cube.piece_0.back = cube.piece_4.back
    turned_cube.piece_0.left = cube.piece_4.up
    turned_cube.piece_0.down = cube.piece_4.left

    # piece_2 case:
    turned_cube.piece_2.left = ''
    turned_cube.piece_2.up = ''
    turned_cube.piece_2.front = ''
    turned_cube.piece_2.back = cube.piece_0.back
    turned_cube.piece_2.down = cube.piece_0.left
    turned_cube.piece_2.right = cube.piece_0.down

    # piece_4 case:
    turned_cube.piece_4.front = ''
    turned_cube.piece_4.down = ''
    turned_cube.piece_4.right = ''
    turned_cube.piece_4.back = cube.piece_6.back
    turned_cube.piece_4.up = cube.piece_6.right
    turned_cube.piece_4.left = cube.piece_6.up

    # piece_6 case:
    turned_cube.piece_6.left = ''
    turned_cube.piece_6.down = ''
    turned_cube.piece_6.front = ''
    turned_cube.piece_6.back = cube.piece_2.back
    turned_cube.piece_6.right = cube.piece_2.down
    turned_cube.piece_6.up = cube.piece_2.right

    # others:
    turned_cube.piece_1 = cube.piece_1
    turned_cube.piece_3 = cube.piece_3
    turned_cube.piece_5 = cube.piece_5
    turned_cube.piece_7 = cube.piece_7
    return turned_cube

def r_inverse_turn(cube):
    #print 'turn the right face inversely'
    piece_0 = Piece(0, ['', '', '', '', '', ''])
    piece_1 = Piece(1, ['', '', '', '', '', ''])
    piece_2 = Piece(2, ['', '', '', '', '', ''])
    piece_3 = Piece(3, ['', '', '', '', '', ''])
    piece_4 = Piece(4, ['', '', '', '', '', ''])
    piece_5 = Piece(5, ['', '', '', '', '', ''])
    piece_6 = Piece(6, ['', '', '', '', '', ''])
    piece_7 = Piece(7, ['', '', '', '', '', ''])


    turned_cube = Cube([piece_0, piece_1, piece_2, piece_3, piece_4, piece_5, piece_6, piece_7])
    # right turn will influence piece_2, piece_3, piece_6, piece_7

    # piece_2 case:
    turned_cube.piece_2.front = ''
    turned_cube.piece_2.up = ''
    turned_cube.piece_2.left = ''
    turned_cube.piece_2.right = cube.piece_3.right
    turned_cube.piece_2.down = cube.piece_3.front
    turned_cube.piece_2.back = cube.piece_3.down
    
    # piece_3 case:
    turned_cube.piece_3.up = ''
    turned_cube.piece_3.left = ''
    turned_cube.piece_3.back = ''
    turned_cube.piece_3.right = cube.piece_7.right
    turned_cube.piece_3.down = cube.piece_7.front
    turned_cube.piece_3.front = cube.piece_7.up

    # piece_6 case:
    turned_cube.piece_6.front = ''
    turned_cube.piece_6.left = ''
    turned_cube.piece_6.down = ''
    turned_cube.piece_6.right = cube.piece_2.right
    turned_cube.piece_6.back = cube.piece_2.down
    turned_cube.piece_6.up = cube.piece_2.back

    # piece_7 case:
    turned_cube.piece_7.left = ''
    turned_cube.piece_7.back = ''
    turned_cube.piece_7.down = ''
    turned_cube.piece_7.right = cube.piece_6.right
    turned_cube.piece_7.front = cube.piece_6.up
    turned_cube.piece_7.up = cube.piece_6.back
    
    # others:
    turned_cube.piece_0 = cube.piece_0
    turned_cube.piece_1 = cube.piece_1
    turned_cube.piece_4 = cube.piece_4
    turned_cube.piece_5 = cube.piece_5
    return turned_cube

def l_inverse_turn(cube):
    #print 'turn the left face inversely'
    piece_0 = Piece(0, ['', '', '', '', '', ''])
    piece_1 = Piece(1, ['', '', '', '', '', ''])
    piece_2 = Piece(2, ['', '', '', '', '', ''])
    piece_3 = Piece(3, ['', '', '', '', '', ''])
    piece_4 = Piece(4, ['', '', '', '', '', ''])
    piece_5 = Piece(5, ['', '', '', '', '', ''])
    piece_6 = Piece(6, ['', '', '', '', '', ''])
    piece_7 = Piece(7, ['', '', '', '', '', ''])


    turned_cube = Cube([piece_0, piece_1, piece_2, piece_3, piece_4, piece_5, piece_6, piece_7])
    # left turn will influence piece_0, piece_1, piece_4, piece_5

    # piece_0 case:
    turned_cube.piece_0.up = ''
    turned_cube.piece_0.front = ''
    turned_cube.piece_0.right = ''
    turned_cube.piece_0.left = cube.piece_4.left
    turned_cube.piece_0.down = cube.piece_4.back
    turned_cube.piece_0.back = cube.piece_4.up

    # piece_1 case:
    turned_cube.piece_1.up = ''
    turned_cube.piece_1.right = ''
    turned_cube.piece_1.back = ''
    turned_cube.piece_1.left = cube.piece_0.left
    turned_cube.piece_1.down = cube.piece_0.back
    turned_cube.piece_1.front = cube.piece_0.down

    # piece_4 case:
    turned_cube.piece_4.right = ''
    turned_cube.piece_4.front = ''
    turned_cube.piece_4.down = ''
    turned_cube.piece_4.left = cube.piece_5.left
    turned_cube.piece_4.back = cube.piece_5.up
    turned_cube.piece_4.up = cube.piece_5.front

    # piece_5 case:
    turned_cube.piece_5.right = ''
    turned_cube.piece_5.back = ''
    turned_cube.piece_5.down = ''
    turned_cube.piece_5.left = cube.piece_1.left
    turned_cube.piece_5.front = cube.piece_1.down
    turned_cube.piece_5.up = cube.piece_1.front

    # others:
    turned_cube.piece_2 = cube.piece_2
    turned_cube.piece_3 = cube.piece_3
    turned_cube.piece_6 = cube.piece_6
    turned_cube.piece_7 = cube.piece_7
    return turned_cube

def u_inverse_turn(cube):
    #print 'turn the up face inversely'
    piece_0 = Piece(0, ['', '', '', '', '', ''])
    piece_1 = Piece(1, ['', '', '', '', '', ''])
    piece_2 = Piece(2, ['', '', '', '', '', ''])
    piece_3 = Piece(3, ['', '', '', '', '', ''])
    piece_4 = Piece(4, ['', '', '', '', '', ''])
    piece_5 = Piece(5, ['', '', '', '', '', ''])
    piece_6 = Piece(6, ['', '', '', '', '', ''])
    piece_7 = Piece(7, ['', '', '', '', '', ''])


    turned_cube = Cube([piece_0, piece_1, piece_2, piece_3, piece_4, piece_5, piece_6, piece_7])
    # up turn will influence piece_4, piece_5, piece_6, piece_7

    # piece_4 case:
    turned_cube.piece_4.right = ''
    turned_cube.piece_4.front = ''
    turned_cube.piece_4.down = ''
    turned_cube.piece_4.up = cube.piece_6.up
    turned_cube.piece_4.left = cube.piece_6.back
    turned_cube.piece_4.back = cube.piece_6.right

    # piece_5 case:
    turned_cube.piece_5.back = ''
    turned_cube.piece_5.right = ''
    turned_cube.piece_5.down = ''
    turned_cube.piece_5.up = cube.piece_4.up
    turned_cube.piece_5.front = cube.piece_4.left
    turned_cube.piece_5.left = cube.piece_4.back

    # piece_6 case:
    turned_cube.piece_6.left = ''
    turned_cube.piece_6.front = ''
    turned_cube.piece_6.down = ''
    turned_cube.piece_6.up = cube.piece_7.up
    turned_cube.piece_6.back = cube.piece_7.right
    turned_cube.piece_6.right = cube.piece_7.front

    # piece_7 case:
    turned_cube.piece_7.left = ''
    turned_cube.piece_7.back = ''
    turned_cube.piece_7.down = ''
    turned_cube.piece_7.up = cube.piece_5.up
    turned_cube.piece_7.right = cube.piece_5.front
    turned_cube.piece_7.front = cube.piece_5.left

    # others:
    turned_cube.piece_0 = cube.piece_0
    turned_cube.piece_1 = cube.piece_1
    turned_cube.piece_2 = cube.piece_2
    turned_cube.piece_3 = cube.piece_3
    return turned_cube

def d_inverse_turn(cube):
    #print 'turn the down face inversely'
    piece_0 = Piece(0, ['', '', '', '', '', ''])
    piece_1 = Piece(1, ['', '', '', '', '', ''])
    piece_2 = Piece(2, ['', '', '', '', '', ''])
    piece_3 = Piece(3, ['', '', '', '', '', ''])
    piece_4 = Piece(4, ['', '', '', '', '', ''])
    piece_5 = Piece(5, ['', '', '', '', '', ''])
    piece_6 = Piece(6, ['', '', '', '', '', ''])
    piece_7 = Piece(7, ['', '', '', '', '', ''])


    turned_cube = Cube([piece_0, piece_1, piece_2, piece_3, piece_4, piece_5, piece_6, piece_7])
    # down turn will influence piece_0, piece_1, piece_2, piece_3

    # piece_0 case:
    turned_cube.piece_0.right = ''
    turned_cube.piece_0.front = ''
    turned_cube.piece_0.up = ''
    turned_cube.piece_0.down = cube.piece_1.down
    turned_cube.piece_0.back = cube.piece_1.left
    turned_cube.piece_0.left = cube.piece_1.front

    # piece_1 case:
    turned_cube.piece_1.back = ''
    turned_cube.piece_1.right = ''
    turned_cube.piece_1.up = ''
    turned_cube.piece_1.down = cube.piece_3.down
    turned_cube.piece_1.left = cube.piece_3.front
    turned_cube.piece_1.front = cube.piece_3.right

    # piece_2 case:
    turned_cube.piece_2.left = ''
    turned_cube.piece_2.up = ''
    turned_cube.piece_2.front = ''
    turned_cube.piece_2.down = cube.piece_0.down
    turned_cube.piece_2.back = cube.piece_0.left
    turned_cube.piece_2.right = cube.piece_0.back

    # piece_3 case:
    turned_cube.piece_3.up = ''
    turned_cube.piece_3.left = ''
    turned_cube.piece_3.back = ''
    turned_cube.piece_3.down = cube.piece_2.down
    turned_cube.piece_3.right = cube.piece_2.back
    turned_cube.piece_3.front = cube.piece_2.right

    # others:
    turned_cube.piece_4 = cube.piece_4
    turned_cube.piece_5 = cube.piece_5
    turned_cube.piece_6 = cube.piece_6
    turned_cube.piece_7 = cube.piece_7
    return turned_cube

def f_inverse_turn(cube):
    #print 'turn the front face inversely'
    piece_0 = Piece(0, ['', '', '', '', '', ''])
    piece_1 = Piece(1, ['', '', '', '', '', ''])
    piece_2 = Piece(2, ['', '', '', '', '', ''])
    piece_3 = Piece(3, ['', '', '', '', '', ''])
    piece_4 = Piece(4, ['', '', '', '', '', ''])
    piece_5 = Piece(5, ['', '', '', '', '', ''])
    piece_6 = Piece(6, ['', '', '', '', '', ''])
    piece_7 = Piece(7, ['', '', '', '', '', ''])


    turned_cube = Cube([piece_0, piece_1, piece_2, piece_3, piece_4, piece_5, piece_6, piece_7])
    # front turn will influence piece_1, piece_3, piece_5, piece_7

    # piece_1 case:
    turned_cube.piece_1.right = ''
    turned_cube.piece_1.back = ''
    turned_cube.piece_1.up = ''
    turned_cube.piece_1.front = cube.piece_5.front
    turned_cube.piece_1.down = cube.piece_5.left
    turned_cube.piece_1.left = cube.piece_5.up

    # piece_3 case:
    turned_cube.piece_3.back = ''
    turned_cube.piece_3.left = ''
    turned_cube.piece_3.up = ''
    turned_cube.piece_3.front = cube.piece_1.front
    turned_cube.piece_3.right = cube.piece_1.down
    turned_cube.piece_3.down = cube.piece_1.left

    # piece_5 case:
    turned_cube.piece_5.right = ''
    turned_cube.piece_5.back = ''
    turned_cube.piece_5.down = ''
    turned_cube.piece_5.front = cube.piece_7.front
    turned_cube.piece_5.up = cube.piece_7.right
    turned_cube.piece_5.left = cube.piece_7.up

    # piece_7 case:
    turned_cube.piece_7.down = ''
    turned_cube.piece_7.left = ''
    turned_cube.piece_7.back = ''
    turned_cube.piece_7.front = cube.piece_3.front
    turned_cube.piece_7.right = cube.piece_3.down
    turned_cube.piece_7.up = cube.piece_3.right

    # others:
    turned_cube.piece_0 = cube.piece_0
    turned_cube.piece_2 = cube.piece_2
    turned_cube.piece_4 = cube.piece_4
    turned_cube.piece_6 = cube.piece_6
    return turned_cube

def b_inverse_turn(cube):
    #print 'turn the back face inversely'
    piece_0 = Piece(0, ['', '', '', '', '', ''])
    piece_1 = Piece(1, ['', '', '', '', '', ''])
    piece_2 = Piece(2, ['', '', '', '', '', ''])
    piece_3 = Piece(3, ['', '', '', '', '', ''])
    piece_4 = Piece(4, ['', '', '', '', '', ''])
    piece_5 = Piece(5, ['', '', '', '', '', ''])
    piece_6 = Piece(6, ['', '', '', '', '', ''])
    piece_7 = Piece(7, ['', '', '', '', '', ''])


    turned_cube = Cube([piece_0, piece_1, piece_2, piece_3, piece_4, piece_5, piece_6, piece_7])
    # back turn will influence piece_0, piece_2, piece_4, piece_6

    # piece_0 case:
    turned_cube.piece_0.right = ''
    turned_cube.piece_0.front = ''
    turned_cube.piece_0.up = ''
    turned_cube.piece_0.back = cube.piece_2.back
    turned_cube.piece_0.left = cube.piece_2.down
    turned_cube.piece_0.down = cube.piece_2.right

    # piece_2 case:
    turned_cube.piece_2.left = ''
    turned_cube.piece_2.up = ''
    turned_cube.piece_2.front = ''
    turned_cube.piece_2.back = cube.piece_6.back
    turned_cube.piece_2.down = cube.piece_6.right
    turned_cube.piece_2.right = cube.piece_6.up

    # piece_4 case:
    turned_cube.piece_4.front = ''
    turned_cube.piece_4.down = ''
    turned_cube.piece_4.right = ''
    turned_cube.piece_4.back = cube.piece_0.back
    turned_cube.piece_4.up = cube.piece_0.left
    turned_cube.piece_4.left = cube.piece_0.down

    # piece_6 case:
    turned_cube.piece_6.left = ''
    turned_cube.piece_6.down = ''
    turned_cube.piece_6.front = ''
    turned_cube.piece_6.back = cube.piece_4.back
    turned_cube.piece_6.right = cube.piece_4.up
    turned_cube.piece_6.up = cube.piece_4.left

    # others:
    turned_cube.piece_1 = cube.piece_1
    turned_cube.piece_3 = cube.piece_3
    turned_cube.piece_5 = cube.piece_5
    turned_cube.piece_7 = cube.piece_7
    return turned_cube




final_status = ' ' * 2 + 'B' * 2 + '\n' + ' ' * 2 + 'B' * 2 + '\n' + 'O' * 2 + 'Y' * 2 + 'R' * 2 + 'W' * 2 + '\n' + 'O' * 2 + 'Y' * 2 + 'R' * 2 + 'W' * 2 + '\n' + ' ' * 2 + 'G' * 2 + '\n' + ' ' * 2 + 'G' * 2

def get_start_state():
    return [0, cube_test, []]

def is_goal_state(cube):
    #return cube.get_status() == final_status
    return cube.piece_4.up == 'W' and cube.piece_5.up == 'W' and cube.piece_6.up == 'W' and cube.piece_7.up == 'W' and cube.piece_5.front == 'G' and cube.piece_7.front == 'G' and cube.piece_6.right == 'R' and cube.piece_7.right == 'R' and cube.piece_4.left == 'O' and cube.piece_5.left == 'O' and cube.piece_4.back == 'B' and cube.piece_6.back == 'B'


def solve_first_layer():
    frontier = []
    visited = []
    dict1 = {}
    frontier.append(get_start_state())

    while frontier:
        nowCost, nowNode, nowpath = frontier.pop()
        if nowNode.get_status() not in visited:
            visited.append(nowNode.get_status())
            dict1[nowNode.get_status()] = nowpath
            if is_goal_state(nowNode):
                print nowpath
                print nowNode.get_status()
                return [0, nowNode, nowpath], visited, dict1
            else:
                if nowCost >= 7:
                    continue
                r_turned = r_turn(nowNode)
                frontier.append([nowCost + 1, r_turned, nowpath + ['r']])
               
                l_turned = l_turn(nowNode)
                frontier.append([nowCost + 1, l_turned, nowpath + ['l']])
                
                u_turned = u_turn(nowNode)
                frontier.append([nowCost + 1, u_turned, nowpath + ['u']])

                d_turned = d_turn(nowNode)
                frontier.append([nowCost + 1, d_turned, nowpath + ['d']])

                f_turned = f_turn(nowNode)
                frontier.append([nowCost + 1, f_turned, nowpath + ['f']])

                b_turned = b_turn(nowNode)
                frontier.append([nowCost + 1, b_turned, nowpath + ['b']])
                
                r_inverse_turned = r_inverse_turn(nowNode)
                frontier.append([nowCost + 1, r_inverse_turned, nowpath + ['r_']])
                
                l_inverse_turned = l_inverse_turn(nowNode)
                frontier.append([nowCost + 1, l_inverse_turned, nowpath + ['l_']])
                
                u_inverse_turned = u_inverse_turn(nowNode)
                frontier.append([nowCost + 1, u_inverse_turned, nowpath + ['u_']])
                
                d_inverse_turned = d_inverse_turn(nowNode)
                frontier.append([nowCost + 1, d_inverse_turned, nowpath + ['d_']])
                
                f_inverse_turned = f_inverse_turn(nowNode)
                frontier.append([nowCost + 1, f_inverse_turned, nowpath + ['f_']])
               
                b_inverse_turned = b_inverse_turn(nowNode)
                frontier.append([nowCost + 1, b_inverse_turned, nowpath + ['b_']])
                
    return None, visited , dict1
first_layer, visited , dict1 = solve_first_layer()


piece_0 = Piece(0, ['', '', 'B', 'O', '', 'Y'])
piece_1 = Piece(1, ['G', '', '', 'O', '', 'Y'])
piece_2 = Piece(2, ['', 'R', 'B', '', '', 'Y'])
piece_3 = Piece(3, ['G', 'R', '', '', '', 'Y'])
piece_4 = Piece(4, ['', '', 'B', 'O', 'W', ''])
piece_5 = Piece(5, ['G', '', '', 'O', 'W', ''])
piece_6 = Piece(6, ['', 'R', 'B', '', 'W', ''])
piece_7 = Piece(7, ['G', 'R', '', '', 'W', ''])

right_cube = Cube([piece_0, piece_1, piece_2, piece_3, piece_4, piece_5, piece_6, piece_7])

def unsolve():
    frontier = []
    visited = []
    dict2 = {}
    frontier.append([0, right_cube, []])

    while frontier:
        nowCost, nowNode, nowpath = frontier.pop()
        if nowNode.get_status() not in visited:
            visited.append(nowNode.get_status())
            dict2[nowNode.get_status()] = nowpath
            if nowCost >= 7:
                continue
            r_turned = r_turn(nowNode)
            frontier.append([nowCost + 1, r_turned, nowpath + ['r_']])
           
            l_turned = l_turn(nowNode)
            frontier.append([nowCost + 1, l_turned, nowpath + ['l_']])
            
            u_turned = u_turn(nowNode)
            frontier.append([nowCost + 1, u_turned, nowpath + ['u_']])

            d_turned = d_turn(nowNode)
            frontier.append([nowCost + 1, d_turned, nowpath + ['d_']])

            f_turned = f_turn(nowNode)
            frontier.append([nowCost + 1, f_turned, nowpath + ['f_']])

            b_turned = b_turn(nowNode)
            frontier.append([nowCost + 1, b_turned, nowpath + ['b_']])
            
            r_inverse_turned = r_inverse_turn(nowNode)
            frontier.append([nowCost + 1, r_inverse_turned, nowpath + ['r']])
            
            l_inverse_turned = l_inverse_turn(nowNode)
            frontier.append([nowCost + 1, l_inverse_turned, nowpath + ['l']])
            
            u_inverse_turned = u_inverse_turn(nowNode)
            frontier.append([nowCost + 1, u_inverse_turned, nowpath + ['u']])
            
            d_inverse_turned = d_inverse_turn(nowNode)
            frontier.append([nowCost + 1, d_inverse_turned, nowpath + ['d']])
            
            f_inverse_turned = f_inverse_turn(nowNode)
            frontier.append([nowCost + 1, f_inverse_turned, nowpath + ['f']])
           
            b_inverse_turned = b_inverse_turn(nowNode)
            frontier.append([nowCost + 1, b_inverse_turned, nowpath + ['b']])
            
    return None, visited , dict2

path, un_visited , dict2 = unsolve()

for status in visited:
    if status in un_visited:
        print dict1[status]
        print dict2[status]
        break








