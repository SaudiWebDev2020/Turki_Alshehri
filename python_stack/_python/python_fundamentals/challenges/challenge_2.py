def parnesValid(str):
    openCount = 0  # open parantheses
    closeCount = 0 # open parantheses

    preStat = 0

    for i in str:
        if i == '(':
            openCount += 1
            preStat = 1
        elif i == ')':
            if preStat == 1:
                closeCount += 1
                preStat = 0
            else:
                return False

    if openCount == closeCount:
        return True
    else:
        return False


print("\nparnesValid:",parnesValid("()n(0(p)3)()")) 


#-----------------------------------------------------------------------------------------------


def bracesValid(str):
    op_bracket = 0
    close_bracket = 0

    op_curBracket = 0
    close_curBracket = 0

    op_para = 0
    close_para = 0

    for i in str:
        if i == '[':
            op_bracket += 1
        elif i == ']':
            close_bracket += 1
        elif i == '{':
            op_curBracket += 1
        elif i == '}':
            close_curBracket += 1
        elif i == '(':
            op_para += 1
        elif i == ')':
            close_para +=1

    if op_bracket == close_bracket and op_curBracket == close_curBracket and op_para == close_para:
        return True
    else:
        return False
    
print("bracesValid:",bracesValid("d(i{a}l[t]o)n{e"), "\n")
        

