import io
import pandas as pd
import pycaret
from pycaret.regression import *
from pycaret.regression import RegressionExperiment
from flask import Flask, request, jsonify

filename = 'UPDRS_prediction_model'

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files.get('file')
        if file is None or file.filename == "":
            return jsonify({"error": "no file"})

        try:
            X_test = pd.read_csv(file)
            loaded_best_pipeline = load_model(filename)
            prediction = predict_model(loaded_best_pipeline, data=X_test)
            data = prediction
            return data.to_json()
        except Exception as e:
            return jsonify({"error": str(e)})

    return "OK"


if __name__ == "__main__":
    app.run(debug=True)