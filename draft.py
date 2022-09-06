import numpy as np
from flask import Flask, request,jsonify,make_response
import sklearn
import numpy
import pickle
import json

app = Flask(__name__)
model = pickle.load(open('draft1.pkl', 'rb'))
#model1 = pickle.load(open('P4.pkl', 'rb'))

# Opening JSON file
#f = open("data.json")

# returns JSON object as
# a dictionary



@app.route('/json',methods=['POST'])
def json():
    # if request.method == 'POST':
   # data = request.get_json()
    data = request.get_json()
    Opening_Rank=float(data['Opening_Rank'])
    Closing_Rank=float(data['Closing_Rank'])
    AI = float(data['AI'])
    GO = float(data['GO'])
    HS = float(data['HS'])
    JK = float(data['JK'])
    LA = float(data['LA'])
    OS = float(data['OS'])
    EWS = float(data['EWS'])
    EWS_PWD = float(data['EWS_PWD'])
    OBC_NCL = float(data['OBC_NCL'])
    OBC_NCL_PWD = float(data['OBC_NCL_PWD'])
    OPEN = float(data['OPEN'])
    OPEN_PWD = float(data['OPEN_PWD'])
    SC = float(data['SC'])
    SC_PWD = float(data['SC_PWD'])
    ST= float(data['ST'])
    ST_PWD = float(data['ST_PWD'])
    Female_only = float(data['Female_only'])
    Gender_Neutral = float(data['Gender_Neutral'])

    #'Opening_Rank', 'Closing_Rank', 'AI', 'GO', 'HS', 'JK', 'LA', 'OS',
    #   'EWS', 'EWS (PwD)', 'OBC-NCL', 'OBC-NCL (PwD)', 'OPEN', 'OPEN (PwD)',
    #   'SC', 'SC (PwD)', 'ST', 'ST (PwD)', 'Female_only', 'Gender_Neutral'
    #print(data['IFW'])
    array = np.array([[Opening_Rank, Closing_Rank, AI, GO, HS, JK, LA, OS, EWS, EWS_PWD, OBC_NCL, OBC_NCL_PWD, OPEN, OPEN_PWD, SC, SC_PWD, ST, ST_PWD, Female_only, Gender_Neutral]])
    pre=model.predict(array)
    fpre=int(pre)
    jpre={'pre':fpre}
    print(pre)
    r = make_response(jpre)
    r.mimetype = 'application/json'
    return r

    #print(data['IFW'])



if __name__=='__main__':
    app.run(debug=True)
