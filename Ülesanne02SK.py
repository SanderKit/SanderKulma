#Sander Kulma IT20
#24.11.2020
#Ülesanne 2

import math

# Kolmnurga ümbermõõt
a = 2
b = 3
c = 4

p=a+b+c
print("Kolmnurga ümbermõõt = ",p )

# Toote hind
hind = 36.75
ale = 0.4
kogus = 3
summa = (hind-(hind*ale))*kogus
print("Summa: ", summa)

# Pitsa
hind = 12.9
tip = 1.1
sõbrad = 3
maksmine = (hind*tip)/sõbrad
print("Igaüks peab maksma: ", maksmine)

# Rulluisutajad
Kiirus = 29.9
aeg = (24/60)
dist = Kiirus * aeg
print("Kaugus: ",dist,"km")

# Kolmnurga hüpotenuus
import math
a,b = 16,9
c= math.sqrt(a**2 + b**2)
print("Kolmnurga hypotenuus: ",c)

#Aja teisendus
aeg = int(input("Sisesta aeg minutites: "))
h = aeg//60
v = "/€"
m = aeg%60
p = "Pole oluline muutuja"
print(aeg,"minutit on",h,":",m)

#Arvusüsteemid
arv = int(input("Kasutaja sisestab kymnendsysteemis: "))
kahend = bin(arv)
kuusteist = hex(arv)
print("kahendsysteem arv: ",kahend)
print("kuusteistsysteem arv: ",kuusteist)

#Kütusekulu arvutamine
liiter = int(input("Kasutaja sisestab tangitud kytuse liitrid: "))
kilomeeter = int(input("Kasutaja sisestab l2bitud kilomeetrid: "))
kutus = liitrid / (km//100)
print("Kütusekulu 100km'le: ",kutus)






