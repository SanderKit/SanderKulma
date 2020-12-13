arv = int(input("Pange sisse esimene number: "))
arv2 = int(input("Pange sisse teine number: "))
arvv = input("Kirjuta pluss märk: ")

result = 0
if arvv == "+":
    result = arv + arv2
    
print(arv, "+", arv2, "=", result)