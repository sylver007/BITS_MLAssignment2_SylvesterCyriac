# BITS_MLAssignment2_SylvesterCyriac
BITS_MLAssignment2_SylvesterCyriac

ML Model Name,Observation about model performance
Logistic Regression,Performed well as a baseline but struggled to capture non-linear relationships between features like 'age' and 'balance'.
Decision Tree,High training accuracy but showed signs of overfitting; the performance dropped on the test set compared to ensemble methods.
kNN,"Highly sensitive to the scaling of numerical features. After standard scaling, it provided decent local patterns but was computationally slower."
Naive Bayes,"The fastest model to train, though it assumed independence between features (like 'job' and 'education') which may not be entirely true."
Random Forest,One of the top performers; the ensemble of trees effectively handled the mix of categorical and numerical data in the banking set.
XGBoost,Likely the best performance in terms of AUC and F1 Score. It handled the class imbalance of the bank dataset better than single-tree models.
