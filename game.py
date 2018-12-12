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

def fight():
    global player
    enemy = random.choice(monsters)
    first = random.choice([0, 1])
    # print('Number chosen was:',first)

    print('-' * 50)
    print(player.name,"versus",enemy.name)
    if first != 0:
        playerFirst(player.name, enemy.name)
    else:
        enemyFirst(player.name, enemy.name)
                
    print('-' * 50)
    question()


def playerFirst(player, enemy):
    print(player,"goes first!")
    print(player,'attacks',enemy)
    print(enemy,'winces in pain!')
    print(player,'says sorry and leaves...')

def enemyFirst(player, enemy):
    print(enemy,"goes first!")
    print(enemy,'attacks',player)
    print(player,'winces in pain!')
    print(enemy,'says sorry and leaves...')

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
    playerChoice = input(player.name +"! What would you like to do? ")
    action(playerChoice)


def wander():
    # Placeholder
    print("You take a deep breath and take in the countryside...")

def save():
    # Placeholder
    print("Saving... JK IT'S NOT DONE YET!")
    question()

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

def help():
    print("Here is what you can do:")
    print()
    print('Fight = Fight a random monster')
    print('Wander = Just travel around')
    print('Stats = Take a look at your stats')
    print('Save = Saves your game progress')
    print('End = Ends the Program')
    print('-' * 50)

def intro(player):
    print('Hello',player.name + '!')
    print('Here are your stats! ')
    print()
    printInfo(player)

def printInfo(player):
    # print('-' * 50)
    print('Job:',player.job)
    print('Level:',player.level)
    print('HP:',player.health)
    print('Attack:',player.attack)
    print('Armor:',player.armor)
    print('Experience:',player.experience)
    print('Gold:',player.gold)
    print('-' * 50)

newGame()





