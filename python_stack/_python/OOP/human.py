class Human:

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender


    def eating(self, food):
        print("I am eatting", food)

    
    def moving(self, direction):
        print("I am moving to the",direction)





muhammed = Human("Muhammed", "Male")  #created an object
muhammed.eating("an apple")
muhammed.moving("left")
