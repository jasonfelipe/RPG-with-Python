#   Simple RPG
#  Level up system?
#  Choose your own adventure system?
#  
# TO DO:
# Get Character Fighting.
# Get Health, money, and Experience Points both working
# Get a shop working
# Equip system?
# Get inventory system


# Questions for yourself:
# Hey, why not Template literals in Python instead of concatenation? 
# (%s replaces variable names after.)
# Example: 
# 
# name = Jason
# x = "%s is new to coding Python!" % (name) 
# 
# 
# Is having a dictionary full of other dictionaries of lists 
# for text worth more than using a 
# function to print out strings? 


# =============================================
#               GLOBAL STUFF
# =============================================

# Using the class method to create an object
import random

explorationTxt = {
    'Noob': ["You take a deep breath and take in the countryside...",
        "You look around and think to yourself, 'where am I?'"],
    'Scrub': ['You look around you, everything seems so fresh and new!',
        "You feel like walking somewhere... but where?"],
    'Novice': ['Your wandering leads you to some caves, a small fort, and a village...',
        "You feel like you'll gain some sort of benefit going through these areas..."],
    'Average': ['You find a road and keep walking on it...',
        'At the end you find a city and are allowed to enter!',
        'You go into the local tavern and strike a conversation with the locals...',
        'You find out other areas of exploration! Get out there!'],
    'Apprentice': ['You feel connected to the area you are in...',
        'But inside yourself you know that there is more out there...'],
    'Experienced': ["You feel well-travelled, but there are some places you've yet to explore...",
        "You've heard of other islands, cities, and small villages.",
        "The choice is yours, go and get out there!"],
    'Veteran': ['You have walked the paths to walk, but...',
        "You wonder what other secrets this place holds...",
        'You have heard rumors from local mercenaries of hidden caves, underwater habitats, and sky realms.'],
    'Master': ['You feel like you know this place better than yourself, and yet...',
        'You almost feel connected to the world...',
        'Something is missing though.',
        'Something... otherworldly...'],
    'Grandmaster': ['Congrats you have travelled the entire world!',
        'You feel accomplished... but...' ,
        'Your legs hurt too much and you die.'],
    
}

class Character:
    def __init__(self, name, job, level, maxHealth, currentHealth, attack, armor, experience, gold):
        self.name = name
        self.job = job
        self.level = level
        self.maxHealth = maxHealth
        self.currentHealth = currentHealth
        self.attack = attack
        self.armor = armor
        self.experience = experience
        self.gold = gold
        pass


class NewProtagonist(Character):
    def __init__(self, name, job):
        exploration = 0
        self.name = name
        self.job = job
        self.level = 1
        self.maxHealth = 100
        self.currentHealth = 100
        self.attack = 5
        self.armor = 3
        self.experience = 0
        self.gold = 0
        self.exploration = 0
        super().__init__(name, job, self.level, self.maxHealth, self.currentHealth, self.attack, self.armor, self.experience, self.gold)


# Empty Variable which is filled in on our newGame function
player = None

# Monsters that were created
# Name, Job, level, armor, attack, currentHealth, maxHealth, exp, $$
goblin = Character('Goblin', 'Humanoid', 2, 0, 1, 8, 8, 30, 10)
rat = Character('Rat', 'Animal', 1, 0, 1, 3, 3, 10, 5)
# knight = Character('Knight', 'Knight', 10, 20, 20, 100, 100, 500, 300)
# dragon = Character('Dragon', 'Dragon', 100, 100, 100, 1000, 1000, 1000000000, 1000000000)
peasant = Character('Villager', 'Peasant', 5, 2, 3, 15, 15, 100, 30)
wolf = Character('Wolf', 'Animal', 3, 2, 2, 5, 5, 15, 10)

monsters = [goblin, rat, peasant, wolf]

# =============================================
#               INFO STUFF
# =============================================

def intro(player):
    print('Hello',player.name + '!')
    print('Here are your stats! ')
    print()
    printInfo(player)

def printInfo(something):
    # print('-' * 50)
    print('Job:',something.job)
    print('Level:',something.level)
    print('HP:',something.currentHealth, '/',something.maxHealth)
    print('Attack:',something.attack)
    print('Armor:',something.armor)
    print('Experience:',something.experience)
    print('Gold:',something.gold)
    print('-' * 50)

    
def printTxtArray(arr):
    for x in arr:
        print (x)

# Begins the game


def newGame():
    global player
    playerName = input('What is your character\'s name? ')
    playerJob = input('What is your character\'s job? ')

# Name, Job, level, armor, attack, health, exp, $$, exploration
    player = NewProtagonist(playerName, playerJob)
    intro(player)
    command()


# =============================================
#               BATTLE STUFF
# =============================================

# THINK OF HOW THIS FIGHT IS GOING TO WORK...
# What is the loop of the fight?
# Someone goes first, then opponent goes. etc.
# 
# 

# Stuff to do: 
# Display Enemy stats before and after combat.
# Make function that actually carries health and stuff.
# Make it so exp and gold go into the Protagonist.
# Rejoice!

def fight(enemy):
    global player
    fightHelp()
    try: 
        enemy
    except NameError:
        enemy = random.choice(monsters)
        print('Your enemy is:', enemy.name)
        battleChoice = input("What is your choice? ")
        battle(battleChoice, enemy)
    else: 
        print('Your enemy is:', enemy.name)
        battleChoice = input("What is your choice? ")
        battle(battleChoice, enemy)

def turnOrder(player, enemy):
    first = random.choice([0, 1])
    print(player.name,"versus",enemy.name)
        
    if first != 0:
        firstTurn(player, enemy)
    else:
        firstTurn(enemy, player)


