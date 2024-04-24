def isogram(word:str) -> bool:
    newWord = word.lower()
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    string = ''
    for i in newWord:
        if len(set(i)&set(alpha)) > 0:
            string = string+i
    setIso = set(string)
    lenIso = len(string)
    lensetIso = len(setIso)
    if lenIso == lensetIso:
        return True
    else:
        return False
assert (isogram('background')==True)
assert (isogram('lumberjacks')==True)
assert (isogram('downstream')==True)
assert (isogram('six-year-old')==True)
assert (isogram('Baby')==False)
assert (isogram('ICCS101')==False)
assert (isogram('00-MuiC-00')==True)
assert (isogram('APefLtMXCdKUJWO')==True)
assert (isogram('keIzsx-T_QCHFa^')==True)
assert (isogram('o ~_?#ha?cj~Pxw')==True)
assert (isogram('kQsN~ciyJvJyNq~')==False)
assert (isogram('qyeyTikaT%PoIzp')==False)
assert (isogram('h!KLKFhEfDLrijo')==False)
assert (isogram('~%#tF^l~i^AQKud')==True)
assert (isogram('koFsSQVTvxZJJLo')==False)
assert (isogram('&PJ%&Z~#!No&H_w')==True)
assert (isogram('_aFgixdsWzfcqDA')==False)