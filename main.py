import numpy as np
from flask import Flask, request,jsonify ,make_response
import sklearn
import numpy
import pickle
import json

app = Flask(__name__)
model = pickle.load(open('ml_model.pkl', 'rb'))

# Opening JSON file
#f = open("data.json")

# returns JSON object as
# a dictionary



@app.route('/json',methods=['POST'])
def json():
    if request.method == 'POST':
        data = request.get_json()
        Seat_Type=float(data['Seat_Type'])
        Opening_Rank=float(data['Opening_Rank'])
        Closing_Rank=float(data['Closing_Rank'])
        print(data['Seat_Type'])
    array = np.array([[Seat_Type, Opening_Rank, Closing_Rank]])
    pre=model.predict(array)
    fpre=int(pre)
    jpre={'pre':fpre}
    print(pre)
    r = make_response(jpre)
    r.mimetype = 'application/json'
    return r


if __name__=='main_':
        app.run(debug=True)