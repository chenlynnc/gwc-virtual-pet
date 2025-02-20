class Pet:
    MOOD = ['sad','mad','happy','excited','chill','stressed','relaxed','hungry','onthevergeofdeath']
    
    def __init__(self, name):
        self.name = name
        self.hunger = 80
        self.happiness = 60
        self.currency = 0
        self.skills = {
            "Sleeping" : 0,
            "Productivity" : 0,
            "Outside" : 0,
            "Hydrate" : 0,
            "Connecting" : 0
        }
        self.mood = "chill"
        self.xp = 0

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
        # make "sleeping" skill increase exp
        return
        
    def hydrate(self):
        return
        
    def play(self):
        #Play == hobbies?
        return

#age and XP are the same thing, how do you want to do it?
#0/baby, toddler, child, teen, adult
#outside, hydrate, eat, sleep, productivity(for study and such), connecting with yourself
#daily positive quote ^)
#hunger, happiness, mood, age, currency, skills