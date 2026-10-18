from pathlib import Path

import joblib
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Financial Fraud Risk Checker", layout="centered")

MODEL_PATH = Path(__file__).parent / "final_model.joblib"
FEATURES = ["Is_Night", "Is_International", "Suspicious_Keyword"]
THRESHOLD = 0.5

# Fraud rate seen in the 5,000-row dataset for each number of risk flags
OBSERVED = {
    0: "0.03% (1 of 3,278 transactions)",
    1: "24.2% (370 of 1,528 transactions)",
    2: "55.6% (104 of 187 transactions)",
    3: "100% (7 of 7 transactions)",
}


@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)


model = load_model()

st.title("Financial Fraud Risk Checker")
st.write(
    "Enter three details of a transaction. The model gives a fraud probability "
    "and tells you if the transaction should be sent for review."
)

hour = st.slider("Hour of the transaction (0 to 23)", 0, 23, 14)
international = st.radio("Is the transaction international?", ["No", "Yes"], horizontal=True)
keyword = st.radio("Was a suspicious keyword present?", ["No", "Yes"], horizontal=True)

is_night = int(hour <= 5)
is_international = int(international == "Yes")
has_keyword = int(keyword == "Yes")

if st.button("Check transaction"):
    x = pd.DataFrame([[is_night, is_international, has_keyword]], columns=FEATURES)
    prob = float(model.predict_proba(x)[0, 1])
    flags = is_night + is_international + has_keyword

    col1, col2 = st.columns(2)
    col1.metric("Fraud probability", f"{prob:.1%}")
    col2.metric("Risk flags", f"{flags} of 3")

    if prob >= THRESHOLD:
        st.error("FLAGGED: send this transaction for review.")
    else:
        st.success("NOT FLAGGED: no risk flag found.")

    st.write(
        f"Night-time (hours 0 to 5): **{'Yes' if is_night else 'No'}**, "
        f"International: **{international}**, Suspicious keyword: **{keyword}**"
    )
    st.caption(f"In the full 5,000-row dataset, transactions with {flags} risk flag(s) had a fraud rate of {OBSERVED[flags]}.")

with st.expander("About this model and its limits"):
    st.write(
        "Model: Logistic Regression (balanced class weights) on three features. "
        "Threshold: 0.5."
    )
    st.table(
        pd.DataFrame(
            {
                "Test-set measure (1,250 transactions)": ["ROC-AUC", "PR-AUC", "Recall", "Precision", "F1 score"],
                "Value": ["0.907", "0.453", "1.00", "0.27", "0.43"],
            }
        )
    )
    st.write(
        "- The model catches almost every fraud, but about three of four alerts are false alarms.\n"
        "- The dataset is synthetic, so these results do not show real-world performance.\n"
        "- At threshold 0.5 the model works like the rule: flag a transaction if it has at least one risk flag.\n"
        "- This app is a portfolio demo and must not be used for real decisions."
    )

st.caption("Built by Akash Vaishnav, Data Science Intern, Zidio Development.")
