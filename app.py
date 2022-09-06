from flask import Flask, jsonify, request
import pickle
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET"])
def home():
    return "<center><h1> This is the Home Route </h1></center>"

@app.route("/predict", methods=["GET", "POST"])

def predict():
    with open("ml_model.pickle", "rb") as f:
        model = pickle.load(f)

request.form

request.json


@app.route('/json',methods=['POST'])
def json():
    # if request.method == 'POST':
    data = request.get_json()
    Seat_Type=int(data['Seat_Type'])
    Opening_Rank=float(data['Opening_Rank'])
    Closing_Rank=float(data['Closing_Rank'])
    #print(data['IFW'])
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