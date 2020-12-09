#Sander Kulma IT20
#02.12.2020
#Ülesanne06

#Faili avamine
minu_fail = open('s6pru_l6ustaraamatus.txt', 'r')
ref = 0
ke = 0
erakondi_kokku = []
#Faili sisu kuvamine
faili_sisu = minu_fail.readlines()
for i in range(len(faili_sisu)):
    #print(faili_sisu[i], end="")
    enimi, pnimi, ek, s = faili_sisu[i].split(" ")
    print(f"{enimi:11}{pnimi:11}{ek:4}{s:5}", end="")
    if ek == "RE":
        ref+=1
    if ek == "KE":
        ke+=1
    if ek not in erakondi_kokku:
        erakondi_kokku.append(ek)

#faili kirjutamine
with open('poliitikud.txt','a') as fail_kirjutamiseks:
    for nr in range(1,100):
         fail_kirjutamiseks.write(enimi+" "+pnimi+"\n")

print("\nReformikaid kokku:", ref)
print("Kesikuid kokku:", ke)
print("Erakondi kokku:", len(erakondi_kokku))
    
#faili sulgemine
minu_fail.close