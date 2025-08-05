#!/usr/bin/env python3
"""
Test script to verify the RandomForest model works correctly
"""

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import pickle

def test_model():
    """Test the model training and prediction"""
    print("Testing RandomForest model...")
    
    # Create sample data
    np.random.seed(42)
    n_samples = 100
    
    data = {
        'N': np.random.randint(0, 140, n_samples),
        'P': np.random.randint(5, 145, n_samples),
        'K': np.random.randint(5, 205, n_samples),
        'temperature': np.random.uniform(8.0, 44.0, n_samples),
        'humidity': np.random.uniform(14.0, 100.0, n_samples),
        'ph': np.random.uniform(3.5, 10.0, n_samples),
        'rainfall': np.random.uniform(20.0, 300.0, n_samples)
    }
    
    crops = ['rice', 'maize', 'chickpea', 'cotton', 'coffee']
    data['crop'] = np.random.choice(crops, n_samples)
    
    df = pd.DataFrame(data)
    X = df.drop('crop', axis=1)
    y = df['crop']
    
    # Train model
    model = RandomForestClassifier(n_estimators=50, random_state=42, n_jobs=1)
    model.fit(X, y)
    
    # Test prediction
    test_features = [90, 42, 43, 20.9, 75, 5.5, 220]
    test_array = np.array(test_features).reshape(1, -1)
    
    prediction = model.predict(test_array)[0]
    probability = model.predict_proba(test_array)[0]
    max_prob = max(probability)
    
    print(f"✅ Model trained successfully")
    print(f"✅ Prediction: {prediction}")
    print(f"✅ Confidence: {max_prob:.2%}")
    print(f"✅ Model type: {type(model).__name__}")
    
    # Save model
    with open('crop_model.pkl', 'wb') as f:
        pickle.dump(model, f)
    
    print("✅ Model saved successfully")
    return True

if __name__ == "__main__":
    test_model() 