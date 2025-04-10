import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import streamlit as st
import plotly.express as px

class HeartHealthRecommender:
    def __init__(self, data_path):
        # Handle tab-delimited file
        self.data = pd.read_csv(data_path, sep='\t')
        
        # Print columns for debugging
        print("Columns in dataset:", self.data.columns.tolist())
        
        # Make sure the model is only initialized if data loading is successful
        try:
            self.model = self._train_model()
            self.model_ready = True
        except Exception as e:
            print(f"Error training model: {e}")
            self.model_ready = False
            
        self.recommendations = {
            'High_BP': {
                'diet': ['Reduce sodium intake', 'Increase potassium-rich foods', 'Follow DASH diet'],
                'exercise': ['Regular aerobic exercise', 'Moderate-intensity workouts', 'Daily walking'],
                'habits': ['Regular blood pressure monitoring', 'Stress management techniques', 'Limit alcohol']
            },
            'High_Cholesterol': {
                'diet': ['Reduce saturated fats', 'Increase fiber intake', 'Include omega-3 rich foods'],
                'exercise': ['Regular cardio workouts', 'Maintain healthy weight', 'Daily physical activity'],
                'habits': ['Regular cholesterol checks', 'Quit smoking', 'Maintain healthy weight']
            },
            'Diabetes': {
                'diet': ['Low glycemic index foods', 'Balanced carbohydrate intake', 'Regular meal timing'],
                'exercise': ['Regular physical activity', 'Strength training', 'Daily movement'],
                'habits': ['Regular blood sugar monitoring', 'Consistent meal schedule', 'Proper sleep']
            },
            'Smoking': {
                'diet': ['Antioxidant-rich foods', 'Vitamin C supplements', 'Stay hydrated'],
                'exercise': ['Gradual increase in activity', 'Deep breathing exercises', 'Regular cardio'],
                'habits': ['Smoking cessation program', 'Stress management', 'Support group participation']
            },
            'Obesity': {
                'diet': ['Calorie-controlled meals', 'Portion control', 'Balanced macronutrients'],
                'exercise': ['Regular physical activity', 'Strength training', 'Daily movement'],
                'habits': ['Regular weight monitoring', 'Meal planning', 'Sleep hygiene']
            },
            'Sedentary_Lifestyle': {
                'diet': ['Balanced nutrition', 'Regular meal timing', 'Stay hydrated'],
                'exercise': ['Start with walking', 'Gradual activity increase', 'Regular movement breaks'],
                'habits': ['Set activity reminders', 'Standing desk use', 'Regular breaks from sitting']
            },
            'Chronic_Stress': {
                'diet': ['Balanced meals', 'Limit caffeine', 'Include stress-reducing foods'],
                'exercise': ['Yoga', 'Meditation', 'Regular physical activity'],
                'habits': ['Mindfulness practice', 'Regular relaxation', 'Proper sleep schedule']
            }
        }

    def _train_model(self):
        # Check if the 'Heart_Risk' column exists
        if 'Heart_Risk' not in self.data.columns:
            raise ValueError(f"'Heart_Risk' column not found. Available columns: {self.data.columns.tolist()}")
            
        X = self.data.drop('Heart_Risk', axis=1)
        y = self.data['Heart_Risk']
        model = RandomForestClassifier(random_state=42)
        model.fit(X, y)
        return model

    def get_risk_factors(self, user_data):
        risk_factors = []
        for factor in ['High_BP', 'High_Cholesterol', 'Diabetes', 'Smoking', 
                      'Obesity', 'Sedentary_Lifestyle', 'Chronic_Stress']:
            if user_data[factor] == 1:
                risk_factors.append(factor)
        return risk_factors

    def generate_recommendations(self, user_data):
        risk_factors = self.get_risk_factors(user_data)
        recommendations = {
            'diet': [],
            'exercise': [],
            'habits': []
        }
        
        for factor in risk_factors:
            for category in ['diet', 'exercise', 'habits']:
                recommendations[category].extend(self.recommendations[factor][category])
        
        # Remove duplicates while preserving order
        for category in recommendations:
            recommendations[category] = list(dict.fromkeys(recommendations[category]))
        
        return recommendations

