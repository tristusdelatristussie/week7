from flask import Flask, jsonify, request
import pickle


app = Flask(__name__)

#open models with pickle
with open('rf_model.bin', 'rb')  as f_in:
    model_rf = pickle.load(f_in)
f_in.close()

with open('xgb_model.bin', 'rb')  as f_in:
    model_xgb = pickle.load(f_in)
f_in.close()

with open('dv.bin', 'rb')  as f_in:
    dv = pickle.load(f_in)
f_in.close()


# route predict
@app.route("/predict", methods=["POST"])
def predict():
    #retrieve data and transform
    data = request.get_json()
    X_rf = dv.transform([data])
    X_xgb = dv.transform([data])
    #predict
    xgb_res = model_xgb.predict(X_xgb)
    X_rf_res = model_rf.predict(X_rf)
    #return restults
    return jsonify({"result for prediction_xgb": xgb_res.tolist(),
                    "result for prediction_rf": X_rf_res.tolist()})

if __name__ == "__main__":
   app.run(debug=True, host='0.0.0.0', port=9797) 