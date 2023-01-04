#modules
import time as cooldown
#creeps

#class Creeps

class Creeps:
    def __init__(self):
        self.name = "Golem"
        self.role = "Creeper"
        self.weapon = "Rocks"
    
    #attack method
    def attack(self):
        print(f"\nSwinging {self.weapon}")
        cooldown.sleep(1)
        print("+2 damage")
        cooldown.sleep(1.5)
        print(f"\nSwinging {self.weapon}")
        cooldown.sleep(2)
        print("+2 damage")
creeps = Creeps()