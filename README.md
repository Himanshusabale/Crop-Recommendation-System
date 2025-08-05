# Crop Recommendation System

A modern web application that provides crop recommendations based on soil and climate conditions using machine learning.

## Features

- **Interactive Web Interface**: Beautiful, responsive UI
- **Machine Learning Model**: Uses RandomForest for accurate predictions
- **Real-time Predictions**: Get instant crop recommendations with confidence scores
- **Crop Information**: Detailed information about recommended crops

## Input Parameters

The system analyzes the following soil and climate parameters:

1. **Nitrogen (N)** - kg/ha (0-140)
2. **Phosphorus (P)** - kg/ha (5-145)
3. **Potassium (K)** - kg/ha (5-205)
4. **Temperature** - °C (8-44)
5. **Humidity** - % (14-100)
6. **pH Level** - (3.5-10)
7. **Rainfall** - mm (20-300)

## Installation

1. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the application**:
   ```bash
   python app.py
   ```

3. **Open your web browser** and navigate to:
   ```
   http://localhost:5000
   ```

## Deployment

### Vercel Deployment

1. **Go to [vercel.com](https://vercel.com)**
2. **Import your GitHub repository**
3. **Deploy automatically**

### Railway Deployment

1. **Go to [railway.app](https://railway.app)**
2. **Connect your GitHub repository**
3. **Deploy with one click**

## File Structure

```
crop-recommendation-system/
├── app.py                 # Main Flask application
├── templates/
│   └── index.html        # Web interface template
├── requirements.txt       # Python dependencies
├── vercel.json           # Vercel configuration
└── README.md             # This file
```

## API Endpoints

- `GET /` - Main application page
- `POST /predict` - Get crop recommendation
- `GET /get_crop_info/<crop_name>` - Get information about a specific crop

## License

This project is open source and available under the MIT License. 