# House Price Prediction API

This is a simple Flask API that serves predictions using a pre-trained Random Forest model. The model takes input features and returns the predicted house price.

## Prerequisites

Make sure you have the following installed:
- Python 3.7+
- `pip` (Python package manager)
- `virtualenv` (optional but recommended)

## Setup Instructions

### 1️⃣ Clone the Repository (If Applicable)
```bash
# Clone the repository (if applicable)
git clone <repo-url>
cd House_price_prediction
```

### 2️⃣ Create and Activate Virtual Environment
```bash
# Create a virtual environment
python -m venv venv

# Activate virtual environment (Windows)
venv\Scripts\activate

# Activate virtual environment (Mac/Linux)
source venv/bin/activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Ensure the Model File Exists
Make sure the `random_forest_model.pkl` file is present in the project directory.

### 5️⃣ Run the Flask App
```bash
python app.py
```
By default, the server runs on `http://127.0.0.1:5000/`.

### 6️⃣ Test the API
Once the server is running, you can test the API using `curl` or Postman.

#### Example Request (Using `curl`):
```bash
curl -X POST "http://127.0.0.1:5000/predict" \
     -H "Content-Type: application/json" \
     -d '{"features": [3, 2, 1500]}'
```

#### Expected Response:
```json
{
  "predicted_price": 250000.0
}
```

### 7️⃣ Troubleshooting
#### "Connection Refused" Error
- Make sure the Flask app is running.
- Disable firewall/antivirus temporarily.
- Change Flask's port in `app.py`:
  ```python
  app.run(host='0.0.0.0', port=8000)
  ```
  Then access `http://127.0.0.1:8000/predict`.

#### "Module Not Found" Error
- Ensure dependencies are installed: `pip install -r requirements.txt`
- Check if `random_forest_model.pkl` exists in the project directory.

## License
This project is open-source. Modify and use as needed!

