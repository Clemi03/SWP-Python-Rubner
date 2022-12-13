import random
import ast
from flask import Flask, request
from flask_restful import Resource, Api

choices = ["Schere","Stein", "Papier", "Echse","Spock"]

playerWins = 0
playerStatSymbols = {"Schere" : 0,"Stein": 0, "Papier": 0, "Echse": 0,"Spock": 0}
compWins = 0

app = Flask(__name__)
api = Api(app) 

name_score = {}


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

def comp_selectWithAnalyse():
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


def game(runden):
    for i in range(0,runden):
        player = player_select()
        comp = comp_selcet()
        print(comp)
        analysis(comp,player)
        print("Player: " + str(playerWins) + ", Comp: " + str(compWins))
        print(playerStatSymbols)
    # loadDataFromStorage()
    # saveDataToStorage()

def gameWithAnalyse(runden):
    for i in range(0,runden):
        player = player_select()
        comp = comp_selectWithAnalyse()
        print(comp)
        analysis(comp,player)
        print("Player: " + str(playerWins) + ", Comp: " + str(compWins))
        print(playerStatSymbols)


def loadDataFromStorage(doc = '\db.txt'):
    global playerWins, compWins,playerStatSymbols
    datei = open(r'C:\Users\Clemens\Dokumente\Schule\HTL\5.Klasse\SWP-python\SWP-Python-Rubner\03_ScherSteinPapier' + doc,'r')
    data = ast.literal_eval(str(datei.read()))
    playerWins = data['PlayerWins']
    compWins = data['CompWins']
    playerStatSymbols = data['stats']
    datei.close()


def saveDataToStorage(doc = '\db.txt'):
    data = {
    "PlayerWins": playerWins,
    "CompWins": compWins,
    "stats":playerStatSymbols
    }
    with open(r'C:\Users\Clemens\Dokumente\Schule\HTL\5.Klasse\SWP-python\SWP-Python-Rubner\03_ScherSteinPapier'+ doc,'w') as db:
        db.write(str(data))
        db.close()

def consolenMenue():
    print("[Spielen, Statistik, Daten Uploaden, Spiel mit Analyse]")
    inp = input()
    if(inp == 'Spielen'):
        print("Anzahl versuche:")
        inp2 = int(input())
        game(inp2)
    elif(inp == 'Statistik'):
        loadDataFromStorage()
        print("playerWins",playerWins)
        print("compWins",compWins)
        print(playerStatSymbols)
    elif(inp == 'Daten Uploaden'):
        saveDataToStorage()
    elif(inp == 'Spiel mit Analyse'):
        print("Anzahl versuche:")
        inp2 = int(input())
        loadDataFromStorage()
        gameWithAnalyse(inp2)  
    else:
        print("Falsche eingabe, erneut")
        consolenMenue()


class Statistik(Resource):
    def get(self, name):
        if name in name_score:
            return {name: name_score[name]}
        return {"Message" : "Nicht vorhanden"}

    def put(self, name):
        print(name)
        existing = name in name_score
        d = request.get_json(force=True)
        name_score[name] = {'playerWins': d['playerWins'], 'compWins':d['compWins'], 'stats': d['stats']}
        # TODO wie mit API?? Speichern nach jedem Spiel?? und holen??
        if existing:
            return {"Message" : "Überschrieben"}
        return {"Message" : "Neu hinzugefügt"}

    def delete(self, name):
        del name_score[name]
        return {"Message": "%s gelöscht" % name}

    def patch(self, name):
        d = request.get_json(force=True)
        name_score[name] = {'playerWins': d['playerWins'], 'compWins':d['compWins'], 'stats': d['stats']}
        return {"Message": "%s gepatched" % name}
api.add_resource(Statistik, '/stats/<string:name>')


if __name__ == '__main__':
    app.run(debug=True)
    loadDataFromStorage()
    while(True):
        consolenMenue()
