import random

class Charakter:
    def __init__(self, name, hp, angriff, verteidigung):
        self.name = name
        self.hp = hp
        self.angriff = angriff
        self.verteidigung = verteidigung
        self.level = 1
        self.erfahrung = 0

    def schadenNehmen(self, schaden):
        self.hp -= schaden

    def istAmLeben(self):
        return self.hp > 0

    def levelAufstieg(self):
        self.level += 1
        self.angriff += 2
        self.verteidigung += 1
        self.hp += 10
        print(f"{self.name} ist auf Level {self.level} aufgestiegen!")
        print(f"+2 Angriff! +1 Verteidigung! +10 HP!")
        print(f"Welchen Stat möchtest du erhöhen?")
        print("1. Angriff +3")
        print("2. Verteidigung + 2")
        print("3. HP + 10")
        auswahl = input("Wähle einen Stat: ")

        if auswahl == "1":
            self.angriff += 3
        if auswahl == "2":
            self.verteidigung += 2
        if auswahl == "3":
            self.hp += 10

    def erfahrungSammeln(self, erfahrung):
        self.erfahrung += erfahrung
        print(f"{self.name} hat {erfahrung} Erfahrungspunkte gesammelt!")
        if self.erfahrung >= self.level * 10:
            self.levelAufstieg()
            self.erfahrung = 0

    def gegnerAngreifen(self, gegner):
        schaden = max(0, self.angriff - gegner.verteidigung)
        gegner.schadenNehmen(schaden)
        print(f"{self.name} hat angegriffen und {gegner.name} {schaden} Schaden verursacht!")

class Gegner(Charakter):
    def __init__(self, name, hp, angriff, verteidigung):
        super().__init__(name, hp, angriff, verteidigung)

def kampf(spieler, gegner):
    print(f"Ein {gegner.name} ist aufgetaucht!\n")
    while spieler.istAmLeben() and gegner.istAmLeben():
        print(f"{spieler.name}: HP={spieler.hp} | {gegner.name}: HP={gegner.hp}")
        print("1. Angreifen")
        print("2. Fliehen")
        auswahl = input("Wähle eine Aktion: ")
        
        if auswahl == "1":
            spieler.gegnerAngreifen(gegner)
            if gegner.istAmLeben():
                gegner.gegnerAngreifen(spieler)
        elif auswahl == "2":
            print(f"{spieler.name} ist geflohen!")
            return False

    if spieler.istAmLeben():
        spieler.erfahrungSammeln(5)
        print(f"{spieler.name} hat {gegner.name} besiegt!\n")
        return True
    else:
        print(f"{spieler.name} wurde von {gegner.name} besiegt...\n")
        return False

def hauptprogramm():
    spielerName = input("Gib den Namen deines Charakters ein: ")
    spieler = Charakter(spielerName, hp=30, angriff=8, verteidigung=5)
    
    while True:
        gegnerName = random.choice(["Zombie", "Skelett", "Schleim", "Spinne"])
        gegner = Gegner(gegnerName, hp=20 + spieler.level, angriff=6 + spieler.level, verteidigung=3 + spieler.level)
        
        if not kampf(spieler, gegner):
            break

if __name__ == "__main__":
    hauptprogramm()
