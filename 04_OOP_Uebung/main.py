from enum import Enum

class Sex(Enum):
    male = 0
    female = 1
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
    def __init__(self,nameAbteilung, Gruppenleiter = [], Mitarbeiter = []):
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
        dep = []
        for a in self.abteilungen:
            dep.append(a.nameAbteilung)
        return dep

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
        nenner = male+female
        male = male/nenner*100
        female = female/nenner*100
        return male, female

    def salariers(self):
        sum = 0
        for a in self.abteilungen:
            for m in a.Mitarbeiter:
                sum += m.Gehalt
            for g in a.Gruppenleiter:
                sum += g.Gehalt
        return sum

if __name__ == '__main__':
    p = Person("Clemens","Rietzler", Sex.male)
    p2 = Person("Clemens2","Rietzler2", Sex.female)
    p3 = Person("Clemens3","Rietzler3", Sex.female)


    g = Gruppenleiter(p.Vorname,p.Nachname,p.Sex,1000, AbteilungName.IT)
    g2 = Gruppenleiter(p.Vorname,p.Nachname,p.Sex,3000, AbteilungName.Management)
    m = Mitarbeiter(p2.Vorname,p2.Nachname,p2.Sex,1000)
    m1 = Mitarbeiter(p.Vorname,p.Nachname,p.Sex,1000)
    m2 = Mitarbeiter(p3.Vorname,p3.Nachname,p3.Sex,80000)
    m3 = Mitarbeiter(p3.Vorname,p3.Nachname,p3.Sex,100)
    m4 = Mitarbeiter(p3.Vorname,p3.Nachname,p3.Sex,200)

    a = Abteilung("IT", [g],[m,m1,m2])
    print("Mitarbeiter in Abteilung ",a.nameAbteilung,a.count_MA())
    a1 = Abteilung("Mg", [g2],[m3,m4])

    f = Firma("HTL", [a,a1])
    print("Anzahl Abteilungen ",f.count_Dep())
    print("Mitarbeiter in Frima ", f.count_CompMA())
    print("Größte Abteilung/en, mit Mitarbeiteranzahl ",f.biggest_Dep())
    print("Verhältniss Male-Female ",f.proportionMaleFemal())
    print("Anzahl Gruppenleiter in der Firma ",f.count_GL())
    print("Abteilungen ",f.allAbt())
    print("Auszuzahlende Gehälter pro Monat ",f.salariers())
