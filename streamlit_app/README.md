# Streamlit app

**Live app:** [Financial Fraud Risk Checker](https://financial-fraud-risk-checker.streamlit.app/)

A small web app to try the final model (`app.py`). You choose the hour, whether the transaction is international and whether a suspicious keyword was present. The app shows the fraud probability, the number of risk flags and whether the transaction would be flagged for review.

## Files in this folder

- `app.py`: the Streamlit app.
- `final_model.joblib`: a copy of the final model. The app loads it from its own folder.
- `requirements.txt`: the Python packages that the app needs.

## About the model

The model is a Logistic Regression with balanced class weights. It uses three risk flags: night-time (hours 0 to 5), international transaction and suspicious keyword. On the test set of 1,250 transactions it reached ROC-AUC 0.907 and caught all 120 frauds, but about three of every four alerts are false alarms.

## Run the app on your own computer

1. Install the packages: `pip install -r requirements.txt`
2. Start the app from this folder: `streamlit run app.py`

Built by Akash Vaishnav, Data Science Intern, Zidio Development.
