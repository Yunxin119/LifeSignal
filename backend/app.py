from flask import Flask, request, jsonify
from datetime import datetime
import numpy as np
from sklearn.ensemble import IsolationForest

app = Flask(__name__)

# Generate some sample training data for the model
# These are example normal ranges for heart rate (60-100) and blood oxygen (95-100)
np.random.seed(42)
n_samples = 1000
normal_heart_rates = np.random.uniform(60, 100, n_samples)
normal_blood_oxygen = np.random.uniform(95, 100, n_samples)
training_data = np.column_stack((normal_heart_rates, normal_blood_oxygen))

# Initialize and train the anomaly detection model
anomaly_detector = IsolationForest(contamination=0.1, random_state=42)
anomaly_detector.fit(training_data)

@app.route('/api/analyze_health_data', methods=['POST'])
def analyze_health_data():
    data = request.get_json()
    
    # Extract health metrics
    heart_rate = data.get('heart_rate')
    blood_oxygen = data.get('blood_oxygen')
    
    if not heart_rate or not blood_oxygen:
        return jsonify({'error': 'Missing required health metrics'}), 400
    
    # Prepare data for analysis
    features = np.array([[heart_rate, blood_oxygen]])
    
    # Detect anomalies
    prediction = anomaly_detector.predict(features)
    is_anomaly = prediction[0] == -1
    
    # Calculate risk score (simple example)
    risk_score = calculate_risk_score(heart_rate, blood_oxygen)
    
    return jsonify({
        'timestamp': datetime.now().isoformat(),
        'is_anomaly': bool(is_anomaly),
        'risk_score': risk_score,
        'recommendations': generate_recommendations(risk_score, heart_rate, blood_oxygen)
    })

def calculate_risk_score(heart_rate, blood_oxygen):
    # Define normal ranges
    hr_normal_low, hr_normal_high = 60, 100
    bo_normal_low = 95
    
    # Calculate heart rate risk
    if hr_normal_low <= heart_rate <= hr_normal_high:
        hr_risk = 0
    else:
        # Calculate how far from normal range
        hr_deviation = min(abs(heart_rate - hr_normal_low), 
                         abs(heart_rate - hr_normal_high))
        hr_risk = min(100, (hr_deviation / 20) * 100)  # 20 BPM deviation = 100% risk
    
    # Calculate blood oxygen risk
    if blood_oxygen >= bo_normal_low:
        bo_risk = 0
    else:
        bo_deviation = bo_normal_low - blood_oxygen
        bo_risk = min(100, (bo_deviation / 5) * 100)  # 5% deviation = 100% risk
    
    # Weighted average (blood oxygen is more critical)
    return (hr_risk * 0.4 + bo_risk * 0.6)

def generate_recommendations(risk_score, heart_rate, blood_oxygen):
    recommendations = []
    
    # Severe conditions requiring immediate attention
    if blood_oxygen < 90 or heart_rate > 150 or heart_rate < 40:
        recommendations.extend([
            "URGENT: Immediate medical attention required",
            "Contact emergency services immediately",
            f"Critical values detected: HR={heart_rate}, SpO2={blood_oxygen}%"
        ])
    
    # High risk conditions
    elif risk_score > 70:
        recommendations.extend([
            "Contact your healthcare provider soon",
            "Monitor vital signs closely",
            "Rest and avoid physical exertion"
        ])
    
    # Moderate risk conditions
    elif risk_score > 40:
        recommendations.extend([
            "Continue monitoring your vital signs",
            "Consider contacting your healthcare provider if symptoms persist",
            "Take rest and stay hydrated"
        ])
    
    # Low risk or normal conditions
    else:
        recommendations.extend([
            "Vital signs are within normal range",
            "Continue normal activities",
            "Stay hydrated and maintain regular monitoring"
        ])
    
    return recommendations

if __name__ == '__main__':
    print("Model trained with sample data. Ready to process health metrics.")
    app.run(host='0.0.0.0', port=5100) 