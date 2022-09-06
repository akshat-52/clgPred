import numpy as np
from flask import Flask, request,jsonify,make_response
import sklearn
import numpy
import pickle
import json

app = Flask(__name__)
model = pickle.load(open('jeemodel1.pkl', 'rb'))
#model1 = pickle.load(open('P4.pkl', 'rb'))

# Opening JSON file
#f = open("data.json")

# returns JSON object as
# a dictionary



@app.route('/',methods=['POST'])
def json():
    # if request.method == 'POST':
   # data = request.get_json()
    data = request.get_json()
    Gender_Neutral=float(data['Gender_Neutral'])
    Female_only = float(data['Female_only'])
    Opening_Rank=float(data['Opening_Rank'])
    Closing_Rank=float(data['Closing_Rank'])
    #print(data['IFW'])
    array = np.array([[Gender_Neutral, Female_only, Opening_Rank, Closing_Rank]])
    pre=model.predict(array)
    fpre=int(pre)
    jpre={'pre':fpre}
    print(pre)
    r = make_response(jpre)
    r.mimetype = 'application/'
    return r

    #print(data['IFW'])



if __name__=='__main__':
    app.run(debug=True)
