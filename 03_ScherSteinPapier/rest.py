from flask import Flask, request, render_template, url_for, redirect
from flask_restful import Resource, Api
import plotly.express as px

app = Flask(__name__)
api = Api(app) 

name_score = {}

@app.route('/', methods=('GET', 'POST'))
def home():
    return render_template('index.html')


@app.route('/statsPlayer', methods=('GET', 'POST'))
def statsPlayer(user='user'):
    data = dict(name_score[user])

    fig = px.bar({"symbole":["Schere","Stein", "Papier", "Echse","Spock"], "werte":[data['stats']['Schere'],data['stats']['Stein'],data['stats']['Papier'],data['stats']['Echse'],data['stats']['Spock']]}, x='symbole', y='werte')
    fig.show()
    return redirect(url_for('home'))


@app.route('/wins', methods=('GET', 'POST'))
def wins(user='user'):
    data = dict(name_score[user])

    fig = px.bar({"player":["du","computer"], "werte":[data['playerWins'],data['compWins']]}, x='player', y='werte')
    fig.show()
    return redirect(url_for('home'))

@app.route('/statsPlayerPie', methods=('GET', 'POST'))
def piestatsPlayer(user='user'):
    data = dict(name_score[user])
    df={"symbole":["Schere","Stein", "Papier", "Echse","Spock"], "werte":[data['stats']['Schere'],data['stats']['Stein'],data['stats']['Papier'],data['stats']['Echse'],data['stats']['Spock']]}
    fig = px.pie(df, values='werte', names='symbole')
    fig.show()
    return redirect(url_for('home'))

@app.route('/winsPie', methods=('GET', 'POST'))
def winsPie(user='user'):
    data = dict(name_score[user])
    df = {"player":["du","computer"], "werte":[data['playerWins'],data['compWins']]}
    fig = px.pie(df, values='werte', names='player')
    fig.show()
    return redirect(url_for('home'))



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

    def patch(self, name): 
        d = request.get_json(force=True)
        name_score[name] = {'playerWins': d['playerWins'], 'compWins':d['compWins'], 'stats': d['stats']}
        return {"Message": "%s gepatched" % name}

api.add_resource(Statistik, '/stats/<string:name>')

if __name__ == '__main__':
    app.run(debug=True) 

#Aufrufe für SimpleNameScore
# curl http://localhost:5000/stats/user"