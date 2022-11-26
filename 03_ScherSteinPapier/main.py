import random
import ast

choices = ["Schere","Stein", "Papier", "Echse","Spock"]

playerWins = 0
playerStatSymbols = {"Schere" : 0,"Stein": 0, "Papier": 0, "Echse": 0,"Spock": 0}
compWins = 0

def player_select():
    print("Auswählen zwischen "+ str(choices))
    choice = input()
    if(choice in choices):
        playerStatSymbols[choice] = playerStatSymbols[choice] + 1
        return choice
    else:
        print("Falsche Eingabe, nochmal!")
        player_select()

def comp_selcet():
    return choices[random.randint(0,4)]

def analysis(comp, player):
    global compWins, playerWins
    if(player == "Schere" and (comp == "Papier" or comp=="Echse")):
        print("Player won")
        playerWins = playerWins + 1
    elif(player == "Spock" and (comp == "Schere" or comp=="Stein")):
        print("Player won")
        playerWins = playerWins + 1
    elif(player == "Echse" and (comp == "Spcok" or comp=="Papier")):
        print("Player won")
        playerWins = playerWins + 1
    elif(player == "Stein" and (comp == "Schere" or comp=="Echse")):
        print("Player won")
        playerWins = playerWins + 1
    elif(player == "Papier" and (comp == "Stein" or comp=="Spock")):
        print("Player won")
        playerWins = playerWins + 1
    elif(player == comp):
        print("equal, try it again")
    else:
        print("PC won")
        compWins = compWins + 1

def game():
    loadDataFromStorage()

    player = player_select()
    comp = comp_selcet()
    print(comp)
    analysis(comp,player)
    print("Player: " + str(playerWins) + " Comp: " + str(compWins))
    print(playerStatSymbols)

    saveDataToStorage()


def loadDataFromStorage():
    global playerWins, compWins,playerStatSymbols
    datei = open(r'C:\Users\Clemens\Dokumente\Schule\HTL\5.Klasse\SWP-python\SWP-Python-Rubner\03_ScherSteinPapier\db.txt','r')
    playerWins = int(datei.readline().split(' ')[1])
    compWins = int(datei.readline().split(' ')[1])
    playerStatSymbols = ast.literal_eval(str(datei.readline()))
    datei.close()


def saveDataToStorage():
    data = "PlayerWins " + str(playerWins) + "\nCompWins " + str(compWins) + "\n" + str(playerStatSymbols)
    #print(data)
    with open(r'C:\Users\Clemens\Dokumente\Schule\HTL\5.Klasse\SWP-python\SWP-Python-Rubner\03_ScherSteinPapier\db.txt','w') as db:
        db.write(data)
        db.close()


#TODO Alle gewähten Sympole, auch von PC???

if __name__ == '__main__':

    while(True):
        game()
