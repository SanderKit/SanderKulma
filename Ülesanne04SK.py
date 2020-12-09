#Sander Kulma IT20
#25.11.2020
#Ülesanne04

print("*******MMPANK*******")
konto = 10000
aeg = 5
intress = 0.05
alg = konto

print("Aasta \t Algsumma \t Intress \t Aasta lõpuks")
for i in range(aeg):
    algsumma = konto
    konto = konto+konto*intress
    print(f"{i+1} \t {algsumma: .2f} \t {algsumma*intress: .2f} \t {konto: .2f}")
kasum = konto-alg

print(f"Summa kokku: {kasum}")
print(f"Kasum: {alg}")

#Prindi ruutude ja kuupide tabel
for i in range(1,11):
    for j in range(1,11):
        print('{0:>3}'.format(j*i), end=" ")
    print()









#Mäng
import random

print("********* GUESS **********")

loop = 0
suv = random.randint(1,5)

while loop<3:
    arva = int(input("Arva arv 1-5: "))
    if suv==arva:
        print("Võitsid")
        valik = input("Kas sa soovid veel m2ngida jah/ei: ")
        if valik=="jah":
            loop = 0
            suv = random.randint(1,5)
        else:
            loop = 100
    else:
        print("Proovi uuesti")
    loop = loop + 1
    
print("Said kotti")
input()

    

#----------- FOR -----------
#viisikud
for i in range(1,101):
    if i%5==0:
        print(i, end=" ")
print()

#korrutustabel
for i in range(1,11):
    print(f"5 x {i}={5*i}")
input()

#paaris ja paaritus 1-10
for i in range(1,11):
    if i%2==0:
        print(f"{1} paaris")
        print(i, "paaris")
    else:
        print(f"{i} paaritu")

#Loto
    print("Tänased HKHK-LOTO tulemused on: ")
for i in range(5):
    suv = random.randint(0,9)
    print(suv, end="")

input()

#Tärnid
for i in range(1,26):
    print("*", end="")
    if i%5==0:
        print("", end="\n")
#Tärnidest kasvav kolmnurk
for i in range(1,6):
    print("*"*i)
  
j = 6
for i in range(1,j):
   print((j-i)*"*")

#----------- IF ------------

#Külg
kylg = input("Sisesta ruudu yks kylg: ")
kylg2 = input("Sisesta ruudu teine kylg: ")
# = võrdub
# == on võrdne
if kylg==kylg2:
    print("Tegemist on ruuduga")
else:
    print("Ei ole ruut")

#Matemaatika
mat1 = int(input("Sisesta arv 1: "))
mat2 = int(input("Sisesta arv 2: "))
tehe = input("Sisesta tehe + - * / : ")
if tehe=="+":
    print(f"{mat1}+{mat2}={mat1+mat2}")
elif tehe=="-":
    print(f"{mat1}-{mat2}={mat1-mat2}")
elif tehe=="/":
    print(f"{mat1}/{mat2}={mat1/mat2}")
else:
    print(f"{mat1}*{mat2}={mat1*mat2}")
    
#Juubel
aasta = 2003
vanus = 2020-aasta
if vanus%5==0:
    print("Juubel")
else:
    print("Ei ole juubel")
    
#Müük
müük = int(input("Sisesta toote hind: "))
if 0.1 <= 10:
    print("Allahindlus on 10%")
else:
    print("Allahindlust pole")

#Jalgpalli meeskond
sugu = input("Sisesta sugu: ")
vanus = int(input("Sisesta vanus: "))
if vanus >= 16 and vanus <= 18 and sugu=="mees":
    print("Sobib meeskonda")
else:
    print("Ei sobi")


    

    
