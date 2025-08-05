# Crop Recommendation System

A modern web application that provides crop recommendations based on soil and climate conditions using machine learning.

## Features

- **Interactive Web Interface**: Beautiful, responsive UI built with Bootstrap and custom CSS
- **Machine Learning Model**: Uses LightGBM for accurate crop predictions
- **Real-time Predictions**: Get instant crop recommendations with confidence scores
- **Crop Information**: Detailed information about recommended crops
- **Sample Data**: Try the system with pre-loaded sample data
- **Probability Analysis**: View confidence scores for all possible crops

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

1. **Clone or download the project files**

2. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:
   ```bash
   python app.py
   ```

4. **Open your web browser** and navigate to:
   ```
   http://localhost:5000
   ```

## Usage

1. **Enter Soil and Climate Data**: Fill in the form with your soil and climate measurements
2. **Get Recommendation**: Click "Get Recommendation" to receive your crop suggestion
3. **View Results**: See the recommended crop with confidence score and detailed information
4. **Try Sample Data**: Use the sample data buttons to test the system with different scenarios

## Sample Data

The application includes three sample datasets for testing:

- **Sample 1**: Rice-growing conditions
- **Sample 2**: Moderate climate conditions
- **Sample 3**: High-nutrient soil conditions

## Technical Details

### Backend
- **Framework**: Flask (Python)
- **Machine Learning**: LightGBM Classifier
- **Data Processing**: Pandas, NumPy
- **Model Persistence**: Pickle serialization

### Frontend
- **Framework**: Bootstrap 5
- **Icons**: Font Awesome
- **Styling**: Custom CSS with modern gradients and animations
- **Interactivity**: Vanilla JavaScript with async/await

### Model Training
The system includes a training function that generates sample data and trains a LightGBM model. In a production environment, you would:

1. Replace the sample data generation with your actual dataset
2. Use the trained model from your Jupyter notebook
3. Implement proper model versioning and deployment

## File Structure

```
crop-recommendation-system/
├── app.py                 # Main Flask application
├── templates/
│   └── index.html        # Web interface template
├── requirements.txt       # Python dependencies
├── README.md             # This file
└── crop-recommendation-system-using-lightgbm.ipynb  # Original notebook
```

## API Endpoints

- `GET /` - Main application page
- `POST /predict` - Get crop recommendation
- `GET /get_crop_info/<crop_name>` - Get information about a specific crop

## Customization

### Adding New Crops
To add information about new crops, edit the `crop_info` dictionary in `app.py`:

```python
crop_info = {
    'new_crop': {
        'description': 'Description of the crop',
        'optimal_conditions': 'Optimal growing conditions',
        'growing_season': 'Growing season duration',
        'water_requirement': 'Water requirement level'
    }
}
```

### Using Your Own Model
To use your own trained model:

1. Save your model as `crop_model.pkl` in the project directory
2. Ensure it accepts the same 7 input features in the correct order
3. The model should have a `predict()` and `predict_proba()` method

## Troubleshooting

### Common Issues

1. **Port already in use**: Change the port in `app.py`:
   ```python
   app.run(debug=True, host='0.0.0.0', port=5001)
   ```

2. **Missing dependencies**: Install all requirements:
   ```bash
   pip install -r requirements.txt
   ```

3. **Model not loading**: The application will automatically train a new model if none exists

## Contributing

Feel free to contribute to this project by:
- Adding more crop information
- Improving the UI/UX
- Adding new features
- Optimizing the machine learning model

## License

This project is open source and available under the MIT License. 