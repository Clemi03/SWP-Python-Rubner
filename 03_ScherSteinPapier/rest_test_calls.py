import requests

#Einfache Aufrufe des REST-Services

host = 'http://localhost:5000/stats'

print('Speichere einen Eintrag am Server:')
#response = requests.put('%s/%s' % (host, 'franz'), data={"sis":12, "stone":14})
j = {"playerWins":2, "compWins":5, "stats":{'Schere': 10, 'Stein': 0, 'Papier': 0, 'Echse': 0, 'Spock': 0}}
response = requests.put('%s/%s' % (host, 'user') , json=j)
print (response) #Gibt den Response Code aus (Header)
print(response.json()) #Gibt den Response Body aus (also die wirkliche Antwort)

print('---------------------------')
print('Hole diesen Eintrag wieder:')
response = requests.get('%s/%s' % (host, 'user')).json()
print (response)

print("ändern")
j = {"playerWins":4, "compWins":5, "stats":{'Schere': 10, 'Stein': 2, 'Papier': 0, 'Echse': 0, 'Spock': 0}}
response = requests.patch('%s/%s' % (host, 'user'),  json=j).json()
print (response)


print('---------------------------')
print('Hole diesen Eintrag wieder:')
response = requests.get('%s/%s' % (host, 'user')).json()
print (response)

# print('---------------------------')
# print('Löschen :')
# response = requests.delete('%s/%s' % (host, 'hubert'))
# print (response.status_code)
# print (response.json())

# response = requests.delete('%s/%s' % (host, 'hubert'))
# print (response.status_code)