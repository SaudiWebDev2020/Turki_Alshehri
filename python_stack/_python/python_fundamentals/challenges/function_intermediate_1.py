
import random

def randInt(min= 0, max= 100):
    num = random.random() * max + min
    return int(num)

print(randInt())
print(randInt(min=50))
print(randInt(max=120))
print(randInt(min=50, max= 1000))