def countdown(num):
    li = []
    for x in range(num,-1, -1):
        li.append(x)
    return li

print(countdown(5))

#-----------------------------------------------------

def print_and_return(li):
    print(li[0])
    return li[1]

print(print_and_return([1,2]))

#-----------------------------------------------------

def first_plus_length(li):
    return li[0] + len(li)

print(first_plus_length([1,2,3,4,5]))

#-----------------------------------------------------

def values_greater_than_second(li):
    newlist = []
    for x in li:
        if x > li[1]:
            newlist.append(x)
    print(len(newlist))
    return newlist

print(values_greater_than_second([5,2,3,2,1,4]))

#-----------------------------------------------------

def length_and_value(size, value):
    li = []
    for x in range(0, size, 1):
        li.append(value)
    return li

print(length_and_value(4,7))

#-----------------------------------------------------

