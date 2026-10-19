# Financial Fraud Detection: Risk-Flag Model, Power BI Dashboard and Streamlit App

**Live app:** [Financial Fraud Risk Checker](https://financial-fraud-risk-checker.streamlit.app/)

A model that flags fraudulent card and online transactions, with a Power BI dashboard for a business reader and a Streamlit app for live testing. This is an internship and portfolio project (Zidio Development) by Akash Vaishnav.

## Result (test set, 1,250 transactions)

| Measure | Value |
|---|---|
| ROC-AUC | 0.907 |
| PR-AUC | 0.453 |
| Recall (fraud class) | 1.00 (120 of 120 frauds caught) |
| Precision (fraud class) | 0.27 |
| F1 score | 0.43 |
| Alerts per fraud caught | 3.7 (444 alerts, 324 false alarms) |

The model catches every fraud in the test set, but about three of every four alerts are false alarms. This limit comes from the data, not from the algorithm.

## What was done

- Tested four datasets and rejected three of them (no usable pattern, or a leaking column). See `data/README.md`.
- Cleaned the main dataset (5,000 transactions, 9.64% fraud) and created features.
- Found that only three features carry a signal: a suspicious keyword, an international transaction, and a night-time transaction (hours 0 to 5).
- Compared Logistic Regression, Random Forest and XGBoost. They scored the same, so the simplest model was chosen: Logistic Regression with balanced class weights on the three risk flags.
- Handled class imbalance, chose a decision threshold, and explained the business trade-off.
- Built a Power BI dashboard (4 pages).

## Honest limits

- **Low precision (27%):** analysts would need to review 3.7 alerts to find one fraud.
- **Synthetic data:** the patterns are probably simple rules built into the data generator. Real fraud is more complex, so these numbers do not predict real-world performance.
- **Mild data snooping:** the three flags and the night cutoff were chosen after looking at the full dataset, including the test rows. The test result is slightly optimistic.
- **The model is close to a simple rule:** at threshold 0.5 it flags a transaction if it has at least one risk flag.
- **Small test set:** only 120 frauds, so every test metric is uncertain.
- **Random split:** a split by time was not tested.
- **Assumed costs:** the threshold assumes a missed fraud costs more than a false alarm. Real costs were not available.

## Repository structure

```
01_fraud_detection.ipynb   full analysis and modelling notebook
final_model.joblib         saved final model (scikit-learn pipeline)
dashboard_data.csv         data exported for Power BI
requirements.txt           Python packages
data/                      datasets and notes on which were used or rejected
dashboard/                 Power BI file (fraud_dashboard.pbix) and page guide
report/                    final project report (PDF)
```

## How to run

1. Install the packages: `pip install -r requirements.txt`
2. Open `01_fraud_detection.ipynb` in JupyterLab and run the cells from top to bottom. If the notebook cannot find a data file, change the file path in the first cells to where you saved the `data` folder.
3. Open `dashboard/fraud_dashboard.pbix` with Power BI Desktop (Windows).

## Report

The full report (22 pages, with an appendix about the Streamlit app) is in [report/Fraud_Detection_Final_Report_with_Streamlit.pdf](report/Fraud_Detection_Final_Report_with_Streamlit.pdf).
