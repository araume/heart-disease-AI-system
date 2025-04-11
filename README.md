# Heart Health Lifestyle Recommendation Engine

This system provides personalized lifestyle recommendations based on health profiles to help reduce the risk of heart disease. It uses machine learning to analyze health data and generates customized diet, exercise, and habit recommendations.

## Features

- Interactive web interface using Streamlit
- Personalized recommendations based on health profile
- Comprehensive risk factor analysis
- Customized diet, exercise, and lifestyle recommendations

## Documentation

Detailed documentation is available in the IMPORTANT folder:

| Document | Description |
|----------|-------------|
| [Introduction](IMPORTANT/01_Introduction.md) | Overview of the system, its purpose, target users, and features |
| [Installation Guide](IMPORTANT/02_Installation.md) | Detailed setup instructions and troubleshooting |
| [How It Works](IMPORTANT/03_How_It_Works.md) | High-level overview of system architecture and components |
| [Analysis Methods](IMPORTANT/04_How_Analysis_Works.md) | Technical explanation of data analysis and ML processes |
| [System Architecture](IMPORTANT/05_How_System_Works.md) | Detailed implementation and code structure |
| [Output Explanation](IMPORTANT/06_Output_Explanation.md) | Guide to understanding and interpreting recommendations |
| [User Benefits](IMPORTANT/07_User_Benefits.md) | How to maximize value and implement lifestyle changes |

## Installation

1. Clone this repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Activate your virtual environment
2. Run the application:
   ```bash
   streamlit run app.py
   ```
3. Open your web browser and navigate to the provided local URL
4. Fill in your health profile in the sidebar
5. Click "Generate Recommendations" to get personalized suggestions

## Data

The system uses a heart disease risk prediction dataset that includes:
- Symptoms (chest pain, shortness of breath, etc.)
- Medical conditions (high blood pressure, diabetes, etc.)
- Lifestyle factors (smoking, sedentary lifestyle, etc.)
- Demographic information (age, gender)

## Recommendations

The system provides recommendations in three categories:
1. Diet: Customized eating plans and nutritional advice
2. Exercise: Personalized physical activity suggestions
3. Habits: Lifestyle modifications to reduce heart disease risk

## Note

This system is for educational purposes and should not replace professional medical advice. Always consult with healthcare professionals for medical decisions.


