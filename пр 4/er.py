#A
def a():
    for y in range(7):
        row = ""
        for x in range(5):
            if y == 0:
                if x == 0:
                    row = row + " "
                if x == 1 or x == 2 or x == 3:
                    row = row + "*"
                if x == 4:
                    row = row + " "
            if y == 1 or y == 2 or y == 4 or y == 5 or y == 6:
                if x == 0:
                    row = row + "*"
                if x == 1 or x == 2 or x == 3:
                    row = row + " "
                if x == 4:
                    row = row + "*"
            if y == 3:
                row = row + "*"
        print(row)

#B
def b():
    for y in range(7):
        row = ""
        for x in range(5):
            if y == 0 or y == 3 or y == 6:
                if x == 0 or x == 1 or x == 2 or x == 3:
                    row = row + "*"
                if x == 4:
                    row = row + " "
            if y == 1 or y == 2 or y == 4 or y == 5:
                if x == 0:
                    row = row + "*"
                if x == 1 or x == 2 or x == 3:
                    row = row + " "
                if x == 4:
                    row = row + "*"
        print(row)

#C
def c():
    for y in range(7):
        row = ""
        for x in range(5):
            if y == 0 or y == 6:
                if x == 0 or x == 4:
                    row = row + " "
                if x == 1 or x == 2 or x == 3:
                    row = row + "*"
            if y == 1 or y == 5:
                if x == 0 or x == 4:
                    row = row + "*"
                if x == 1 or x == 2 or x == 3:
                    row = row + " "
            if y == 2 or y == 3 or y == 4:
                if x == 0:
                    row = row + "*"
                if x == 1 or x == 2 or x == 3:
                    row = row + " "
        print(row)

#D
def d():
    for y in range(7):
        row = ""
        for x in range(5):
            if y == 0 or  y == 6:
                if x == 0 or x == 1 or x == 2 or x == 3:
                    row = row + "*"
                if x == 4:
                    row = row + " "
            if y == 1 or y == 2 or y == 3 or y == 4 or y == 5:
                if x == 0:
                    row = row + "*"
                if x == 1 or x == 2 or x == 3:
                    row = row + " "
                if x == 4:
                    row = row + "*"
        print(row)

#E
def e():
    for y in range(7):
        row = ""
        for x in range(5):
            if y == 0 or y == 6:
                if x == 0 or x == 1 or x == 2 or x == 3 or x == 4:
                    row = row + "*"
            if y == 1 or y == 2 or y == 4 or y == 5:
                if x == 0:
                    row = row + "*"
                if x == 1 or x == 2 or x == 3 or x == 4:
                    row = row + " "
            if y == 3:
                if x == 0 or x == 1 or x == 2:
                    row = row + "*"
                if x == 3 or x == 4:
                    row = row + " "
        print(row)

#F
def f():
    for y in range(7):
        row = ""
        for x in range(5):
            if y == 0:
                if x == 0 or x == 1 or x == 2 or x == 3 or x == 4:
                    row = row + "*"
            if y == 1 or y == 2 or y == 4 or y == 5 or y == 6:
                if x == 0:
                    row = row + "*"
                if x == 1 or x == 2 or x == 3 or x == 4:
                    row = row + " "
            if y == 3:
                if x == 0 or x == 1 or x == 2:
                    row = row + "*"
                if x == 3 or x == 4:
                    row = row + " "
        print(row)

#G
def g():
    for y in range(7):
        row = ""
        for x in range(5):
            if y == 0 or y == 6:
                if x == 0 or x == 4:
                    row = row + " "
                if x == 1 or x == 2 or x == 3:
                    row = row + "*"
            if y == 1 or y == 5 or y == 4:
                if x == 0 or x == 4:
                    row = row + "*"
                if x == 1 or x == 2 or x == 3:
                    row = row + " "
            if y == 2:
                if x == 0:
                    row = row + "*"
                if x == 1 or x == 2 or x == 3 or x == 4:
                    row = row + " "
            if y == 3:
                if x == 0 or x == 3 or x == 4:
                    row = row + "*"
                if x == 1 or x == 2:
                    row = row + " "
        print(row)

