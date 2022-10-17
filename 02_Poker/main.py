import random


# a = 14 % 13
# print(a)

def kartenAusteilen(anzahl):
    karten = []
    for i in range(5):
        karten.append(ziehung(karten))
    return karten

def ziehung(karten):
    rand = random.randint(0,51)
    if(not rand in karten):
        return rand
    else:
        return ziehung(karten)


def paarVorhanden(karten):
    paar = []
    for i in karten:
        card = i%13
        if(card in paar):
            print("PAAR " + str(card))
        paar.append(card)
    print(paar)

def flushVorhanden(karten):
    flush = []
    vorherigeFarbe = -1
    for i in karten:
        card = int(i/13)
        if(len(flush)  == 0): vorherigeFarbe = card
        if(not vorherigeFarbe == card): 
            print("no flush")
            return False
        else:
            flush.append(card)
    print(flush)
    print("Flush")
    return True


hand = kartenAusteilen(5)
print(hand)
paarVorhanden(hand)


# a = False
# i = 0
# while(a == False):
#     hand = kartenAusteilen(5)
#     print(hand)
#     #paarVorhanden(hand)
#     a = flushVorhanden(hand)
#     i +=1
# print(i)