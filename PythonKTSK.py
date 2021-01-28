#Autor: Sander Kulma IT20b
#Kuupäev: 10.12.2020
#Tiitel: 
import random
import os.path

score = 0
user = input("Insert your players name!: ")
if os.path.isfile(user+".txt")==True:
    print("Player has been already created")
    print("Using existing accounts data")
    s = open(user+".txt", 'r').read()
#     Health = int(eval(s)["Health"])
#     Strenght = int(eval(s)["Strenght"])
#     Defence = int(eval(s)["Defence"])
#     Magic = int(eval(s)["Magic"])
#     print("Health:",(Health))
#     print("Strenght:", (Strenght))
#     print("Defence:", (Defence))
#     print("Magic:", (Magic))
else:
    print("Creating account")
    
#Hero classes
class warrior (object):
    health = 60
    strength = 15
    defence = 10
    magic = 2
    
class wizard (object):
    health = 40
    strength = 4
    defence = 13
    magic = 12
    
class paladin (object):
    health = 45
    strength = 16
    defence = 12
    magic = 0
class rogue (object):
    health = 31
    strength = 14
    defence = 24
    magic = 1
#Enemy
class bear (object):
    name = "Bear"
    health = 40
    strength = 11
    defence = 5
    loot = random.randint(0,2)
class goblin (object):
    name = "Goblin"
    health = 25
    strength = 3
    defence = 4
    loot = random.randint(0,2)
class mouse (object):
    name = "Mouse"
    health = 15
    strength = 3
    defence = 15
    loot = random.randint(0,2)
class boar (object):
    name = "Boar"
    health = 34
    strength = 14
    defence = 14
    loot = random.randint(0,2)
#Score
def gameover(character, score):
    if character.health < 1:
        print("You have no health left")
        print("Thanks for playing")
        print("You have scored", score)
        exit()
#Hero select
def heroselect():
    print("Select your class!")
    selection = input("1. Warrior \n2. Wizard \n3. Paladin \n4. Rogue \n")
    if selection == "1":
        character = warrior
        print("You have selected class Warrior, these are the Warriors statistics")
        print("Health - ", character.health)
        print("Strength - ", character.strength)
        print("Defence - ", character.defence)
        print("Magic - ", character.defence)
        return character
    elif selection == "2":
        character = wizard
        print("You have selected class Wizard, these are the Wizards statistics")
        print("Health - ", character.health)
        print("Strength - ", character.strength)
        print("Defence - ", character.defence)
        print("Magic - ", character.defence)
        return character
    elif selection == "3":
        character = paladin
        print("You have selected class Paladin, these are the Paladins statistics")
        print("Health - ", character.health)
        print("Strength - ", character.strength)
        print("Defence - ", character.defence)
        print("Magic - ", character.defence)
        return character
    elif selection == "4":
        character = rogue
        print("You have selected class Rogue, these are the Rogues statistics")
        print("Health - ", character.health)
        print("Strength - ", character.strength)
        print("Defence - ", character.defence)
        print("Magic - ", character.defence)
        return character
    else:
        print("Only press 1, 2, 3 or 4")
        heroselect()
def saving():
    if os.path.isfile(user+".txt")==True:
        print("User already exists")
    else:
        f = open(user+".txt", "w")
        print("User has been created!")
        
        dict = {
            "Health": character.health,
            "Strength": character.strength,
            "Defence": character.defence,
            "Magic": character.defence}
        f.write(str(dict))
        f.close()
def enemyselect(bear,goblin,mouse,boar):
    enemylist = [bear,goblin,mouse,boar]
    chance = random.randint(0,3)
    enemy = enemylist[chance]
    return enemy

def loot():
    loot = ["Potion", "Gold", "Shield", "Armor", "Melee weapon", "Food"]
    lootchance = random.randint(0,3)
    lootdrop = loot[lootchance]
    return lootdrop

def battlestate():
    score = 0
    enemy = enemyselect(bear,goblin,mouse,boar)
    print("A wild", enemy.name, "has appeared!")
    print("You will have 3 options!")
    while enemy.health > 0 :
        choice = input("1. Sword\n2. Magic \n3. RUN!")
        if choice == "1":
            print("You slashed the", enemy.name, "with your sword!")
            hitchance = random.randint(0,10)
            if hitchance > 3:
                enemy.health = enemy.health - character.strength
                print("You slashed the enemy, the opponents health is now..", enemy.health)
                score = score + 5
                print(score)
        if choice == "2":
            print("You hit the", enemy.name, "with your spell!")
            hitchance = random.randint(0,10)
            if hitchance > 5:
                enemy.health = enemy.health - character.strength
                print("You hit the enemy, the opponents health is now..", enemy.health)
                score = score + 5
                print(score)
        if choice == "3":
            danger = input("1. Yes \n2. No \n")
            print("You have ran away, like a coward")
            character.health =  0
            score = score - 5
            print(score)
            if enemy.health > 0:
                character.health = character.health - (enemy.strength/character.defence)
                print("The", enemy.name, "takes a swing, it hits you leaving", character.health, "health")
                gameover(character, score)
            else:
                if enemy.name == "bear":
                        enemy.health = 30
                        score = score + 10
                        return score
                elif enemy.name == "goblin":
                        enemy.health = 12
                        score = score + 10
                        return score
                elif enemy.name == "mouse":
                        enemy.health = 9
                        score = score + 5
                        return score
                elif enemy.name == "boar":
                        enemy.health = 17
                        score = score + 15
                        return score
                        print("You have defeated", enemy.name)
                        print("Looks like it has dropped something for you!")
                        lootdrop = loot()
                        print("You have got a", lootdrop)
                        break
                else:
                    print("Your sword has slipped from your grasp, you've fumbled and missed!")
                    print("The", enemy.name, "hits you for full damage!")
                    character.health = character.health - enemy.strength
                    print("You now have", character.health, "left")
                    gameover(character, score)
        elif choice == "3":
            print("You're trying to run!")
            runchance = random.randint(1,10)
            if runchance > 4:
                print("You were untouchable!")
                break
            else:
                print("You tried to run, but you slipped and fell!")
                print("You tried defending, but you couldn't")
                character.health = character.health = enemy.strength
                print("Your health is now", character.health)
                gameover(character, score)
                
character = heroselect()
saving()
print(battlestate())