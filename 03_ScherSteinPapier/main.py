import random
import ast
from flask import Flask, request
import requests # for rest calls

host = 'http://localhost:5000/stats'

choices = ["Schere","Stein", "Papier", "Echse","Spock"]

name_score = {}


def player_select(playerStatSymbols):
    print("Auswählen zwischen "+ str(choices))
    choice = input()
    if(choice in choices):
        playerStatSymbols[choice] = playerStatSymbols[choice] + 1
        return choice
    else:
        print("Falsche Eingabe, nochmal!")
        player_select(playerStatSymbols)

def comp_selcet():
    return choices[random.randint(0,4)]

def comp_selectWithAnalyse(playerStatSymbols):
    listSorted = sorted(playerStatSymbols.items(), key=lambda x:x[1], reverse=True)
    dicSorted = dict(sorted(playerStatSymbols.items(), key=lambda x:x[1], reverse=True))
    most = listSorted[0][0]
    if most == "Schere" and dicSorted['Stein'] > dicSorted['Spock']: return "Spock"
    elif most == "Schere" and dicSorted['Spock'] > dicSorted['Stein']: return "Stein"
    elif most == "Papier" and dicSorted['Schere'] > dicSorted['Echse']: return "Echse"
    elif most == "Papier" and dicSorted['Echse'] > dicSorted['Schere']: return "Schere"
    elif most == "Stein" and dicSorted['Papier'] > dicSorted['Spock']: return "Spock"
    elif most == "Stein" and dicSorted['Spock'] > dicSorted['Papier']: return "Papier"   
    elif most == "Echse" and dicSorted['Stein'] > dicSorted['Schere']: return "Schere"
    elif most == "Echse" and dicSorted['Schere'] > dicSorted['Stein']: return "Stein"
    elif most == "Spock" and dicSorted['Echse'] > dicSorted['Papier']: return "Papier"
    elif most == "Spock" and dicSorted['Papier'] > dicSorted['Echse']: return "Echse"
    else: return choices[random.randint(0,4)]


def analysis(comp, player, playerWins, compWins,playerStatSymbols):
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
    return (playerWins, compWins,playerStatSymbols)


def game(runden, playerWins, compWins,playerStatSymbols):
    for i in range(0,runden):
        player = player_select(playerStatSymbols)
        comp = comp_selcet()
        print(comp)
        (playerWins, compWins,playerStatSymbols) = analysis(comp,player, playerWins, compWins,playerStatSymbols)
        print("Player: " + str(playerWins) + ", Comp: " + str(compWins))
        print(playerStatSymbols)
    return (playerWins, compWins,playerStatSymbols)

def gameWithAnalyse(runden, playerWins, compWins,playerStatSymbols):
    for i in range(0,runden):
        player = player_select(playerStatSymbols)
        comp = comp_selectWithAnalyse(playerStatSymbols)
        print(comp)
        (playerWins, compWins,playerStatSymbols) = analysis(comp, player, playerWins, compWins,playerStatSymbols)
        print("Player: " + str(playerWins) + ", Comp: " + str(compWins))
        print(playerStatSymbols)


def loadDataFromStorage(doc = '\db.txt'):
    datei = open(r'C:\Users\Clemens\Dokumente\Schule\HTL\5.Klasse\SWP-python\SWP-Python-Rubner\03_ScherSteinPapier' + doc,'r')
    data = ast.literal_eval(str(datei.read()))
    playerWins = data['PlayerWins']
    compWins = data['CompWins']
    playerStatSymbols = data['stats']
    datei.close()
    return (playerWins, compWins,playerStatSymbols)


def saveDataToStorage(playerWins, compWins,playerStatSymbols, doc = '\db.txt'):
    data = {
    "PlayerWins": playerWins,
    "CompWins": compWins,
    "stats":playerStatSymbols
    }
    with open(r'C:\Users\Clemens\Dokumente\Schule\HTL\5.Klasse\SWP-python\SWP-Python-Rubner\03_ScherSteinPapier'+ doc,'w') as db:
        db.write(str(data))
        db.close()

def saveDataToAPI(playerWins, compWins,playerStatSymbols, user='user'):
    j = {"playerWins":playerWins, "compWins":compWins, "stats":{'Schere': playerStatSymbols['Schere'], 'Stein': playerStatSymbols['Stein'], 'Papier': playerStatSymbols['Papier'], 'Echse': playerStatSymbols['Echse'], 'Spock': playerStatSymbols['Spock']}}
    response = requests.put('%s/%s' % (host, user) , json=j)
    print (response) #Gibt den Response Code aus (Header)
    print(response.json()) #Gibt den Response Body aus (also die wirkliche Antwort)

def loadDataFromAPI(user='user'):
    response = requests.get('%s/%s' % (host, user)).json()
    print (response)

def changeDataOnAPI(playerWins, compWins,playerStatSymbols, user='user'):
    j = {"playerWins":playerWins, "compWins":compWins, "stats":{'Schere': playerStatSymbols['Schere'], 'Stein': playerStatSymbols['Stein'], 'Papier': playerStatSymbols['Papier'], 'Echse': playerStatSymbols['Echse'], 'Spock': playerStatSymbols['Spock']}}
    response = requests.patch('%s/%s' % (host, user),  json=j).json()
    print (response)


def consolenMenue(playerWins, compWins,playerStatSymbols):
    print("[spielen, statistik, daten uploaden, spiel mit analyse, daten neu auf api, daten von api, daten update api]")
    inp = input()
    if(inp == 'spielen'):
        print("Anzahl versuche:")
        inp2 = int(input())
        playerWins, compWins,playerStatSymbols = game(inp2, playerWins, compWins,playerStatSymbols)
    elif(inp == 'statistik'):
        playerWins, compWins,playerStatSymbols = loadDataFromStorage()
        print("playerWins",playerWins)
        print("compWins",compWins)
        print(playerStatSymbols)
    elif(inp == 'daten uploaden'):
        saveDataToStorage(playerWins, compWins,playerStatSymbols)
    elif(inp == 'spiel mit analyse'):
        print("Anzahl versuche:")
        inp2 = int(input())
        playerWins, compWins,playerStatSymbols = loadDataFromStorage()
        gameWithAnalyse(inp2, playerWins, compWins,playerStatSymbols) 
    elif(inp == 'daten neu auf api'):
        saveDataToAPI(playerWins, compWins,playerStatSymbols)
    elif(inp == 'daten von api'):
        loadDataFromAPI()
    elif(inp == 'daten update api'):
        changeDataOnAPI(playerWins, compWins,playerStatSymbols)
    else:
        print("Falsche eingabe, erneut")
        consolenMenue(playerWins, compWins,playerStatSymbols)

if __name__ == '__main__':
    (playerWins, compWins,playerStatSymbols) = loadDataFromStorage()
    while(True):
        consolenMenue(playerWins, compWins,playerStatSymbols)
