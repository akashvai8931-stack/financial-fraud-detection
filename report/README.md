# Report

`Fraud_Detection_Final_Report_with_Streamlit.pdf` is the final project report (22 pages). It covers the dataset choice, cleaning, exploratory analysis, model comparison, threshold choice, the Power BI dashboard, limitations and future work. Appendix B describes the live Streamlit app.

Main result (test set, 1,250 transactions): ROC-AUC 0.907, recall 1.00, precision 0.27. The model catches every fraud but raises many false alarms. The limit comes from the data, which is synthetic and has only three useful signals.

**Live app:** [Financial Fraud Risk Checker](https://financial-fraud-risk-checker.streamlit.app/)
