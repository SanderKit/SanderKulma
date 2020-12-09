#Harjutus08
#09.12.2020
#Sander Kulma IT20b

class Auto:
    automark = 'puudub'
    aasta = 0
    hind = 0

    def __init__(self,x,y,z):
        self.automark = x
        self.aasta = y
        self.hind = z

    def lisaMark(self, x):
        self.mark = x
        
    def lisaAasta(self, x):
        self.aasta = x
        
     def lisaHind(self, x):
        self.hind = x
        
    def kuva(self):
        print(f"Automark: {self.automark} \nAasta{self.aasta} \nHind: {self.hind}")
        
minuaAuto = Auto("BMW E46", 2000, 5000)
minuAuto.kuva()