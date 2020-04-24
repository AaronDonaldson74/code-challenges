#Build three classes, 
#two of which must inherit from the first and employ polymorphism. Between the three classes, there must be at least 5 methods, 
# 3 instance attributes, 
# 1 class attribute, and 
# the parent class should have a dunder init. 
# If you want you can add dunder str and dunder repr to each class.

class Starcraft:
    minerals = 200
    gas = 200


    def __init__(self, marine):
        self.unit = marine
    
    def getUnit(self):
        return self.unit

class Zerg(Starcraft):

    def __init__(self, marine, stim_pack):
        Starcraft.__init__(self, marine)
        self.weapon = stim_pack

    def getWeapon(self):
        return self.weapon

class Protoss(Zerg):

    def __init__(self, marine, stim_pack, armor):
        Zerg.__init__(self, marine, stim_pack)
        self.protect = armor

    def getArmor(self):
        return self.protect

character = Protoss("Marine", "Stim-pack", "level 3")
print("I play starcraft as a", character.getUnit(), character.getWeapon(), character.getArmor())
print("I have", Starcraft.minerals, "minerals. And", Starcraft.gas, "gas.")