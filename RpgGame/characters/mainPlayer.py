#modules
import time as cooldown
#Main Player


#class MainPlayer

class MainPlayer:
    def __init__(self):
        self.name = "Maxi"
        self.role = "Knight"
        self.weapon = "Sword"
    
    #attack method
    def attack(self):
        print(f"\nSwinging {self.weapon}")
        cooldown.sleep(1)
        print("+5 damage")
        cooldown.sleep(1.5)
        print(f"\nSwinging {self.weapon}")
        cooldown.sleep(2)
        print("+5 damage")
mPlayer = MainPlayer()