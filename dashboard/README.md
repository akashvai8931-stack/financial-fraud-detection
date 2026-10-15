# Dashboard

Power BI dashboard for the financial fraud detection project (`fraud_dashboard.pbix`). It uses `dashboard_data.csv` (5,000 rows, 22 columns) from the main folder.

| Page | Rows used | What it shows |
|---|---|---|
| Introduction | n/a | Title, dataset and final model |
| Fraud Overview | All 5,000 | Nine number cards, and fraud rate by time of day, suspicious keyword, risk flags, international status and month |
| Model Performance | Test set only (1,250) | Confusion matrix, recall, precision and alerts per fraud caught |
| Features That Do Not Matter | All 5,000 | Fraud rate by location, payment method, device type and merchant category |

Open the file with Power BI Desktop (Windows). If Power BI cannot find the data, go to Transform data, then Data source settings, and point it to your copy of `dashboard_data.csv`.
