class Pet:
    MOOD = ['sad','mad','happy','excited','chill','stressed','relaxed','hungry','onthevergeofdeath']
    # Add list of ages: baby, toddler, child, teen, adult
    # Static variable: max xp possible

    def __init__(self, name):
        self.name = name
        self.hunger = 80
        self.happiness = 60
        self.currency = 0
        self.skills = {
            "Resting" : 0,
            "Productivity" : 0,
            "Outside" : 0,
            "Hydrate" : 0,
            "Connecting" : 0
        }
        self.mood = "chill"
        self.xp = 0  # Max 50 for now?
        self.age = "baby"

    def printStats(self):
        print(f"Name: {self.name}")
        print(f"Hunger: {self.hunger}")
        print(f"Happiness: {self.happiness}")
        print(f"Currency: {self.currency}")
        print(f"Mood: {self.mood}")
        print(f"Experience points: {self.xp}")
        return

    def feed(self):
        # make hunger go up but caps out at 100
        return
        
    def rest(self):
        # make "resting" skill increase exp
        return
        
    def hydrate(self):
        # make "hydrate" skill increase exp
        return
    
    def beProductive(self):
        # make "Productivity" skill increase exp
        return
        
    def goOutside(self):
        # Play == hobbies?
        # max 50 for now
        self.xp += 10
        
        if self.xp > 50:
            self.xp -= 50 # When xp reaches 50, subtract past xp -> go to a new level.
            self.levelUp(); 
        
        return
    
    def connectWith(self):
        # make "COnnecting" skill increase exp
        return
    
    def levelUp(self):
        print(f"Congrats, you leveled up to: {self.age}")
        self.age += 1 #0/baby, 1-toddler, 2-child, 3-teen, 4-adult
        return
    
    def addXp(self, experience):
        # 1. experience gets added to self.xp
        # 2. check if xp has surpassed max xp limit (aka xp should never surpass 50)
        # 3. if so, level up and set xp backward
        return

#age and XP are the same thing, how do you want to do it?
#0/baby, toddler, child, teen, adult
#  0       1.       2.     3.    4
#outside, hydrate, eat, sleep, productivity(for study and such), connecting with yourself
#daily positive quote ^)
#hunger, happiness, mood, age, currency, skills