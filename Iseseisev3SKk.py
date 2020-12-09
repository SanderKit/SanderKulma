#Iseseisvad tööd 3
#Sander Kulma IT20b

#kuup2ev
kuup2ev = input("Sisestage kuup2ev DD.MM.YYYY: ")
def kuu_nimi(i):
    p,k,a = i.split(".")
    kuud = ('jaanuar', 'veebruar', 'märts', 'aprill', 'mai', 'juuni', 'juuli', 'august', 'september', 'oktoober', 'november', 'detsember')
    k = int(k)
    return kuud[k-1]
def kuup2ev_s6nena(i):
    p,k,a = i.split(".")
    return p+". "+kuu_nimi(i)+" "+a+". a"

print(kuup2ev_s6nena(kuup2ev))

input()
#Tervitused
fail = open("myndid.txt")
rida = fail.readlines()

print(rida,end="")
def pronskikarva_summa(m):
    kassa = 0
    for i in range(len(m)):
        if int(m[i]) < 10:
            kassa+=int(m[i])
    print("Kassase läheb",kassa,"senti.")
pronksikarva_summa(rida)


input()
#Eelarve
# def eelarve(k):
#     summa = k*10+55
#     return summa
# kutsub = int(input("Kui palju inim kutsuti?: "))
# kutsub2 = int(input("Kes on teatanud tulemisest?. "))
# 
# print("Maksimaalne eelarve:", eelarve(kutsub),"eurot")
# print("Minimaalne eelarve:", eelarve(kutsub2),"eurot")
# 
# #õun
# ounad = int(input("Kui palju tahad 6unu?: "))
# def mahlapakkide_arv():
#     mpa = round(ounad*0,4/3,0)
#     mpa = int(mpa)
#     return mpa
# print(mahlapakkide_arv(ounad))
# 
# 
# input()
# #Tahvli juurde
# fail = open("failid/nimekiri.txt","r")
# rida = fail.readlines()
# from datetime import *

# print(f"Vastama tuleb: {rida[datetime.now().day-1]}")

#jukebox
# kys = input("Millist faili te tahate?")
# fail = open("failid/"+kys+".txt","r")
# read = fail.readlines()
# for n in range(len(read))
#     print(str(n+1)+". "+read[n],end="")
# kyss = int(input("\n \n Millist laulu te soovite?: "))
# print(read[kyss-1])




#Sissetulekud
# fail = open("failid/konto.txt","r")
# loeb = fail.readlines()
# for n in range(len(loeb)):
#     print(float(loeb[n]))
#     if float(loeb[n]) > 0:
#         print(loeb[n],end="")