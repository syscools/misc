#!/usr/bin/python
#

import sys

def row_desc(r):
    def conv(c):
        return [[' ']*int(x) if x.isdigit() else x for x in c]

    def flatten(arr):
        return [item for sublist in arr for item in sublist]

    return flatten(conv(r))

def row_desc2(r):
    result = []
    for elem in r:
        if elem.isdigit():
            for q in [' ']*int(elem):
                result.append(q)
        else:
            result.append(elem)    
    return result

def fen_desc(F):
    board = []
    for q in F:
        board.append(row_desc2(q))
    return board

L = '+---+---+---+---+---+---+---+---+'
M = '|   |   |   |   |   |   |   |   |'
#      2   6   10

sq = [(2,0),(6,1),(10,2),(14,3),(18,4),(22,5),(26,6),(30,7)]

def draw_board(fenstring):
    board = fen_desc(fenstring.split('/'))
    for row in xrange(8):
        print L

        i = 0
        for x in M:

            def in_sq(n):
                for qq in sq:
                    if n == qq[0]:
                        return qq[1]
                return None

            if in_sq(i) is not None:
                ident = board[row][in_sq(i)]
                sys.stdout.write(ident)
            else:
                sys.stdout.write(x)

            i = i + 1

        print "\n",
    print L

draw_board(sys.argv[1])
