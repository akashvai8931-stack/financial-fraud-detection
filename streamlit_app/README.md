# Streamlit app

A small web app to try the final model (`app.py`). You choose the hour, whether the transaction is international and whether a suspicious keyword was present. The app shows the fraud probability, the number of risk flags and whether the transaction would be flagged for review.

`final_model.joblib` here is a copy of the model in the main folder, because the app loads it from its own folder. The colours are set in `.streamlit/config.toml` in the main folder.

This is a portfolio demo on synthetic data. It must not be used for real decisions.
