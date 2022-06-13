from flask import Flask, Response
import random


app = Flask(__name__)

@app.route('/get/colour', methods=['GET'])
def colour():
    colours = ['yellow', 'red', 'grey']
    n = random.randint(0,2) # this variable will randomly pick a number between 0 and 4, this number will return the value found at its index position in colours list
    return Response (colours[n], mimetype='text/plain')

if __name__ == ' main ':
    app.run(port=5001, debug=True, host='0.0.0.0')