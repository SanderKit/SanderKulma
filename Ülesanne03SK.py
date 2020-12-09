#Sander Kulma IT20
#24.11.2020
#Ülesanne 03

#Nime sisestamine
nimi = input("Mis on teie nimi: ")
nimi = nimi.strip()
nimi = nimi.capitalize()
print(f"Tere {nimi}!")

#Vandumine

vandumine = input("Sisesta vanne: ")
print(vandumine.replace('Kuradi' ,'******'))


#Email
email = input("Sisesta email: ")
print("@" in email)

#Tundide ajad
algus = input("Sisesta algusaeg (hh:mm): ")
lopp = input("Sisesta lõppaeg (hh:mm): ")
hh1, mm1 = algus.split(":")
hh2, mm2 = lopp.split(":")
aeg1 = int(hh1) * 60 + int(mm1)
aeg2 = int(hh2) * 60 + int(mm2)
vahe = aeg2-aeg1
h = vahe // 60
m = vahe % 60
print(f"Päeva pikkus on {h}:{m}")

#Palindroom
sona = input("Sisesta palindroom: ")
print(sona == sona[::-1])

