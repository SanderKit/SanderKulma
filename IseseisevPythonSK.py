#Sander Kulma IT20b
#12.14.2020
#Iseseisev Python
#Ülesannete järjekord läheb alt ülesse

#Ülesanne 9
#Koosta programm, mis joonistab tsüklite abil samasugused kolmnurgad
# A)
rows = 5
for i in range(0, rows):
    for j in range(0, i + 1):
        print("*", end=' ')
    print("\r")

for i in range(rows, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print("\r")

input()
# B)
rows = 5
for i in range(rows + 1, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print(" ")

input()
# C)
rows = 5
for i in range(0, rows):
    for j in range(0, i + 1):
        print("*", end=' ')

    print("\r")

input()

#Ülesanne 9
#Kirjuta programm, mis väljastab arvud 1-66 reana
for i in range (1, 60):
    print(i, end="")

input()
#Ülesanne 8
#Kirjuta programm, mis muudab lause tagurpidiseks
lause = "Ma armastan Javat"
s6na = lause.split()
tagurpidi = s6na[:: -1]
tagurpidi = " ".join(tagurpidi)

print(tagurpidi)

input()
#Ülesanne 4
#Väljasta samasugune "Eesti lipp"
print("¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤")
print("¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤")
print("¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤")
print("==============================================")
print("==============================================")
print("==============================================")
print("----------------------------------------------")
print("----------------------------------------------")
print("----------------------------------------------")

input()
#Ülesanne 1
#Küsi kasutajalt kahte arvu ning väljasta liitmise vastus
arv = int(input("Pange sisse esimene number: "))
arv2 = int(input("Pange sisse teine number: "))
arvv = input("Kirjuta pluss märk: ")

result = 0
if arvv == "+":
    result = arv + arv2
    
print(arv, "+", arv2, "=", result)