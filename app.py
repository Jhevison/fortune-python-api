# app.py
from flask import Flask, request, jsonify, Response
import json
import choose
import requests
import ast


app = Flask(__name__)

@app.route('/', methods=['GET'])
def respond():   
    quote = choose.returnQuote()
    dict = {} 
    dict['quote'] = quote   
    return jsonify(dict)


app.config['JSON_AS_ASCII'] = False
app.run()
