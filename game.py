#   Simple RPG
#  Level up system?
#  Choose your own adventure system?
#  
# 
# TO DO:
# Get Character Fighting.
# Get Health, money, and Experience Points both working
# Get a shop working
# 


# Using the class method to create an object
import random


class character:
    def __init__(self, name, job, level, armor, attack, health, experience, gold):
        self.name = name
        self.job = job
        self.level = level
        self.armor = armor
        self.attack = attack
        self.health = health
        self.experience = experience
        self.gold = gold


class protagonist(character):
    def __init__(self, name, job, level, armor, attack, health, experience, gold, \
        exploration):
        
        self.name = name
        self.job = job
        self.level = level
        self.armor = armor
        self.attack = attack
        self.health = health
        self.experience = experience
        self.gold = gold



# Empty Variable which is filled in on our newGame function
player = None

# Monsters that were created
# Name, Job, level, armor, attack, health, exp, $$
goblin = character('Goblin', 'Goblin', 2, 0, 1, 8, 30, 10)
rat = character('Rat', 'Animal', 1, 0, 1, 3, 10, 5)
knight = character('Knight', 'Knight', 10, 20, 20, 100, 500, 300)
dragon = character('Dragon', 'Dragon', 100, 100, 100, 1000, 1000000000, 1000000000)
peasant = character('Villager', 'Peasant', 5, 2, 3, 15, 100, 30)
wolf = character('Wolf', 'Animal', 3, 2, 2, 5, 15, 10)

monsters = [goblin, rat, knight, dragon, peasant, wolf]


# THINK OF HOW THIS FIGHT IS GOING TO WORK...
# What is the loop of the fight?
# Someone goes first, then opponent goes. etc.
# 
# 


def fight():
    global player
    orderInput = input("What is your choice? ")
    order(orderInput)


def order(input):
    global player
    enemy = random.choice(monsters)
    
    if input.lower() == 'attack':
        first = random.choice([0, 1])
        print(player.name,"versus",enemy.name)
        
        if first != 0:
            firstTurn(player, enemy)
        else:
            firstTurn(enemy, player)

    elif input.lower() == 'run':
        runAway()
        question()
    elif input.lower() == 'defend':
        defend()
    elif input.lower() == 'help':
        fightHelp()
        fight()
    elif input.lower() == 'die':
        death()
    else:
        print("Sorry, I cannot recognize your choice!")
        fight()

def runAway():
    global player
    print(player.name,'runs away!')                

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

    fHealth = first.health
    sHealth = second.health

    fAttack = first.attack
    sAttack = second.attack

    print(fName,'goes first!')
    print(fName,'attacks',sName)
    print(sName,'takes',fAttack,'damage!')
    sHealth = attacked(sHealth, fAttack)
    if sHealth <= 0:
        if sName == player.name:
            print(sName,'has been slayed!')
            print('-' * 50)
            death()
        else:
            print(sName,'has been slayed!')
            print(fName,'does a sweet victory dance!')
            question()
    else:
        secondTurn(first, second)

def secondTurn(first, second):
    global player
    fName = first.name
    sName = second.name

    fHealth = first.health
    sHealth = second.health

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
            question()
    else:
        print('-' * 50)
        fight()

def newGame():
    global player
    playerName = input('What is your character\'s name? ')
    playerJob = input('What is your character\'s job? ')
    player = protagonist(playerName, playerJob, 1, 1, 3, 10, 0, 0, 0)
    intro(player)
    question()

def question():
    global player
    help()
    print('-' * 50)
    playerChoice = input(player.name +"! What would you like to do? ")
    action(playerChoice)


def wander():
    # Placeholder
    print("You take a deep breath and take in the countryside...")
    print('-' * 50)
    question()

def save():
    # Placeholder
    print("Saving... JK IT'S NOT DONE YET!")
    cont = input('Would you like to continue playing? Y/n' )
    if cont == 'Y':
        question()
    else:
        quit()

def action(playerChoice):
    print("Your choice was:", playerChoice)
    print('-' * 50)
    if playerChoice.lower() == "fight":
        fight()
    elif playerChoice.lower() == 'wander':
        wander()
        # Placeholder
        question()
    elif playerChoice.lower() == 'stats':
        printInfo(player)
        question()
    elif playerChoice.lower() == 'save':
        save()
        question()
    elif playerChoice.lower() == 'help':
        help()
        question()
    elif playerChoice.lower() == 'end':
        print('Good Bye!')
    elif playerChoice.lower() =='die':
        death()
    else:
        print('Choice not found, please try again')
        print('-' * 50)
        question()


def death():
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
    question()


def intro(player):
    print('Hello',player.name + '!')
    print('Here are your stats! ')
    print()
    printInfo(player)

def printInfo(something):
    # print('-' * 50)
    print('Job:',something.job)
    print('Level:',something.level)
    print('HP:',something.health)
    print('Attack:',something.attack)
    print('Armor:',something.armor)
    print('Experience:',something.experience)
    print('Gold:',something.gold)
    print('-' * 50)

newGame()





