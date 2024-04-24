# Assignment 3, Task 5
# Name: Alexander Ogay
# Collaborators:
# Time Spent: 1:00 hrs
def phoneWord2Num(word: str) -> int:
    low = word.lower()
    if 'a' or 'b' or 'c' in low:
        alow = low.replace('a', '2')
        blow = alow.replace('b', '2')
        clow = blow.replace('c', '2')
        if 'd' or 'e' or 'f' in clow:
            dlow = clow.replace('d', '3')
            elow = dlow.replace('e', '3')
            flow = elow.replace('f', '3')
            if 'g' or 'h' or 'i' in flow:
                hlow = flow.replace('g', '4')
                ilow = hlow.replace('h', '4')
                jlow = ilow.replace('i', '4')
                if 'j' or 'k' or 'l' in jlow:
                    klow = jlow.replace('j', '5')
                    llow = klow.replace('k', '5')
                    mlow = llow.replace('l', '5')
                    if 'm' or 'n' or 'o' in mlow:
                        nlow = mlow.replace('m', '6')
                        olow = nlow.replace('n', '6')
                        plow = olow.replace('o', '6')
                        if 'p' or 'q' or 'r' or 's' in plow:
                            qlow = plow.replace('p', '7')
                            rlow = qlow.replace('q', '7')
                            slow = rlow.replace('r', '7')
                            tlow = slow.replace('s', '7')
                            if 't' or 'u' or 'v' in tlow:
                                ulow = tlow.replace('t', '8')
                                vlow = ulow.replace('u', '8')
                                wlow = vlow.replace('v', '8')
                                if 'w' or 'x' or 'y' or 'z' in wlow:
                                    xlow = wlow.replace('w', '9')
                                    ylow = xlow.replace('x', '9')
                                    zlow = ylow.replace('y', '9')
                                    zzlow = zlow.replace('z', '9')
                                    zzlow:int
                                    return zzlow

phoneWord2Num('FLOWERS')