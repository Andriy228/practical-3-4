word = input("Введіть слово :")

for text in word.lower():
    if text == "a":
        #A
        for y in range(7):
            a = ""
            for x in range(5):
                if y == 0:
                    if x == 0:
                        a = a + " "
                    if x == 1 or x == 2 or x == 3:
                        a = a + "*"
                    if x == 4:
                        a = a + " "
                if y == 1 or y == 2 or y == 4 or y == 5 or y == 6:
                    if x == 0:
                        a = a + "*"
                    if x == 1 or x == 2 or x == 3:
                        a = a + " "
                    if x == 4:
                        a = a + "*"
                if y == 3:
                    a = a + "*"
            print(a)
    elif text == "b":
        #B
        for y in range(7):
            b = ""
            for x in range(5):
                if y == 0 or y == 3 or y == 6:
                    if x == 0 or x == 1 or x == 2 or x == 3:
                        b = b + "*"
                    if x == 4:
                        b = b + " "
                if y == 1 or y == 2 or y == 4 or y == 5:
                    if x == 0:
                        b = b + "*"
                    if x == 1 or x == 2 or x == 3:
                        b = b + " "
                    if x == 4:
                        b = b + "*"
            print(b)
    elif text == "c":
        #C
        for y in range(7):
            c = ""
            for x in range(5):
                if y == 0 or y == 6:
                    if x == 0 or x == 4:
                        c = c + " "
                    if x == 1 or x == 2 or x == 3:
                        c = c + "*"
                if y == 1 or y == 5:
                    if x == 0 or x == 4:
                        c = c + "*"
                    if x == 1 or x == 2 or x == 3:
                        c = c + " "
                if y == 2 or y == 3 or y == 4:
                    if x == 0:
                        c = c + "*"
                    if x == 1 or x == 2 or x == 3:
                        c = c + " "
            print(c)
    elif text == "d":
        #D
        for y in range(7):
            d = ""
            for x in range(5):
                if y == 0 or  y == 6:
                    if x == 0 or x == 1 or x == 2 or x == 3:
                        d = d + "*"
                    if x == 4:
                        d = d + " "
                if y == 1 or y == 2 or y == 3 or y == 4 or y == 5:
                    if x == 0:
                        d = d + "*"
                    if x == 1 or x == 2 or x == 3:
                        d = d + " "
                    if x == 4:
                        d = d + "*"
            print(d)
    elif text == "e":
        #E
        for y in range(7):
            e = ""
            for x in range(5):
                if y == 0 or y == 6:
                    if x == 0 or x == 1 or x == 2 or x == 3 or x == 4:
                        e = e + "*"
                if y == 1 or y == 2 or y == 4 or y == 5:
                    if x == 0:
                        e = e + "*"
                    if x == 1 or x == 2 or x == 3 or x == 4:
                        e = e + " "
                if y == 3:
                    if x == 0 or x == 1 or x == 2:
                        e = e + "*"
                    if x == 3 or x == 4:
                        e = e + " "
            print(e)
    elif text == "f":
        #F
        for y in range(7):
            f = ""
            for x in range(5):
                if y == 0:
                    if x == 0 or x == 1 or x == 2 or x == 3 or x == 4:
                        f = f + "*"
                if y == 1 or y == 2 or y == 4 or y == 5 or y == 6:
                    if x == 0:
                        f = f + "*"
                    if x == 1 or x == 2 or x == 3 or x == 4:
                        f = f + " "
                if y == 3:
                    if x == 0 or x == 1 or x == 2:
                        f = f + "*"
                    if x == 3 or x == 4:
                        f = f + " "
            print(f)
    elif text == "g":
        #G
        for y in range(7):
            g = ""
            for x in range(5):
                if y == 0 or y == 6:
                    if x == 0 or x == 4:
                        g = g + " "
                    if x == 1 or x == 2 or x == 3:
                        g = g + "*"
                if y == 1 or y == 5 or y == 4:
                    if x == 0 or x == 4:
                        g = g + "*"
                    if x == 1 or x == 2 or x == 3:
                        g = g + " "
                if y == 2:
                    if x == 0:
                        g = g + "*"
                    if x == 1 or x == 2 or x == 3 or x == 4:
                        g = g + " "
                if y == 3:
                    if x == 0 or x == 3 or x == 4:
                        g = g + "*"
                    if x == 1 or x == 2:
                        g = g + " "
            print(g)
    elif text == "h":
        #H
        for y in range(7):
            h = ""
            for x in range(5):
                if y == 0 or y == 1 or y == 2 or y == 4 or y == 5 or y == 6:
                    if x == 0:
                        h = h + "*"
                    if x == 1 or x == 2 or x == 3:
                        h = h + " "
                    if x == 4:
                        h = h + "*"
                if y == 3:
                    h = h + "*"
            print(h)
    elif text == "i":
        #I
        for y in range(7):
            i = ""
            for x in range(5):
                if y == 0 or y == 6:
                    if x == 0 or x == 4:
                        i = i + " "
                    if x == 1 or x == 2 or x == 3:
                        i = i + "*"
                if y == 1 or y == 2 or y == 3 or y == 4 or y == 5:
                    if x == 0 or x == 1 or x == 3 or x == 4:
                        i = i + " "
                    if x == 2:
                        i = i + "*"
            print(i)
    elif text == "j":
        #J
        for y in range(7):
            j = ""
            for x in range(5):
                if y == 0:
                    if x == 0 or x == 4:
                        j = j + " "
                    if x == 1 or x == 2 or x == 3:
                        j = j + "*"
                if y == 1 or y == 2 or y == 3 or y == 4 or y == 5:
                    if x == 0 or x == 1 or x == 3 or x == 4:
                        j = j + " "
                    if x == 2:
                        j = j + "*"
                if y == 6:
                    if x == 0 or x == 1:
                        j = j + "*"
                    if x == 2 or x == 3 or x == 4:
                        j = j + " "
            print(j)
    elif text == "k":
        #K
        for y in range(7):
            k = ""
            for x in range(5):
                if y == 0 or y == 6:
                    if x == 0 or x == 4:
                        k = k + "*"
                    if x == 1 or x == 2 or x == 3:
                        k = k + " "
                if y == 1 or y == 5:
                    if x == 0 or x == 3:
                        k = k + "*"
                    if x == 1 or x == 2 or x == 4:
                        k = k + " "
                if y == 2 or y == 4:
                    if x == 0 or x == 2:
                        k = k + "*"
                    if x == 1 or x == 3 or x == 4:
                        k = k + " "
                if y == 3:
                    if x == 0 or x == 1:
                        k = k + "*"
                    if x == 2 or x == 3 or x == 4:
                        k = k + " "
            print(k)
    elif text == "l":
        #L
        for y in range(7):
            l = ""
            for x in range(5):
                if y == 0 or y == 1 or y == 2 or y == 3 or  y == 4 or y == 5:
                    if x == 0:
                        l = l + "*"
                    if x == 1 or x == 2 or x == 3 or x == 4:
                        l = l + " "
                if y == 6:
                    l = l + "*"
            print(l)
    elif text == "m":
        #M
        for y in range(7):
            m = ""
            for x in range(5):
                if y == 0 or y == 1 or  y == 4 or y == 5 or y == 6:
                    if x == 0:
                        m = m + "*"
                    if x == 1 or x == 2 or x == 3:
                        m = m + " "
                    if x == 4:
                        m = m + "*"
                if y == 2:
                    if x == 0 or x == 1 or x == 3 or x == 4:
                        m = m + "*"
                    if x == 2:
                        m = m + " "
                if y == 3:
                    if x == 1 or x == 3:
                        m = m + " "
                    if x == 0 or x == 2 or x == 4:
                        m = m + "*"
            print(m)
    elif text == "n":
        #N
        for y in range(7):
            n = ""
            for x in range(5):
                if y == 0 or y == 1 or  y == 5 or y == 6:
                    if x == 0:
                        n = n + "*"
                    if x == 1 or x == 2 or x == 3:
                        n = n + " "
                    if x == 4:
                        n = n + "*"
                if y == 2:
                    if x == 0 or x == 1 or x == 4:
                        n = n + "*"
                    if x == 2 or x == 3 :
                        n = n + " "
                if y == 4:
                    if x == 0 or x == 3 or x == 4:
                        n = n + "*"
                    if x == 1 or x == 2 :
                        n = n + " "
                if y == 3:
                    if x == 1 or x == 3:
                        n = n + " "
                    if x == 0 or x == 2 or x == 4:
                        n = n + "*"
            print(n)
    elif text == "o":
        #O
        for y in range(7):
            o = ""
            for x in range(5):
                if y == 0 or y == 6:
                    if x == 0 or x == 4:
                        o = o + " "
                    if x == 1 or x == 2 or x == 3:
                        o = o + "*"
                if y == 1 or y == 2 or y == 3 or  y == 4 or y == 5:
                    if x == 0 or x == 4:
                        o = o + "*"
                    if x == 1 or x == 2 or x == 3:
                        o = o + " "
            print(o)
    elif text == "p":
        #p
        for y in range(7):
            p = ""
            for x in range(5):
                if y == 0 or y == 3:
                    if x == 0 or x == 1 or x == 2 or x == 3:
                        p = p + "*"
                    if x == 4:
                        p = p + " "
                if y == 1 or y == 2:
                    if x == 0:
                        p = p + "*"
                    if x == 1 or x == 2 or x == 3:
                        p = p + " "
                    if x == 4:
                        p = p + "*"
                if y == 4 or y == 5 or y == 6:
                    if x == 0:
                        p = p + "*"
                    if x == 1 or x == 2 or x == 3 or x == 4:
                        p = p + " "
            print(p)
    elif text == "q":
        #Q
        for y in range(7):
            q = ""
            for x in range(5):
                if y == 0:
                    if x == 0 or x == 4:
                        q = q + " "
                    if x == 1 or x == 2 or x == 3:
                        q = q + "*"
                if y == 1 or y == 2 or y == 3 or  y == 4 :
                    if x == 0 or x == 4:
                        q = q + "*"
                    if x == 1 or x == 2 or x == 3:
                        q = q + " "
                if y == 5:
                    if x == 1 or x == 2 or x == 4:
                        q = q + " "
                    if x == 0 or x == 3:
                        q = q + "*"
                if y == 6:
                    if x == 0 or x == 3:
                        q = q + " "
                    if x == 1 or x == 2 or x == 4:
                        q = q + "*"
            print(q)
    elif text == "r":
        #R
        for y in range(7):
            r = ""
            for x in range(5):
                if y == 0 or y == 3:
                    if x == 0 or x == 1 or x == 2 or x == 3:
                        r = r + "*"
                    if x == 4:
                        r = r + " "
                if y == 1 or y == 2:
                    if x == 0:
                        r = r + "*"
                    if x == 1 or x == 2 or x == 3:
                        r = r + " "
                    if x == 4:
                        r = r + "*"
                if y == 4:
                    if x == 0 or x == 2:
                        r = r + "*"
                    if x == 1  or x == 3 or x == 4:
                        r = r + " "
                if y == 5:
                    if x == 0 or x == 3:
                        r = r + "*"
                    if x == 1  or x == 2 or x == 4:
                        r = r + " "
                if y == 6:
                    if x == 0 or x == 4:
                        r = r + "*"
                    if x == 1  or x == 2 or x == 3:
                        r = r + " "
            print(r)
    elif text == "s":
        #S
        for y in range(7):
            s = ""
            for x in range(5):
                if y == 0:
                    if x == 0:
                        s = s + " "
                    if x == 1 or x == 2 or x == 3 or x == 4:
                        s = s + "*"
                if y == 1 or y == 2:
                    if x == 0:
                        s = s + "*"
                    if x == 1 or x == 2 or x == 3 or x == 4:
                        s = s + " "
                if y == 3 or y == 6:
                    if x == 0 or x == 4:
                        s = s + " "
                    if x == 1 or x == 2 or x == 3:
                        s = s + "*"
                if y == 4 or y == 5:
                    if x == 4:
                        s = s + "*"
                    if x == 0 or x == 1 or x == 2 or x == 3:
                        s = s + " "
            print(s)
    elif text == "t":
        #T
        for y in range(7):
            t = ""
            for x in range(5):
                if y == 0:
                    t = t + "*"
                if y == 1 or y == 2 or y == 3 or y == 4 or y == 5 or y == 6:
                    if x == 2:
                        t = t + "*"
                    if x == 0 or x == 1 or x == 3 or x == 4:
                        t = t + " "
            print(t)
    elif text == "u":
        #U
        for y in range(7):
            u = ""
            for x in range(5):
                if y == 0 or y == 1 or y == 2 or y == 3 or y == 4 or y == 5:
                    if x == 0 or x == 4:
                        u = u + "*"
                    if x == 1 or x == 2 or x == 3:
                        u = u + " "
                if y == 6:
                    if x == 0 or x == 4:
                        u = u + " "
                    if x == 1 or x == 2 or x == 3:
                        u = u + "*"
            print(u)
    elif text == "v":
        #V
        for y in range(7):
            v = ""
            for x in range(5):
                if y == 0 or y == 1 or y == 2 or y == 3 or y == 4:
                    if x == 0 or x == 4:
                        v = v + "*"
                    if x == 1 or x == 2 or x == 3:
                        v = v + " "
                if y == 5:
                    if x == 0 or x == 2 or x == 4:
                        v = v + " "
                    if x == 1 or x == 3:
                        v = v + "*"
                if y == 6:
                    if x == 0 or x == 1 or x == 3 or x == 4:
                        v = v + " "
                    if x == 2:
                        v = v + "*"
            print(v)
    elif text == "w":
        #W
        for y in range(7):
            w = ""
            for x in range(5):
                if y == 0 or y == 1 or  y == 2 or y == 5 or y == 6:
                    if x == 0:
                        w = w + "*"
                    if x == 1 or x == 2 or x == 3:
                        w = w + " "
                    if x == 4:
                        w = w + "*"
                if y == 4:
                    if x == 0 or x == 1 or x == 3 or x == 4:
                        w = w + "*"
                    if x == 2:
                        w = w + " "
                if y == 3:
                    if x == 1 or x == 3:
                        w = w + " "
                    if x == 0 or x == 2 or x == 4:
                        w = w + "*"
            print(w)
    elif text == "x":
        #X
        for y in range(7):
            xb = ""
            for x in range(5):
                if y == 0 or y == 1 or y == 5 or y == 6:
                    if x == 0 or x == 4:
                        xb = xb + "*"
                    if x == 1 or x == 2 or x == 3:
                        xb = xb + " "
                if y == 2 or y == 4:
                    if x == 1 or x == 3:
                        xb = xb + "*"
                    if x == 0 or x == 2 or x == 4:
                        xb = xb + " "
                if y == 3:
                    if x == 0 or x == 1 or x == 3 or x == 4:
                        xb = xb + " "
                    if x == 2:
                        xb = xb + "*"
            print(xb)
    elif text == "y":
        #Y
        for y in range(7):
            yb = ""
            for x in range(5):
                if y == 0 or y == 1:
                    if x == 0 or x == 4:
                        yb = yb + "*"
                    if x == 1 or x == 2 or x == 3:
                        yb = yb + " "
                if y == 2:
                    if x == 1 or x == 3:
                        yb = yb + "*"
                    if x == 0 or x == 2 or x == 4:
                        yb = yb + " "
                if y == 3 or y == 4 or y == 5 or y == 6:
                    if x == 0 or x == 1 or x == 3 or x == 4:
                        yb = yb + " "
                    if x == 2:
                        yb = yb + "*"
            print(yb)
    elif text == "z":
        #Z
        for y in range(7):
            z = ""
            for x in range(5):
                if y == 0 or y == 6:
                    z = z + "*"
                if y == 1:
                    if x == 0 or x == 1 or x == 2 or x == 3:
                        z = z + " "
                    if x == 4:
                        z = z + "*"
                if y == 2:
                    if x == 0 or x == 1 or x == 2 or x == 4:
                        z = z + " "
                    if x == 3:
                        z = z + "*"
                if y == 3:
                    if x == 0 or x == 1 or x == 3 or x == 4:
                        z = z + " "
                    if x == 2:
                        z = z + "*"
                if y == 4:
                    if x == 0 or x == 2 or x == 3 or x == 4:
                        z = z + " "
                    if x == 1:
                        z = z + "*"
                if y == 5:
                    if x == 1 or x == 2 or x == 3 or x == 4:
                        z = z + " "
                    if x == 0:
                        z = z + "*"
            print(yb)
    else:
        print("     ")