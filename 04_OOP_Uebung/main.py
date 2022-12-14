from enum import Enum

class Sex(Enum):
    male = 0
    femal = 1
    notSpecified = 2

class AbteilungName(Enum):
    Verwaltung = 0
    IT = 1
    Management = 2

class Person:
    def __init__(self, Vorname, Nachname, Sex):
        self.Vorname = Vorname
        self.Nachname = Nachname
        self.Sex = Sex

    def __str__(self):
        return f'Person name is {self.Vorname} {self.Nachname} sex is {self.Sex}'

class Mitarbeiter(Person):
    def __init__(self, Vorname, Nachname, Sex, Gehalt):
        super().__init__(Vorname, Nachname, Sex)
        self.Gehalt = Gehalt
    
    def __str__(self): 
        return super().__str__() + f' Abteilung {self.Gehalt}'


class Gruppenleiter(Mitarbeiter):
    def __init__(self, Vorname, Nachname, Sex, Gehalt, AbteilungsName):
        super().__init__(Vorname, Nachname, Sex, Gehalt)
        self.AbteilungsName = AbteilungsName
    
    def __str__(self): 
        return super().__str__() + f' Abteilung {self.AbteilungsName}'


class Abteilung:
    def __init__(self,nameAbteilung, Gruppenleiter, Mitarbeiter = []):
        self.nameAbteilung = nameAbteilung
        self.Gruppenleiter = Gruppenleiter
        self.Mitarbeiter = Mitarbeiter
    
    def count_MA(self):
        return len(self.Mitarbeiter)


class Firma:
    def __init__(self, name, abteilungen = []):
        self.name = name
        self.abteilungen = abteilungen
    
    def count_CompMA(self):
        cnt = 0
        for a in self.abteilungen:
            cnt += int(a.count_MA())
        return cnt

    def allAbt(self):
        cnt = 0
        for a in self.abteilungen:
            cnt += 1
            print(a.nameAbteilung)
        return cnt

    def count_Dep(self):
        return len(self.abteilungen)

    def count_GL(self):
        cnt = 0
        for a in self.abteilungen:
            for g in a.Gruppenleiter:
                cnt += 1
        return cnt

    def biggest_Dep(self):
        biggest = 0
        abt = []
        for a in self.abteilungen:
            if a.count_MA() > biggest:
                abt = [] 
                abt.append(a.nameAbteilung)
                biggest = a.count_MA()
            elif a.count_MA() == biggest:
                abt.append(a.nameAbteilung)
        return abt,biggest
    
    def proportionMaleFemal(self):
        male = 0
        female = 0
        for a in self.abteilungen:
            for m in a.Mitarbeiter:
                if m.Sex == Sex.male: male += 1
                else: female += 1
        return male, female

    # def portion_Male_Female(self):
    #     for a in self.abteilungen:
    #         for m in a.Mitarbeiter






p = Person("Clemens","Rietzler", Sex.male)
p2 = Person("Clemens2","Rietzler2", Sex.male)


g = Gruppenleiter(p.Vorname,p.Nachname,p.Sex,1000, AbteilungName.IT)
m = Mitarbeiter(p2.Vorname,p2.Nachname,p2.Sex,1000)
m1 = Mitarbeiter(p.Vorname,p.Nachname,p.Sex,1000)

a = Abteilung("IT", [g],[m,m1])
print(a.count_MA())
a1 = Abteilung("Mg", [g],[m,m1])

f = Firma("HTL", [a,a1])
print(f.count_Dep())
print(f.allAbt())
print(f.count_CompMA())
print(f.biggest_Dep())
print(f.proportionMaleFemal())
print(f.count_GL())
#print(f.count_Dep())