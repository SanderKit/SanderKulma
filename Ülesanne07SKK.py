#Sander Kulma IT20
#02.12.2020
#Ülesanne07SK

#Ruumala

def kuup():
    x = int(input("Kõrgus: "))
    y = int(input("Laius: "))
    z = int(input("Pikkus: "))
    v = x * y * z
    return v

def kera():
    a = int(input("Sisesta diameeter: "))
    pii = 3.14
    v = pii * d * d
    return "Kera leidmine"

def koonus():

    return "Koonuse leidmine"

def silinder():
    return "Silindri leidmine"

def ruumalad():
    loop = 1
    while loop==1:
        print("Tee valik")
        print("1. Kuup")
        print("2. Kera")
        print("3. Koonus")
        print("4. Silinder")
        print()
        valik = int(input("Tee valik 1-4: "))
        if valik==1:
            print(f"Kuubi ruumala on {kuup()}")
        elif valik==2:
            print(f"Kera diameeter on {kera()}")
        elif valik==3:
            
            

ruumalad()

#Tervitab
def tervita(keel="de"):
    keel = input("Vali keel eng/est/ger: ")
    if keel =="est":
        nimi = input("Sisesta nimi, keda tahad tervitada: ")
        return "Tere, "+nimi
    elif keel=="eng":
        nimi = input("Insert a name, who you want to say hi to: ")
        return "Hi, "+nimi
    else:
        nimi = input("Geben Sie den Namen ein, den Sie begrüßen möchten: ")
        return "Hallo, "+nimi

        
print(tervita("est"))

