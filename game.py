#   Simple RPG
#  Level up system?
#  Choose your own adventure system?
#  
# 
# 
# 



class character:
    def __init__(self, name, job, level, armor, attack, health, experience):
        self.name = name
        self.job = job
        self.level = level
        self.armor = armor
        self.attack = attack
        self.health = health
        self.experience = experience

player = None


goblin = character('Goblin', 'Goblin', 2, 0, 1, 8, 30)
rat = character('Rat', 'animal', 1, 0, 1, 3, 10)
knight = character('Knight', 'Knight', 10, 20, 20, 100, 500)
dragon = character('Dragon', 'Dragon', 100, 100, 100, 100, 1000000000)
peasant = character('Man', 'Peasant', 5, 2, 3, 15, 100)

monsters = [goblin, rat, knight, dragon, peasant]

def fight():

    opponent = monsters.choice
    print('This should be a battle between two things')
    global player
    print(player "versus" )



def newGame():
    global player
    playerName = input('What is your character\'s name? ')
    playerJob = input('What is your character\'s job? ')
    player = character(playerName, playerJob, 1, 1, 3, 10, 0)
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

def action(playerChoice):
    print("Your choice was:", playerChoice)
    print('-' * 50)
    if playerChoice.lower() == "fight":
        fight()
    elif playerChoice.lower() == 'wander':
        wander()
    elif playerChoice.lower() == 'stats':
        printInfo(player)
        question()
    elif playerChoice.lower() == 'end':
        print('Good Bye!')
    elif playerChoice.lower() == 'save':
        save()
    else:
        print('Choice not found, please try again')
        print('-' * 50)
        question()


def help():
    print("Here is what you can do:")
    print('Fight = Fight a random monster')
    print('Wander = Just travel around')
    print('Stats = Take a look at your stats')
    print('Save = Saves your game progress')
    print('End = Ends the Program')
    print('-' * 50)


def intro(player):
    print('Hello',player.name + '!')
    print('Here are your stats! ')
    printInfo(player)

def printInfo(player):
    print('-' * 50)
    print('Job:',player.job)
    print('Level:',player.level)
    print('HP:',player.health)
    print('Attack:',player.attack)
    print('Armor:',player.armor)
    print('-' * 50)

newGame()