#H
def h():
    for y in range(7):
        row = ""
        for x in range(5):
            if y == 0 or y == 1 or y == 2 or y == 4 or y == 5 or y == 6:
                if x == 0:
                    row = row + "*"
                if x == 1 or x == 2 or x == 3:
                    row = row + " "
                if x == 4:
                    row = row + "*"
            if y == 3:
                row = row + "*"
        print(row)

#I
def i():
    for y in range(7):
        row = ""
        for x in range(5):
            if y == 0 or y == 6:
                if x == 0 or x == 4:
                    row = row + " "
                if x == 1 or x == 2 or x == 3:
                    row = row + "*"
            if y == 1 or y == 2 or y == 3 or y == 4 or y == 5:
                if x == 0 or x == 1 or x == 3 or x == 4:
                    row = row + " "
                if x == 2:
                    row = row + "*"
        print(row)

#J
def j():
    for y in range(7):
        row = ""
        for x in range(5):
            if y == 0:
                if x == 0 or x == 4:
                    row = row + " "
                if x == 1 or x == 2 or x == 3:
                    row = row + "*"
            if y == 1 or y == 2 or y == 3 or y == 4 or y == 5:
                if x == 0 or x == 1 or x == 3 or x == 4:
                    row = row + " "
                if x == 2:
                    row = row + "*"
            if y == 6:
                if x == 0 or x == 1:
                    row = row + "*"
                if x == 2 or x == 3 or x == 4:
                    row = row + " "
        print(row)

#K
def k():
    for y in range(7):
        row = ""
        for x in range(5):
            if y == 0 or y == 6:
                if x == 0 or x == 4:
                    row = row + "*"
                if x == 1 or x == 2 or x == 3:
                    row = row + " "
            if y == 1 or y == 5:
                if x == 0 or x == 3:
                    row = row + "*"
                if x == 1 or x == 2 or x == 4:
                    row = row + " "
            if y == 2 or y == 4:
                if x == 0 or x == 2:
                    row = row + "*"
                if x == 1 or x == 3 or x == 4:
                    row = row + " "
            if y == 3:
                if x == 0 or x == 1:
                    row = row + "*"
                if x == 2 or x == 3 or x == 4:
                    row = row + " "
        print(row)

#L
def l():
    for y in range(7):
        row = ""
        for x in range(5):
            if y == 0 or y == 1 or y == 2 or y == 3 or  y == 4 or y == 5:
                if x == 0:
                    row = row + "*"
                if x == 1 or x == 2 or x == 3 or x == 4:
                    row = row + " "
            if y == 6:
                row = row + "*"
        print(row)

#M
def m():
    for y in range(7):
        row = ""
        for x in range(5):
            if y == 0 or y == 1 or  y == 4 or y == 5 or y == 6:
                if x == 0:
                    row = row + "*"
                if x == 1 or x == 2 or x == 3:
                    row = row + " "
                if x == 4:
                    row = row + "*"
            if y == 2:
                if x == 0 or x == 1 or x == 3 or x == 4:
                    row = row + "*"
                if x == 2:
                    row = row + " "
            if y == 3:
                if x == 1 or x == 3:
                    row = row + " "
                if x == 0 or x == 2 or x == 4:
                    row = row + "*"
        print(row)

#N
def n():
    for y in range(7):
        row = ""
        for x in range(5):
            if y == 0 or y == 1 or  y == 5 or y == 6:
                if x == 0:
                    row = row + "*"
                if x == 1 or x == 2 or x == 3:
                    row = row + " "
                if x == 4:
                    row = row + "*"
            if y == 2:
                if x == 0 or x == 1 or x == 4:
                    row = row + "*"
                if x == 2 or x == 3 :
                    row = row + " "
            if y == 4:
                if x == 0 or x == 3 or x == 4:
                    row = row + "*"
                if x == 1 or x == 2 :
                    row = row + " "
            if y == 3:
                if x == 1 or x == 3:
                    row = row + " "
                if x == 0 or x == 2 or x == 4:
                    row = row + "*"
        print(row)

