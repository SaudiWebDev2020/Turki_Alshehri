# print all int from 0 - 150

for x in range(0, 151, 1):
    print(x)


#------------------------------

#  Print all the multiples of 5 from 5 to 1,000
print('-'*70)
for x in range(1,201,1):
    print(5*x)

#------------------------------

# Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
print('-'*70)
for x in range(1,101, 1):
    if (x % 5) == 0:
        print("Coding")
    elif x % 10 == 0:
        print("Coding Dojo")



#------------------------------

#  Add odd integers from 0 to 500,000, and print the final sum.
print('-'*70)
sum = 0
for x in range(0,500000,1):
    if (x % 2) != 0:
        sum += x

print(sum)


#------------------------------

#  Print positive numbers starting at 2018, counting down by fours
print('-'*70)
x = 2018
while (x >= 0):
    print(x)
    x -= 4

#------------------------------

#  Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, 
# print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, 
# and mult=3, the loop should print 3, 6, 9 (on successive lines)

lowNum = 2 
highNum = 9
mult = 3

print('-'*70)
for x in range(lowNum, highNum + 1, 1):
    if x % mult == 0:
        print(x)