def battle(input, enemy):
    global player    
    if input.lower() == 'attack':
        turnOrder(player, enemy)
    elif input.lower() == 'run':
        runAway()
        command()
    elif input.lower() == 'defend':
        defend()
        turnOrder(enemy, player)
    elif input.lower() == 'help':
        fightHelp()
        fight(enemy)
    elif input.lower() == 'die':
        death()
    else:
        print("Sorry, your choice isn't recognized!")
        fight(enemy)

def runAway():
    global player
    print(player.name,'runs away!')
    print("-" * 50)                

def defend():
    global player
    armor = player.armor * 2
    print(player.name,'defends! They now have', armor,'armor!')

def attacked(health, attack):
    health = health - attack
    return health

# Some checks will need to be done,
# did fName or sName use a skill?
# How do we check that?
# what does the skill do?

def firstTurn(first, second):
    global player
    fName = first.name
    sName = second.name

    fHealth = first.currentHealth
    sHealth = second.currentHealth

    fAttack = first.attack
    sAttack = second.attack


    print(fName,'goes first!')
    print(fName,'attacks',sName)
    print(sName,'takes',fAttack,'damage!')
    sHealth = attacked(sHealth, fAttack)

    print(sName, 'is now at', sHealth)

    if sHealth <= 0:
        if sName == player.name:
            print(sName,'has been slayed!')
            print('-' * 50)
            death()
        else:
            print(sName,'has been slayed!')
            print(fName,'does a sweet victory dance!')
            player.currentHealth = fHealth

            print("Player's health is:",player.currentHealth)
            command()
    else:

        secondTurn(first, second)

def secondTurn(first, second):
    global player
    fName = first.name
    sName = second.name

    fHealth = first.currentHealth
    sHealth = second.currentHealth

    fAttack = first.attack
    sAttack = second.attack

    print(sName,'winces in pain!')
    print(sName,'counters',fName)
    print(fName,'takes',sAttack,'damage!')
    fHealth = attacked(fHealth, sAttack)
    if fHealth <= 0:
        if fName == player.name:
            print(fName,'has been slayed!')
            print('-' * 50)
            death()
        else:
            print()
            print(fName,'has been slayed!')
            print(sName,'does a sweet victory dance!')
            print('-' * 50)        
            player.currentHealth = sHealth
            print("Player health is:", player.currentHealth)
            command()
    else:
        print('-' * 50)
        if fName == player.name:
            fight(second)
        else: 
            fight(first)

# =============================================
#              EXPLORATION STUFF
# =============================================
def wander():
    global player
    # Placeholder
    # To Dos for this:
    # Checks exploration points, unlocks new areas when a certain threshold is there.

    exploreUp()
    print("Your total exploration points are:", player.exploration)

    exploreCheck(player.exploration)
    print('-' * 50)
    command()

def exploreUp():
    global player
    explorePts = player.exploration
    explorePts = explorePts + 1
    player.exploration = explorePts


def exploreCheck(points):
    if points >= 100:
        printTxtArray(explorationTxt.get('Grandmaster'))
    elif points >= 70:
        printTxtArray(explorationTxt.get('Master'))
    elif points >= 50:
        printTxtArray(explorationTxt.get('Experienced'))       
    elif points >= 30:
        printTxtArray(explorationTxt.get('Apprentice'))
    elif points >= 20:
        printTxtArray(explorationTxt.get('Veteran'))
    elif points >= 15:
        printTxtArray(explorationTxt.get('Average'))
    elif points >= 10:
        printTxtArray(explorationTxt.get('Novice'))     
    elif points >= 5:
        printTxtArray(explorationTxt.get('Scrub'))
    elif points >= 1: 
        printTxtArray(explorationTxt.get('Noob'))


# =============================================
#                SAVE STUFF
# =============================================

def save():
    # Placeholder
    # To Dos:
    # Learn how to save something LMAO!
    print("Saving... JK IT'S NOT DONE YET!")
    cont = input('Would you like to continue playing? Y/n ')
    if cont.upper() == 'Y':
        command()
    else:
        print('THANKS FOR PLAYING!')
        quit()

# =============================================
#               COMMAND STUFF
# =============================================

def command():
    global player
    help()
    print('-' * 50)
    playerChoice = input(player.name +"! What would you like to do? ")
    action(playerChoice)

def action(playerChoice):
    print("Your choice was:", playerChoice)
    print('-' * 50)
    if playerChoice.lower() == "fight":
        selectedEnemy = random.choice(monsters)
        fight(selectedEnemy)
    elif playerChoice.lower() == 'wander':
        wander()
        # Placeholder, check out the wander stuff.
        command()
    elif playerChoice.lower() == 'stats':
        printInfo(player)
        command()
    elif playerChoice.lower() == 'save':
        # Placeholder, check out the save stuff.
        save()
        command()
    elif playerChoice.lower() == 'help':
        help()
        command()
    elif playerChoice.lower() == 'end':
        print('Good Bye!')
        
    elif playerChoice.lower() =='die':
        death()
    else:
        print('Choice not found, please try again')
        print('-' * 50)
        command()

def death():
    global player
    print('Thus it was not meant to be...')
    print(player.name,"looks up into the sky...")
    print('With one final breath, he screams and perishes...')
    print()
    print("GAME OVER!")
    quit()

def help():
    print("Here is what you can do:")
    print()
    print('Fight = Fight a random monster')
    print('Wander = Just travel around')
    print('Stats = Take a look at your stats')
    print('Save = Saves your game progress')
    print('End = Ends the Program')

def fightHelp():
    print("Here's what you can do:")
    print()
    print('Attack = Attack the monster, and the monster also attacks you!')
    print('Defend = You defend (Armor x2) for two turns! The monster attacks you still')
    print('Run = RUN TO LIVE ANOTHER DAY!')
    print('-' * 50)


# Begins the game
newGame()





