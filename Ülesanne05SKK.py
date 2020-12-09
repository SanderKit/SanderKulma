#SK IT20
#26.11.2020
#Ülesanne 5

#Tärnid
vanused = [15,31,54,54,98,63,14,2,34]
for i in range(len(vanused)):
    print(vanused[i]*"*")


#Arvud loendis
vanused = [15,31,54,54,98,63,14,2,34]
print(f"Suurim arv: {max(vanused)}")
print(f"Väikseim: {min(vanused)}")
print(f"Summa: {sum(vanused)}")
print(f"Keskmine: {round(sum(vanused)/len(vanused),2)}")

input()
#Duplikaadid
opilased = ['Juhan','Mario','Maarja','Mario','Mati','Mati','Sander']
uus_nimekiri = []
#Valib kõik õpilased 1 haaval
for i in range(len(opilased)):
    #Kui õpilast nimekirjas pole, siis lisatakse
    if opilased[i] not in uus_nimekiri:
        uus_nimekiri.append(opilased[i])

for i in uus_nimekiri:
    print(i)

input()
#Õpilased
opilased = ['Juhan','Kati','Maarja','Mario','Mati']
print("Vana nimekiri")
for i in range(len(opilased)):
    print(f"{i+1}. {opilased[i]}")
arv = int(input("Mitmendat sa tahad muuta? "))
print(f"Valisid: {opilased[arv-1]}")
del opilased[arv-1]
print(opilased)
#Asendus
uus_nimi = input("Pane uus nimi: ")
opilased.insert(arv-1,uus_nimi)
#Kuva nimekiri
print("Uus nimekiri")
for i in range(len(opilased)):
    print(f"{i+1}. {opilased[i]}")
    
input()
#Nimede lisamine loendisse
nimed = []

for i in range(5):
    nimi = input("Sisesta nimi: ")
    nimed.append(nimi)

nimed.sort()
print(nimed)
print("Viimati lisatud nimi: ",nimi)
    