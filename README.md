## Customer Churn Prediction Model using Random Forest
This project develops a predictive model to anticipate customer churn for a telecom company using machine learning techniques, specifically Random Forest. The model uses customer demographics, usage patterns, and service interaction data to predict whether a customer is likely to churn.

#### Requirements:
- Python 3.9
- pandas
- scikit-learn
- numpy
- Flask (for deploying the model)
- Jupyter Notebook (for exploratory data analysis and model development)
- Dependencies listed in requirements.txt

#### Usage
API Endpoint  
Endpoint: /predict  
Method: POST  
Request Body: JSON object containing input data for prediction  

```
{
    "gender": "Male",
    "SeniorCitizen": 0,
    "Partner": "Yes",
    "Dependents": "No",
    "tenure": 1,
    "PhoneService": "No",
    "MultipleLines": "No phone service",
    "InternetService": "DSL",
    "OnlineSecurity": "No",
    "OnlineBackup": "Yes",
    "DeviceProtection": "No",
    "TechSupport": "No",
    "StreamingTV": "No",
    "StreamingMovies": "No",
    "Contract": "Month-to-month",
    "PaperlessBilling": "Yes",
    "PaymentMethod": "Electronic check",
    "MonthlyCharges": 29.85,
    "TotalCharges": 29.85
}
```
Response: JSON object with prediction result
```
{
    "prediction": "No"
}
```
