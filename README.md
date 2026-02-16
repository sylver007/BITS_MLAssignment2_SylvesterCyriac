<img width="673" height="204" alt="image" src="https://github.com/user-attachments/assets/28bcbe6d-7c8c-4756-9e5f-569567cd6d79" /># BITS_MLAssignment2_SylvesterCyriac
BITS_MLAssignment2_SylvesterCyriac

Problem statement: The goal of this project is to analyze a bank's marketing campaign data to identify patterns that lead to successful term deposit subscriptions (the deposit column). By building and comparing six different machine learning models, we aim to provide actionable insights for future marketing strategies.

Dataset description:
Source: Bank Marketing Dataset from the UCI Machine Learning Repository.
Size: The dataset contains 17 columns and over 500 instances, meeting the mandatory assignment requirements.
Features: Includes 7 integer, 6 string, and 4 boolean columns covering client demographics (age, job), social-economic attributes, and campaign history.
Target: Binary classification of the deposit column ("yes" or "no").


Models Used
The following 6 models were implemented and evaluated:
Model	              Accuracy	    AUC	          Precision	    Recall	      F1	          MCC
Logistic Regression	0.789968652	  0.866742972	  0.793137255	  0.758200562	  0.775275515	  0.578838523
Decision Tree	      0.768920734	  0.767829039	  0.766183575	  0.743205248	  0.754519505	  0.536562801
kNN	                0.773399015	  0.845134159	  0.787692308	  0.71977507	  0.752203722	  0.54611544
Naive Bayes	        0.746529333	  0.810644776	  0.704156479	  0.809746954	  0.753269398	  0.500392827
Random Forest	      0.828481863	  0.905514893	  0.803191489	  0.849109653	  0.825512528	  0.658102352
XGBoost	            0.842364532	  0.914341198	  0.817777778	  0.862230553	  0.839416058	  0.685760737 

Observations
ML Model Name,        Observation about model performance
Logistic Regression:  Performed well as a baseline but struggled to capture non-linear relationships between features like 'age' and 'balance'.
Decision Tree:        High training accuracy but showed signs of overfitting; the performance dropped on the test set compared to ensemble methods.
kNN:                  Highly sensitive to the scaling of numerical features. After standard scaling, it provided decent local patterns but was computationally slower."
Naive Bayes:          The fastest model to train, though it assumed independence between features (like 'job' and 'education') which may not be entirely true."
Random Forest:        One of the top performers; the ensemble of trees effectively handled the mix of categorical and numerical data in the banking set.
XGBoost:              Likely the best performance in terms of AUC and F1 Score. It handled the class imbalance of the bank dataset better than single-tree models.
