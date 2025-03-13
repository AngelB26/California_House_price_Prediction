import pickle
import numpy as np
from flask import Flask, request, jsonify

# Load the saved model
with open("random_forest_model.pkl", "rb") as file:
    model = pickle.load(file)

app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get JSON data from request
        data = request.get_json()
        
        
        # Convert input into NumPy array (ensure correct format)
        features = np.array(data["features"]).reshape(1, -1)

        # Make prediction
        prediction = model.predict(features)

        # Return response
        return jsonify({"predicted_price": float(prediction[0])})
    
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
