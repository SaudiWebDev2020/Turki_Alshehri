def biggie_size(li):
    for x in range(0,len(li),1):
        if li[x] < 0:
            li[x] = 'big'
    return li

print(biggie_size([-1,2,3,4,-1,-3]))

#---------------------------------------

def count_positives(li):
    count = 0
    for x in range(0, len(li), 1):
        if li[x] > 0:
            count += 1
    li[len(li) - 1] = count
    return li


print(count_positives([-1,1,1,1]))

#---------------------------------------

def  sum_total(li):
    sum = 0
    for x in range(0,len(li),1):
        sum += li[x]
    return sum


print("sum:",sum_total([1,2,3]))

#---------------------------------------

def average(li):
    return sum_total(li) / len(li)

print("avg:", average([10,10]))

#---------------------------------------

def length(li):
    return len(li)


print("length:", length([1,2,3,4,5]))

#---------------------------------------

def minimum(li):
    if len(li) == 0:
        return False
    else:
        min = li[0]
        for x in range(1, len(li), 1):
            if li[x] < min:
                min = li[x]
    return min

print("min:", minimum([23,76,54,-9,58,456]))

#---------------------------------------

def maximum(li):
    if len(li) == 0:
        return False
    else:
        max = li[0]
        for x in range(1, len(li), 1):
            if li[x] > max:
                max = li[x]
    return max

print("max:", maximum([23,76,54,-9,58,456]))

#---------------------------------------

def ultimate_analysis(li):
    dict = {"max" : maximum(li), "min" : minimum(li), "avg" : average(li), "len" : length(li)}
    return dict


print(ultimate_analysis([12,4,3,2,56]))

#---------------------------------------

def reverse_list(li):
    j = len(li) - 1
    for x in range(0,len(li),1):
        if x >= j:
            break
        tmp = li[j]
        li[j] = li[x]
        li[x] = tmp
        j -= 1
    return li

print(reverse_list([37,2,1,6,8,0,-9]))


#---------------------------------------

