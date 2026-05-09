# Rwanda House Price Prediction

A Flask-based API for predicting house prices in Rwanda using a machine learning model.

## Features

- Predict house prices based on size (sq ft), number of bedrooms, bathrooms, and location.
- Uses a trained Random Forest model with location encoding.

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/Ishimwe-Kevin/rwanda_house_price_ai_model.git
   cd rwanda_house_price_ai_model
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the app locally:
   ```
   python app.py
   ```
   The app will run on `http://localhost:5000`.

## Usage

Send a POST request to `/predict` with JSON data:

```json
{
  "size": 1000,
  "bedrooms": 2,
  "bathrooms": 1,
  "location": "Kigali"
}
```

Example using curl:
```
curl -X POST http://localhost:5000/predict -H "Content-Type: application/json" -d '{"size": 1000, "bedrooms": 2, "bathrooms": 1, "location": "Kigali"}'
```

Response:
```json
{
  "predicted_price": 250000.0
}
```

## Deployment

This app is deployed on Render. To deploy your own instance:

1. Push code to a GitHub repository.
2. Go to [Render](https://render.com) and create a new Web Service.
3. Connect your GitHub repo.
4. Set:
   - Runtime: Python 3
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `python app.py`
5. Deploy.

## Model Details

- Trained on `houses.csv` data.
- Model: `house_model.pkl` (Random Forest Regressor)
- Encoder: `location_encoder.pkl` (Label Encoder for locations)

## Files

- `app.py`: Flask application
- `houses.csv`: Training data
- `houses.ipynb`: Jupyter notebook for model training
- `requirements.txt`: Python dependencies
- `house_model.pkl`: Trained model
- `location_encoder.pkl`: Location encoder

## License

MIT License