#O
def o():
    for y in range(7):
        row = ""
        for x in range(5):
            if y == 0 or y == 6:
                if x == 0 or x == 4:
                    row = row + " "
                if x == 1 or x == 2 or x == 3:
                    row = row + "*"
            if y == 1 or y == 2 or y == 3 or  y == 4 or y == 5:
                if x == 0 or x == 4:
                    row = row + "*"
                if x == 1 or x == 2 or x == 3:
                    row = row + " "
        print(row)

#p
def p():
    for y in range(7):
        row = ""
        for x in range(5):
            if y == 0 or y == 3:
                if x == 0 or x == 1 or x == 2 or x == 3:
                    row = row + "*"
                if x == 4:
                    row = row + " "
            if y == 1 or y == 2:
                if x == 0:
                    row = row + "*"
                if x == 1 or x == 2 or x == 3:
                    row = row + " "
                if x == 4:
                    row = row + "*"
            if y == 4 or y == 5 or y == 6:
                if x == 0:
                    row = row + "*"
                if x == 1 or x == 2 or x == 3 or x == 4:
                    row = row + " "
        print(row)

#Q
def q():
    for y in range(7):
        row = ""
        for x in range(5):
            if y == 0:
                if x == 0 or x == 4:
                    row = row + " "
                if x == 1 or x == 2 or x == 3:
                    row = row + "*"
            if y == 1 or y == 2 or y == 3 or  y == 4 :
                if x == 0 or x == 4:
                    row = row + "*"
                if x == 1 or x == 2 or x == 3:
                    row = row + " "
            if y == 5:
                if x == 1 or x == 2 or x == 4:
                    row = row + " "
                if x == 0 or x == 3:
                    row = row + "*"
            if y == 6:
                if x == 0 or x == 3:
                    row = row + " "
                if x == 1 or x == 2 or x == 4:
                    row = row + "*"
        print(row)

#R
def r():
    for y in range(7):
        row = ""
        for x in range(5):
            if y == 0 or y == 3:
                if x == 0 or x == 1 or x == 2 or x == 3:
                    row = row + "*"
                if x == 4:
                    row = row + " "
            if y == 1 or y == 2:
                if x == 0:
                    row = row + "*"
                if x == 1 or x == 2 or x == 3:
                    row = row + " "
                if x == 4:
                    row = row + "*"
            if y == 4:
                if x == 0 or x == 2:
                    row = row + "*"
                if x == 1  or x == 3 or x == 4:
                    row = row + " "
            if y == 5:
                if x == 0 or x == 3:
                    row = row + "*"
                if x == 1  or x == 2 or x == 4:
                    row = row + " "
            if y == 6:
                if x == 0 or x == 4:
                    row = row + "*"
                if x == 1  or x == 2 or x == 3:
                    row = row + " "
        print(row)

#S
def s():
    for y in range(7):
        row = ""
        for x in range(5):
            if y == 0:
                if x == 0:
                    row = row + " "
                if x == 1 or x == 2 or x == 3 or x == 4:
                    row = row + "*"
            if y == 1 or y == 2:
                if x == 0:
                    row = row + "*"
                if x == 1 or x == 2 or x == 3 or x == 4:
                    row = row + " "
            if y == 3 or y == 6:
                if x == 0 or x == 4:
                    row = row + " "
                if x == 1 or x == 2 or x == 3:
                    row = row + "*"
            if y == 4 or y == 5:
                if x == 4:
                    row = row + "*"
                if x == 0 or x == 1 or x == 2 or x == 3:
                    row = row + " "
        print(row)

#T
def t():
    for y in range(7):
        row = ""
        for x in range(5):
            if y == 0:
                row = row + "*"
            if y == 1 or y == 2 or y == 3 or y == 4 or y == 5 or y == 6:
                if x == 2:
                    row = row + "*"
                if x == 0 or x == 1 or x == 3 or x == 4:
                    row = row + " "
        print(row)

