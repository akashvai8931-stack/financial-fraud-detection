# Data

| File | Rows | Used? | Notes |
|---|---|---|---|
| financial_fraud_detection_dataset.csv | 5,000 | Yes (main dataset) | Target: Fraudulent. 482 frauds (9.64%). |
| synthetic_fraud_dataset1.csv | 50,000 | Rejected | No link between any feature and the target (ROC-AUC about 0.51). |
| credit_card_fraud_dataset.csv | 100,000 | Rejected | No usable signal (ROC-AUC about 0.50). |
| Fraud Detection.xlsx | n/a | Rejected | Contains a leaking column and only 68 fraud rows. |

The rejected datasets are kept on purpose. They show why the final dataset was chosen with evidence. The main dataset is synthetic (computer-generated), so results do not show real-world bank performance.