def main():
    st.title("Heart Health Lifestyle Recommendation Engine")
    st.write("""
    This system provides personalized lifestyle recommendations based on your health profile
    to help reduce the risk of heart disease.
    """)

    # Initialize the recommender
    try:
        recommender = HeartHealthRecommender('heart-disease-risk-dataset-sample.csv')
        if not recommender.model_ready:
            st.error("Error initializing the recommendation model. Please check the console for details.")
            return
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return

    # Create input form
    st.sidebar.header("Your Health Profile")
    
    # Collect user data
    user_data = {
        'Chest_Pain': st.sidebar.selectbox('Chest Pain', [0, 1], format_func=lambda x: "Yes" if x == 1 else "No"),
        'Shortness_of_Breath': st.sidebar.selectbox('Shortness of Breath', [0, 1], format_func=lambda x: "Yes" if x == 1 else "No"),
        'Fatigue': st.sidebar.selectbox('Fatigue', [0, 1], format_func=lambda x: "Yes" if x == 1 else "No"),
        'Palpitations': st.sidebar.selectbox('Palpitations', [0, 1], format_func=lambda x: "Yes" if x == 1 else "No"),
        'Dizziness': st.sidebar.selectbox('Dizziness', [0, 1], format_func=lambda x: "Yes" if x == 1 else "No"),
        'Swelling': st.sidebar.selectbox('Swelling', [0, 1], format_func=lambda x: "Yes" if x == 1 else "No"),
        'Pain_Arms_Jaw_Back': st.sidebar.selectbox('Pain in Arms/Jaw/Back', [0, 1], format_func=lambda x: "Yes" if x == 1 else "No"),
        'Cold_Sweats_Nausea': st.sidebar.selectbox('Cold Sweats/Nausea', [0, 1], format_func=lambda x: "Yes" if x == 1 else "No"),
        'High_BP': st.sidebar.selectbox('High Blood Pressure', [0, 1], format_func=lambda x: "Yes" if x == 1 else "No"),
        'High_Cholesterol': st.sidebar.selectbox('High Cholesterol', [0, 1], format_func=lambda x: "Yes" if x == 1 else "No"),
        'Diabetes': st.sidebar.selectbox('Diabetes', [0, 1], format_func=lambda x: "Yes" if x == 1 else "No"),
        'Smoking': st.sidebar.selectbox('Smoking', [0, 1], format_func=lambda x: "Yes" if x == 1 else "No"),
        'Obesity': st.sidebar.selectbox('Obesity', [0, 1], format_func=lambda x: "Yes" if x == 1 else "No"),
        'Sedentary_Lifestyle': st.sidebar.selectbox('Sedentary Lifestyle', [0, 1], format_func=lambda x: "Yes" if x == 1 else "No"),
        'Family_History': st.sidebar.selectbox('Family History of Heart Disease', [0, 1], format_func=lambda x: "Yes" if x == 1 else "No"),
        'Chronic_Stress': st.sidebar.selectbox('Chronic Stress', [0, 1], format_func=lambda x: "Yes" if x == 1 else "No"),
        'Gender': st.sidebar.selectbox('Gender', [0, 1], format_func=lambda x: "Male" if x == 1 else "Female"),
        'Age': st.sidebar.slider('Age', 18, 100, 30)
    }

    if st.sidebar.button('Generate Recommendations'):
        # Get recommendations
        recommendations = recommender.generate_recommendations(user_data)
        
        # Display recommendations
        st.header("Your Personalized Recommendations")
        
        st.subheader("Diet Recommendations")
        if recommendations['diet']:
            for rec in recommendations['diet']:
                st.write(f"• {rec}")
        else:
            st.write("No specific diet recommendations for your profile.")
            
        st.subheader("Exercise Recommendations")
        if recommendations['exercise']:
            for rec in recommendations['exercise']:
                st.write(f"• {rec}")
        else:
            st.write("No specific exercise recommendations for your profile.")
            
        st.subheader("Lifestyle Habit Recommendations")
        if recommendations['habits']:
            for rec in recommendations['habits']:
                st.write(f"• {rec}")
        else:
            st.write("No specific lifestyle habit recommendations for your profile.")

if __name__ == "__main__":
    main() 