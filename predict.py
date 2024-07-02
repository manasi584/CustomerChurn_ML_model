import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler

# Load the trained model
model = joblib.load('customer_churn_model.pkl')





def preprocess_input(input_data):
    
    input_df = pd.DataFrame([input_data])
    for i in range(len(input_df)):
        for j in range(len(input_df.columns)):
            print(input_df.iloc[i, j])
    # Encoding categorical variables
    input_df = pd.get_dummies(input_df, columns=[ 
                                                 'MultipleLines', 'InternetService', 'OnlineSecurity', 
                                                 'OnlineBackup', 'DeviceProtection', 'TechSupport', 
                                                 'StreamingTV', 'StreamingMovies', 'Contract', 
                                                 'PaymentMethod'])
    print("**********************")
    for i in range(len(input_df)):
        for j in range(len(input_df.columns)):
            print(input_df.iloc[i, j])
    
    
    input_df['gender'] = input_df['gender'].map({'Female': 1, 'Male': 0})
    input_df['Partner'] = input_df['Partner'].map({'Yes': 1, 'No': 0})
    input_df['Dependents'] = input_df['Dependents'].map({'Yes': 1, 'No': 0})
    input_df['PhoneService'] = input_df['PhoneService'].map({'Yes': 1, 'No': 0})
    input_df['PaperlessBilling'] = input_df['PaperlessBilling'].map({'Yes': 1, 'No': 0})

    for col in input_df.select_dtypes(include=['bool']).columns:
        input_df[col] = input_df[col].astype(int)
    print("**********************")
    input_df['TotalCharges'] = pd.to_numeric(input_df['TotalCharges'], errors='coerce')
    input_df['TotalCharges'] = input_df['TotalCharges'].fillna(0)
    
    print("**********************")
    # scaler = StandardScaler()
    
    # input_df[['tenure', 'MonthlyCharges', 'TotalCharges']] = scaler.fit_transform(input_df[['tenure', 'MonthlyCharges', 'TotalCharges']])
    
    # print(input_df.columns)

    # print(input_df.shape)

    print("**********************")

    for i in range(len(input_df)):
        for j in range(len(input_df.columns)):
            print(input_df.iloc[i, j])

    required_columns =['gender', 'SeniorCitizen', 'Partner', 'Dependents', 'tenure',
       'PhoneService', 'PaperlessBilling', 'MonthlyCharges', 'TotalCharges',
       'MultipleLines_No phone service', 'MultipleLines_Yes',
       'InternetService_Fiber optic', 'InternetService_No',
       'OnlineSecurity_No internet service', 'OnlineSecurity_Yes',
       'OnlineBackup_No internet service', 'OnlineBackup_Yes',
       'DeviceProtection_No internet service', 'DeviceProtection_Yes',
       'TechSupport_No internet service', 'TechSupport_Yes',
       'StreamingTV_No internet service', 'StreamingTV_Yes',
       'StreamingMovies_No internet service', 'StreamingMovies_Yes',
       'Contract_One year', 'Contract_Two year',
       'PaymentMethod_Credit card (automatic)',
       'PaymentMethod_Electronic check', 'PaymentMethod_Mailed check']
    
    
    for col in required_columns:
        if col not in input_df.columns:
            input_df[col] = 0
    
   
    input_df = input_df[required_columns]

    
    return input_df


def predict_churn(input_data):
    
    processed_data = preprocess_input(input_data)
    
    pd.set_option('display.max_rows', None)  # None means display all rows
    pd.set_option('display.max_columns', None)  # None means display all columns
 
    
    
    
    prediction = model.predict(processed_data)
    if(prediction==0):
        return 'No'
    else:
        return 'Yes'
    
    


def get_input():
    input_data = {}
    
    input_data['gender'] = input("Enter gender (Male/Female): ")
    input_data['SeniorCitizen'] = int(input("Enter SeniorCitizen (0 for No, 1 for Yes): "))
    input_data['Partner'] = input("Enter Partner (Yes/No): ")
    input_data['Dependents'] = input("Enter Dependents (Yes/No): ")
    input_data['tenure'] = int(input("Enter tenure (in months): "))
    input_data['PhoneService'] = input("Enter PhoneService (Yes/No): ")
    input_data['MultipleLines'] = input("Enter MultipleLines (Yes/No/No phone service): ")
    input_data['InternetService'] = input("Enter InternetService (DSL/Fiber optic/No): ")
    input_data['OnlineSecurity'] = input("Enter OnlineSecurity (Yes/No/No internet service): ")
    input_data['OnlineBackup'] = input("Enter OnlineBackup (Yes/No/No internet service): ")
    input_data['DeviceProtection'] = input("Enter DeviceProtection (Yes/No/No internet service): ")
    input_data['TechSupport'] = input("Enter TechSupport (Yes/No/No internet service): ")
    input_data['StreamingTV'] = input("Enter StreamingTV (Yes/No/No internet service): ")
    input_data['StreamingMovies'] = input("Enter StreamingMovies (Yes/No/No internet service): ")
    input_data['Contract'] = input("Enter Contract (Month-to-month/One year/Two year): ")
    input_data['PaperlessBilling'] = input("Enter PaperlessBilling (Yes/No): ")
    input_data['PaymentMethod'] = input("Enter PaymentMethod (Electronic check/Mailed check/Credit card (automatic)/Bank transfer (automatic)): ")
    input_data['MonthlyCharges'] = float(input("Enter MonthlyCharges: "))
    input_data['TotalCharges'] = float(input("Enter TotalCharges: "))
    
    return input_data



input={
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

input_data = {
    'gender': 'Male',
    'SeniorCitizen': 0,
    'Partner': 'No',
    'Dependents': 'No',
    'tenure': 2,
    'PhoneService': 'Yes',
    'MultipleLines': 'No',
    'InternetService': 'DSL',
    'OnlineSecurity': 'Yes',
    'OnlineBackup': 'Yes',
    'DeviceProtection': 'No',
    'TechSupport': 'No',
    'StreamingTV': 'No',
    'StreamingMovies': 'No',
    'Contract': 'Month-to-month',
    'PaperlessBilling': 'Yes',
    'PaymentMethod': 'Mailed check',
    'MonthlyCharges': 53.85,
    'TotalCharges': 108.15,
}


print(predict_churn(input_data))

