# How the System Works

This document details the technical implementation and system architecture of the Heart Health Lifestyle Recommendation Engine, explaining how the various components interact to deliver personalized health recommendations.

## System Components

The application is built with a modular structure consisting of:

1. **HeartHealthRecommender Class**: The core engine that processes health data and generates recommendations
2. **Streamlit Web Interface**: The user-facing component for data input and results display
3. **Data Management Layer**: Handles dataset loading and preprocessing
4. **Recommendation Knowledge Base**: Contains curated health recommendations

## Component Interactions

![System Architecture](../system-architecture.png)

## Code Structure and Implementation

### 1. HeartHealthRecommender Class

This class is the central component of the system, responsible for:
- Loading and processing the dataset
- Training the machine learning model
- Analyzing user health profiles
- Generating personalized recommendations

Key methods include:

```python
def __init__(self, data_path):
    # Initialize and load dataset
    self.data = pd.read_csv(data_path, sep='\t')
    self.model = self._train_model()
    # Initialize recommendation database
    self.recommendations = { ... }

def _train_model(self):
    # Train Random Forest Classifier
    X = self.data.drop('Heart_Risk', axis=1)
    y = self.data['Heart_Risk']
    model = RandomForestClassifier(random_state=42)
    model.fit(X, y)
    return model

def get_risk_factors(self, user_data):
    # Extract relevant risk factors from user profile
    risk_factors = []
    for factor in ['High_BP', 'High_Cholesterol', 'Diabetes', ...]:
        if user_data[factor] == 1:
            risk_factors.append(factor)
    return risk_factors

def generate_recommendations(self, user_data):
    # Generate personalized recommendations based on risk factors
    risk_factors = self.get_risk_factors(user_data)
    recommendations = {'diet': [], 'exercise': [], 'habits': []}
    
    # Match risk factors to recommendations
    for factor in risk_factors:
        for category in ['diet', 'exercise', 'habits']:
            recommendations[category].extend(self.recommendations[factor][category])
    
    # Remove duplicates while preserving order
    for category in recommendations:
        recommendations[category] = list(dict.fromkeys(recommendations[category]))
    
    return recommendations
```

### 2. Streamlit User Interface

The system uses Streamlit to create an interactive web interface:

```python
def main():
    st.title("Heart Health Lifestyle Recommendation Engine")
    
    # Initialize recommender
    recommender = HeartHealthRecommender('heart-disease-risk-dataset-sample.csv')
    
    # Collect user data through UI elements
    user_data = {
        'Chest_Pain': st.sidebar.selectbox('Chest Pain', [0, 1], format_func=lambda x: "Yes" if x == 1 else "No"),
        # Additional health profile inputs
        'Age': st.sidebar.slider('Age', 18, 100, 30)
    }
    
    # Generate and display recommendations
    if st.sidebar.button('Generate Recommendations'):
        recommendations = recommender.generate_recommendations(user_data)
        
        # Display recommendations by category
        st.header("Your Personalized Recommendations")
        
        st.subheader("Diet Recommendations")
        for rec in recommendations['diet']:
            st.write(f"• {rec}")
        # Display exercise and habits recommendations
```

### 3. Recommendation Knowledge Base

The system maintains a structured database of health recommendations mapped to specific risk factors:

```python
self.recommendations = {
    'High_BP': {
        'diet': ['Reduce sodium intake', 'Increase potassium-rich foods', 'Follow DASH diet'],
        'exercise': ['Regular aerobic exercise', 'Moderate-intensity workouts', 'Daily walking'],
        'habits': ['Regular blood pressure monitoring', 'Stress management techniques', 'Limit alcohol']
    },
    'High_Cholesterol': {
        'diet': ['Reduce saturated fats', 'Increase fiber intake', 'Include omega-3 rich foods'],
        # Additional recommendations
    },
    # Additional risk factors
}
```

## Error Handling and Validation

The system incorporates robust error handling:

```python
try:
    recommender = HeartHealthRecommender('heart-disease-risk-dataset-sample.csv')
    if not recommender.model_ready:
        st.error("Error initializing the recommendation model.")
except Exception as e:
    st.error(f"Error loading data: {e}")
```

## Data Flow Sequence

1. **Initialization**: Application loads and prepares the dataset and model
2. **User Input**: Health profile information is collected via form elements
3. **Processing**: Upon form submission, the system:
   - Identifies relevant risk factors
   - Matches risk factors to appropriate recommendations
   - Filters and organizes the recommendations
4. **Display**: Results are presented to the user in a clear, categorized format

## Technology Stack

- **Python 3.8+**: Core programming language
- **pandas**: Data manipulation and analysis
- **scikit-learn**: Machine learning framework
- **Streamlit**: Web application development
- **NumPy**: Numerical computing
- **Plotly**: Data visualization capabilities (for future enhancements)

## Performance Considerations

- The system is designed for low-latency response, with recommendations generated in real-time
- The Random Forest model is trained once at application startup, not on each user request
- Recommendation lookup and filtering operations are optimized for speed
- The application is stateless, allowing for horizontal scaling if deployed as a service

## Future System Enhancements

The modular architecture allows for straightforward extensions:
- Integration with electronic health records
- Addition of more sophisticated ML models
- Expansion of the recommendation knowledge base
- Implementation of user accounts and recommendation tracking
- Development of mobile applications using the same core engine 