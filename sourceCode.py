
class Person:    # blueprint parent class
    def __init__(self, name, relation, age, mainTrait, secondaryTrait, communicationMethod):
        self.name = name
        self.relation = relation
        self.age = age
        self.mainTrait = mainTrait
        self.secondaryTrait = secondaryTrait
        self.communicationMethod = communicationMethod
        
    
    def aboutMe(self):
        print("I am {} we met due to {} I am {:E} years old I am {} and {} I am best communicated with {}".format(self.name, self.relation, self.age, self.mainTrait, self.secondaryTrait, self.communicationMethod))
    
# 1st Object
Person1 = Person("Harysh", "friend", 10, "Potato", "Carrot", "whipped")   

print(Person1)
Person1.aboutMe()

"""
class familyMember(Person):    # child class 1   
    def __init__ (self, ) 
    super().__init__(name, relation, age, mainTrait, secondaryTrait, communicationMethod):
    self.

class innerFriend(Person):    # child class 2 
    def __init__(self, name, mainTrait, secondaryTrait)
    super().__init__(name, relation, age, mainTrait, secondaryTrait, communicationMethod, nationality, ethnicity):
    self.nationality = nationality
    self.ethnicity = ethnicity

    def aboutMe(self):
       
class outerFriend(Person):    # child class 3
    def __init__(self, name, 
    super().__init__(name, relation, age, mainTrait, secondaryTrait, communicationMethod, nationality):
    self.nationality = nationality

class aquaintance(Person):    # child class 4 
    def __init__(self, name, 
    super().__init__(name, relation, age, mainTrait, secondaryTrait, communicationMethod):
                 
"""              
