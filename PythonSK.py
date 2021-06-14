#Sander Kulma
#10.06.2021
#IT-20

import random
import os.path

#Mu kood valmistab enne teile ette salvestusfaili, kuhu sa sisestad enda nime ja see salvestab kausta.
#Kood prindib intro, mis selgitab mis toimub ja kus sa oled.
#Mul pole 2hte karakterit, kuna ma ei suutnud välja nuputada, kuidas ma saan valida embakumba, et see katki ei läheks.


#Salvestusfail (Kopeeritud vanast tööst)
user = input("Sisesta kasutaja nimi!: ")
if os.path.isfile(user+".txt")==True:
    print("\nKasutaja juba loodud")
    print("\nKasutan olemas oleva kasutaja statistikat")
    s = open(user+".txt", 'r').read()
else:
    print("\nLoon kasutaja")


#Intro
print("\nKangelane nimega warrior, kondas ringi väikeses tunnelis, kust ta nägi hästi palju kulda. \nWarrior oli väga uudishimulik ja läks selle juurde. \nKUID hüppas välja selle tagant goblin. \nTe peate ära tapma goblini, et endale saada selle kulla.")

#Karakter
class warrior (object):
    l66k = 10
    m66k = 50
    m6ttej6ud = 20
    elud = 100

#Vaenlane
class goblin (object):
    dmg1 = 20
    viskamine = 20
    hyppamine = 100
    elud1 = 50

#Statistika printimine
print("\n\nVajutage number ühte, et valida endale warrior!")
karakterr = input("1. Warrior")
if karakterr == "1":
    karakter1 = warrior
    print("\nTeie karakteri statistika: ")
    print("Elud -", karakter1.elud)
    print("Tavaline käe/rusika löök -", karakter1.l66k)
    print("Mõõga löök -", karakter1.m66k)
    print("Mõttejõu tugevus -", karakter1.m6ttej6ud)
    
#Võitlus
    vaenlane1 = goblin
    print("\nVaenlane nimega", vaenlane1, "tahab suga kakelda")
    print("Goblini statistika: ")
    print("Elusi on: ", vaenlane1.elud1)
    print("DMGi on: ", vaenlane1.dmg1)
    print("Viskamine: ", vaenlane1.viskamine)
    print("Peale hüppamine: ", vaenlane1.hyppamine)
    while vaenlane1.elud1 > 0 :
        print("\nValige number 1-4, et valida millist ründamismeetodit te tahate kasutada.")
        valik = input("1. Löö rusikaga\n2. Löö jalaga\n3. Löö mõõgaga\n4. Tagane\n5. Kasuta mõttejõudu (ohtlik)")
        if valik == "1":
            chance = random.randint(0,10)
            if chance > 3:
                vaenlane1.elud1 = vaenlane1.elud1 - karakter1.l66k
                print("Lõid goblinit rusikaga näkku")
                print("Goblini elud on nüüd: ", vaenlane1.elud1)
                print("Saate goblinit uuesti lüüa, kuna ta on uimane!")
            else:
                print("Lõid goblinist rusikaga mööda")
                print("Goblini elud on ikka: ", vaenlane1.elud1)
                if vaenlane1.elud1 > 0:
                    karakter1.elud = karakter1.elud - vaenlane1.dmg1
                    print("Goblin lõi sind vastu tatti ja sul on järel", karakter1.elud,"elu")
        if valik == "2":
            chance = random.randint(0,10)
            if chance > 3:
                vaenlane1.elud1 = vaenlane1.elud1 - karakter1.l66k
                print("Lõid goblinile jalaga näkku")
                print("Goblini elud on nüüd: ", vaenlane1.elud1)
                print("Saate goblinit uuesti lüüa, kuna ta on uimane!")
            else:
                print("Lõid goblinist jalaga mööda")
                print("Goblini elud on ikka: ", vaenlane1.elud1)
                if vaenlane1.elud1 > 0:
                    karakter1.elud = karakter1.elud - vaenlane1.dmg1
        if valik == "3":
            chance = random.randint(0,5)
            if chance > 3:
                vaenlane1.elud1 = vaenlane1.elud1 - karakter1.m66k
                print("Torkasid goblinit mõõgaga")
                print("Goblini elud on nüüd: ", vaenlane1.elud1)
                print("Saate goblinit uuesti lüüa, kuna ta on uimane!")
            else:
                print("Lõid goblinist mõõgaga mööda")
                print("Goblini elud on ikka: ", vaenlane1.elud1)
                if vaenlane1.elud1 > 0:
                    karakter1.elud = karakter1.elud - vaenlane1.viskamine
                    print("Goblin viskas sind kuldmüntidega")
                    print("Sul on järel", karakter1.elud,"elu")
        if valik == "4":
            chance = random.randint(0,10)
            if chance > 3:
                print("\nSa üritasid taganeda, aga kari goblineid hüppasid su peale ja sa surid ära.")
                karakter1.elud = karakter1.elud - vaenlane1.hyppamine
                print("Sul on järel: ", karakter1.elud, "elu")
                exit()
            else:
                print("\nSa põgenesid ära goblinite küüsist!")
                exit()
        if valik == "5":
            chance = random.randint(0,5)
            if chance > 3:
                vaenlane1.elud1 = vaenlane1.elud1 - karakter1.m6ttej6ud
                print("\nKontrollisid goblini mõtteid ja lasid tal peaga vastu seina peksta.")
                print("Sa kõndisid rahulikult kulla poole goblini verd täis ja said aru, et see oli plastmass kuld.")
                exit()
            else:
                print("\nGoblini sõbrad hüppasid sulle peale ja tapsid su silmapilkselt.")
                exit()
                
        if karakter1.elud < 1:
            print("Sa surid ära")
            print("\nGoblin tantsib su peal ja sülitab sulle vastu nägu naerdes")
            exit()
        if  vaenlane1.elud1 <1:
            print("Sa tapsid ära goblini")
            print("\nSa kõndisid rahulikult kulla poole goblini verd täis ja said aru, et see oli plastmass kuld.")
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
            "Teie DMG: ": l66k,
            "Teie Mööga löök: ": m66k,
            "Teie Mõttejõu tugevus: ": m6ttej6ud}
        f.write(str(dict))
        f.close()
        
saving()