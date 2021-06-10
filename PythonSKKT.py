#Sander Kulma
#10.06.2021
#IT-20

import random
import os.path

#Mu kood valmistab enne teile ette salvestusfaili, kuhu sa sisestad enda nime ja see salvestab kausta.
#Kood prindib intro, mis selgitab mis toimub ja kus sa oled.
#Lihtne ja loogiline RPG mäng, ilma CLASSide ja DEFideta nagu te palusite.
#Mul pole 2hte karakterit, kuna ma ei suutnud välja nuputada, kuidas ma saan valida embakumba, et see katki ei läheks.


#Salvestusfail (Kopeeritud vanast tööst)
user = input("Sisesta kasutaja nimi!: ")
if os.path.isfile(user+".txt")==True:
    print("Kasutaja juba loodud")
    print("Kasutan olemas oleva kasutaja statistikat")
    s = open(user+".txt", 'r').read()
else:
    print("Loon kasutaja")


#Intro
print("Kangelane nimega warrior, kondas ringi väikeses tunnelis, kust ta nägi hästi palju kulda. \nWarrior oli väga uudishimulik ja läks selle juurde. \nKUID hüppas välja selle tagant goblin. \nTe peate ära tapma goblini, et endale saada selle kulla.")

#Karakter
karakter1 = "warrior"
dmg = 10
elud = 100

#Vaenlane
vaenlane1 = "goblin"
dmg1 = 20
elud1 = 50

#Statistika printimine
karakterr = input("1. Warrior")
if karakterr == "1":
    karakter1 = "warrior"
    print("Teie karakteri statistika: ")
    print("Elud -", elud)
    print("DMG -", dmg)
    
#Võitlus
    print("Vaenlane nimega", vaenlane1, "tahab suga kakelda")
    print("Goblini statistika: ")
    print("Elusi on: ", elud1)
    print("DMGi on: ", dmg1)
    while elud1 > 0 :
        valik = input("1. Löö rusikaga\n2. Löö jalaga")
        if valik == "1":
            chance = random.randint(0,10)
            if chance > 3:
                elud1 = elud1 - dmg
                print("Lõid", vaenlane1, "rusikaga näkku")
                print("Goblini elud on nüüd: ", elud1)    
            else:
                print("Lõid", vaenlane1, "rusikaga mööda")
                print("Goblini elud on ikka: ", elud1)
                if elud1 > 0:
                    elud = elud - dmg1
                    print(vaenlane1, "lõi sind vastu tatti ja sul on järel", elud,"elu")
        if valik == "2":
            chance = random.randint(0,10)
            if chance > 3:
                elud1 = elud1 - dmg
                print("Lõid", vaenlane1, "jalaga näkku")
                print("Goblini elud on nüüd: ", elud1)
            else:
                print("Lõid", vaenlane1, "jalaga mööda")
                print("Goblini elud on ikka: ", elud1)
                if elud1 > 0:
                    elud = elud - dmg1
                    print(vaenlane1, "lõi sind vastu tatti ja sul on järel", elud,"elu")
        if elud < 1:
            print("Sa surid ära")
            print("Goblin tantsib su peal ja sülitab sulle vastu nägu naerdes")
            exit()
        if  elud1 <1:
            print("Sa tapsid ära goblini")
            print("Sa kõndisid rahulikult kulla poole goblini verd täis ja said aru, et see oli plastmass kuld.")
            exit()
        
#Salvestus (Kopeeritud vanast tööst)
def saving():
    if os.path.isfile(user+".txt")==True:
        print("Kasutaja juba eksisteerib!")
    else:
        f = open(user+".txt", "w")
        print("Kasutaja on loodud!")
        
        dict = {
            "Teie elud: ": elud,
            "Teie DMG: ": dmg}
        f.write(str(dict))
        f.close()
        
saving()
        

        
        


    





