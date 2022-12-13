from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app) 

#Speichert den Score zu bestimmten Namen
name_score = {}

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
        if existing:
            return {"Message" : "Überschrieben"}
        return {"Message" : "Neu hinzugefügt"}

    def delete(self, name):
        del name_score[name]
        return {"Message": "%s gelöscht" % name}

    def patch(self, name): #Hier das gleiche wie put, weil ja nur ein Attribut (score) vorhanden ist
        d = request.get_json(force=True)
        name_score[name] = {'playerWins': d['playerWins'], 'compWins':d['compWins'], 'stats': d['stats']}
        return {"Message": "%s gepatched" % name}

#Hier passiert das Mapping auf die Klasse
api.add_resource(Statistik, '/stats/<string:name>')

if __name__ == '__main__':
    app.run(debug=True) #debug=True lädt nach den Änderungen neu


#Aufrufe für SimpleNameScore
# curl http://localhost:5000/score/albert -d "score=100" -X PUT