#U
def u():
    for y in range(7):
        row = ""
        for x in range(5):
            if y == 0 or y == 1 or y == 2 or y == 3 or y == 4 or y == 5:
                if x == 0 or x == 4:
                    row = row + "*"
                if x == 1 or x == 2 or x == 3:
                    row = row + " "
            if y == 6:
                if x == 0 or x == 4:
                    row = row + " "
                if x == 1 or x == 2 or x == 3:
                    row = row + "*"
        print(row)

#V
def v():
    for y in range(7):
        row = ""
        for x in range(5):
            if y == 0 or y == 1 or y == 2 or y == 3 or y == 4:
                if x == 0 or x == 4:
                    row = row + "*"
                if x == 1 or x == 2 or x == 3:
                    row = row + " "
            if y == 5:
                if x == 0 or x == 2 or x == 4:
                    row = row + " "
                if x == 1 or x == 3:
                    row = row + "*"
            if y == 6:
                if x == 0 or x == 1 or x == 3 or x == 4:
                    row = row + " "
                if x == 2:
                    row = row + "*"
        print(row)

#W
def w():
    for y in range(7):
        row = ""
        for x in range(5):
            if y == 0 or y == 1 or  y == 2 or y == 5 or y == 6:
                if x == 0:
                    row = row + "*"
                if x == 1 or x == 2 or x == 3:
                    row = row + " "
                if x == 4:
                    row = row + "*"
            if y == 4:
                if x == 0 or x == 1 or x == 3 or x == 4:
                    row = row + "*"
                if x == 2:
                    row = row + " "
            if y == 3:
                if x == 1 or x == 3:
                    row = row + " "
                if x == 0 or x == 2 or x == 4:
                    row = row + "*"
        print(row)

#X
def x():
    for y in range(7):
        row = ""
        for x in range(5):
            if y == 0 or y == 1 or y == 5 or y == 6:
                if x == 0 or x == 4:
                    row = row + "*"
                if x == 1 or x == 2 or x == 3:
                    row = row + " "
            if y == 2 or y == 4:
                if x == 1 or x == 3:
                    row = row + "*"
                if x == 0 or x == 2 or x == 4:
                    row = row + " "
            if y == 3:
                if x == 0 or x == 1 or x == 3 or x == 4:
                    row = row + " "
                if x == 2:
                    row = row + "*"
        print(row)

#Y
def y():
    for y in range(7):
        row = ""
        for x in range(5):
            if y == 0 or y == 1:
                if x == 0 or x == 4:
                    row = row + "*"
                if x == 1 or x == 2 or x == 3:
                    row = row + " "
            if y == 2:
                if x == 1 or x == 3:
                    row = row + "*"
                if x == 0 or x == 2 or x == 4:
                    row = row + " "
            if y == 3 or y == 4 or y == 5 or y == 6:
                if x == 0 or x == 1 or x == 3 or x == 4:
                    row = row + " "
                if x == 2:
                    row = row + "*"
        print(row)

#Z
def z():
    for y in range(7):
        row = ""
        for x in range(5):
            if y == 0 or y == 6:
                row = row + "*"
            if y == 1:
                if x == 0 or x == 1 or x == 2 or x == 3:
                    row = row + " "
                if x == 4:
                    row = row + "*"
            if y == 2:
                if x == 0 or x == 1 or x == 2 or x == 4:
                    row = row + " "
                if x == 3:
                    row = row + "*"
            if y == 3:
                if x == 0 or x == 1 or x == 3 or x == 4:
                    row = row + " "
                if x == 2:
                    row = row + "*"
            if y == 4:
                if x == 0 or x == 2 or x == 3 or x == 4:
                    row = row + " "
                if x == 1:
                    row = row + "*"
            if y == 5:
                if x == 1 or x == 2 or x == 3 or x == 4:
                    row = row + " "
                if x == 0:
                    row = row + "*"
        print(row)