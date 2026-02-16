import streamlit as st
import pandas as pd
import pickle
from sklearn.metrics import confusion_matrix, classification_report
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Banking Campaign Classification App")

# Step 1: Dataset Upload
uploaded_file = st.file_uploader("Upload your test CSV data", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file, sep=None, engine='python')
    st.write("Data Preview:", df.head())

    # Step 2: Model Selection Dropdown
    model_option = st.selectbox(
        'Which model would you like to use?',
        ('logistic_regression', 'decision_tree', 'knn', 'naive_bayes', 'random_forest', 'xgboost')
    )

    if st.button('Run Prediction and Evaluation'):
        # Load the selected model and the scaler
        with open(f'model/{model_option}.pkl', 'rb') as f:
            model = pickle.load(f)
        with open('model/scaler.pkl', 'rb') as f:
            scaler = pickle.load(f)

        # Basic Preprocessing (Match the training steps)
        # Note: In a real app, you'd handle LabelEncoding here too
        # For the assignment, we assume the uploaded test data matches the format
        
 

# 1. Preprocessing (Must match your training script)
        # We need to encode the 'deposit' column if it's in the test data
        target_col = 'deposit'
        if target_col in df.columns:
            y_true = df[target_col].map({'yes': 1, 'no': 0})
            X_test = df.drop(target_col, axis=1)
        else:
            st.error("Test data must contain a 'deposit' column for evaluation.")
            st.stop()

        # Handle Categorical variables in X_test
        from sklearn.preprocessing import LabelEncoder
        le = LabelEncoder()
        for col in X_test.columns:
            if X_test[col].dtype == 'object' or X_test[col].dtype == 'bool':
                X_test[col] = le.fit_transform(X_test[col].astype(str))

        # Scale data for specific models
        if model_option in ['logistic_regression', 'knn', 'naive_bayes']:
            X_test = scaler.transform(X_test)

        # 2. Run Prediction
        y_pred = model.predict(X_test)

        # 3. Display Metrics
        st.subheader(f"Evaluation Metrics for {model_option}")
        report = classification_report(y_true, y_pred, output_dict=True)
        
        # Display as a clean table
        metrics_df = pd.DataFrame(report).transpose()
        st.table(metrics_df.iloc[:-3, :4]) # Show Precision, Recall, F1

        # 4. Confusion Matrix
        st.subheader("Confusion Matrix")
        cm = confusion_matrix(y_true, y_pred)
        fig, ax = plt.subplots()
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=ax)
        ax.set_xlabel('Predicted')
        ax.set_ylabel('Actual')
        st.pyplot(fig)