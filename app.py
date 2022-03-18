from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

@app.route("/")
def get_cerveja():
    r = requests.get('https://api.punkapi.com/v2/beers/random')
    cervejajson = r.json()
    cerveja = {
    'name': cervejajson[0]['name'],
    'abv': cervejajson[0]['abv'],
    'tagline': cervejajson[0]['tagline'],
    'description': cervejajson[0]['description'],
    'foodpair': cervejajson[0]['food_pairing'][0],
    }
    print(cerveja)
    return render_template('index.html', cerveja=cerveja)
