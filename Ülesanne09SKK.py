#Ülesanne09
#Isikukodist kuupäeva leidmine

ik = input("Sisesta isikukood: ")

# 38011064711
if len(ik) == 11:
    p = ik[6:7]
    k = ik[4:5]
    a = ik[1:3]
    print(f"{p}.{k}.{a}")