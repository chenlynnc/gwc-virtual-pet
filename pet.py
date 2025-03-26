class Pet:
    MOOD = ['sad','mad','happy','excited','chill','stressed','relaxed','hungry','onthevergeofdeath']
    # Static variable: max xp possible
    # Add dict of skill levels, OR make the current skills dict values an int pair [exp, level]

    def __init__(self, name):
        self.name = name
        self.hunger = 80
        self.hydration_level = 0
        self.happiness = 60
        self.currency = 0
        self.skills = { # "Skill": 0 exp
            "Resting" : 0,
            "Productivity" : 0,
            "Outside" : 0,
            "Hydrate" : 0,
            "Connecting" : 0
        }
        self.mood = "chill"
        self.xp = 0  # Max 50 for now?
        self.age = 0 # Add list of ages: 0 = baby, 1 = toddler, 2 = child, 3 = teen, 4 = adult
        self.level = { # "Skill": level
            "Resting" : 0,
            "Productivity" : 0,
            "Outside" : 0,
            "Hydrate" : 0,
            "Connecting" : 0
        }

    def printStats(self):
        print(f"Name: {self.name}")
        print(f"Hunger: {self.hunger}")
        print(f"Happiness: {self.happiness}")
        print(f"Currency: {self.currency}")
        print(f"Mood: {self.mood}")
        print(f"Experience points: {self.xp}")
        return

    '''
    using feed(amount) will make the pet more full.
    if hunger is 30/100, feed(15) will make hunger 45/100
    hunger caps out at 100
    does it increase exp?
    '''
    def feed(self, amount):
        return
    
    def rest(self):
        # Add XP for resting?
        self.addXP(10, "Rest") # we can change the points if we would like, bc idk how much sleep
        
        #should we increase energy level by like 20 and max at 100?
        if self.energy_level < 100:
            self.energy_level += 20
        if self.energy_level > 100:
            self.energy_level = 100 #how do we ensure that this won't exceed 100? 
            
        print(f"{self.name}'s energy level is now {self.energy_level}%.")

        #We can make a fun little message about resting 
        print(f"Time to rest and rechage, {self.name}!!! Zzzzz...")

        return self.energy_level
    
    #Hopefully it will run like this 
    #my_pet = Pet("Buddy")
    #my_pet.rest()
    # Output:
    #buddy earned 20 XP for rest! Total XP : 20
    #Buddy's energy level is now 70%.
    # Time to rest and recharge, buddy! Zzzzz....

    def hydrate(self):
        # when you hydrate your pet, adds XP, and will update the level
        self.addXp(5, "Hydrate")

        # increase hydration level by 5? (max out 100? what #)
        if self.hydration_level < 100:
                self.hydration_level += 5
                if self.hydration_level > 100:
                    self.hydration_level = 100
        print(f"{self.name}'s hydration level is now {self.hydration_level}%.")


        print("Time to drink some water!")
              #alternativly we could do a different phrase like the joke we said before liek hydrate or diedrate or be like take a break and take a sip! IDK
        
        return self.hydration_level

    #technically we can use what i would call like a pet instance so it would be 
        # my_pet = Pet("Buddy")
        # to then hydrate the pet
        # my_pet.hydrate()
        # output :
        # buddy earned 5 XP for Hydrate! Total XP: 5
        # buddy's hydration level is now 20%
        # then do the print statement/ have it say that 

    def beProductive(self):
        # make "Productivity" skill increase exp
        self.addXp(5, "Productivity")

        return
    
    def goOutside(self):
        # Play == hobbies?
        # max 50 for now
        
        #Call the method addxp #self, experience, skill = None
        self.addXp(5, "Outside") #Adds to the outside skill. Am i doing this right? 
        
        return
    
    def connectWith(self):
        # make "COnnecting" skill increase exp
        self.addXp(5, "Connecting")
        return
    
    '''
    using levelUp() will increase the pet's age by 1.
        only happens IF all skills are at the same level already.
        increase happiness
    prevent age from surpassing 4 (adult)?
    '''
    # if (all skills are at level 1)
        # then we can "age up" from baby to toddler
    # else if (some skills are not level 1 yet)
        # then we stay a baby

    # min_value = min(myDictionary.values())
    def checkAgeUp(self, skill):
        #Check level of skill
        current_level = self.level[skill]

        
        
        if all(skill == current_level for skill in self.level.values()):
            if self.age < len(self.level):

#DOnt let the age go past the LAST one
#might need self.age level -> increase it to increase age. 
#Use if else to check that ALL skills are leveled up. If at least one is left pet does NOT age. 

    def levelUp(self):
        print(f"Congrats, you leveled up to: {self.age}")
        self.age += 1 #0/baby, 1-toddler, 2-child, 3-teen, 4-adult
        return
    
    '''
    Levels up skills.
    Increase happiness
    '''
    def skillLevelUp(self, skill):
        print("Congrats, you leveled up you skill!!")
        self.level[skill] += 1 
        return
    
    '''
    Today: Handle leveling up skills.
    '''
    def addXp(self, experience, skill = None):
        

        if skill == None: # addXp(5)
            self.xp += experience # 1. experience gets added
            print(f"{self.name} earned {experience} XP!")
            
            if self.xp > 50: # 2. check if xp has surpassed max xp limit (aka xp should never surpass 50)
                self.xp -= 50 # When xp reaches 50, subtract past xp -> go to a new level.
                self.levelUp() #3. if so, level up and set xp backward
                
        else:
            self.skills[skill] += experience
            
            print(f"{self.name} earned {experience} XP for the {skill} skill!")

            #Check if skill levels up
            if self.skills[skill] >= 20: 
                self.skills[skill] -= 20 #Reset the XP after the skill is leveld up
                self.skillLevelUp(skill)
        return

#age and XP are the same thing, how do you want to do it?
#0/baby, toddler, child, teen, adult
#  0       1.       2.     3.    4
#outside, hydrate, eat, sleep, productivity(for study and such), connecting with yourself
#daily positive quote ^)
#hunger, happiness, mood, age, currency, skills