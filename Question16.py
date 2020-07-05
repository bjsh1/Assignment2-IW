#16. Imagine you are creating a Super Mario game. 
# You need to define a class to represent Mario. 
# What would it look like? If you aren't familiar with SuperMario, use your own favorite video or board game to model a player.

class Mario:
    
    def __init__(self, color):
        
        self.color = color
        self.power = 0
        self.coin = 0
        self.level = 1

    def get_power(self):
        
        self.power += 4
        return self.power

    def collect_coin(self):
        
        self.coin += 1
        return self.coin

    def update_level(self):
        
        if self.level == "success":
            self.level += 1