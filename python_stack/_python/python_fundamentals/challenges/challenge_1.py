def removeBlanks(str):
    newStr = ""
    for x in str:
        if x != ' ':
            newStr += x
    return newStr

print(removeBlanks("Hello      World"))


#---------------------------------------------------------

def getStringDigits(str):
    newStr = ""
    li = ['0','1','2','3','4','5','6','7','8','9']
    for x in str:
        for y in li:
            if x == y:
                newStr += x
    return newStr

print(getStringDigits("12hbef&*7823"))


#---------------------------------------------------------


def acronyms(str):
    isSpace = 1
    newStr = ""
    for x in str:
        if isSpace == 1:
            if x != ' ':
                newStr += x
                isSpace = 0
        if x == ' ':
            isSpace = 1
    return newStr.upper()
    

print(acronyms("   there's            no free lunch -     gotta pay yer way"))

#----------------------------------------------------------
