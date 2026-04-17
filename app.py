import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load saved artifacts
model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")
columns = joblib.load("columns.pkl")

# Custom CSS for white background and black text
st.markdown("""
    <style>
    body, .stApp {
        background-color: #FFFFFF;
        color: #000000;
    }
    h1, h2, h3, h4, h5, h6, p, label {
        color: #000000 !important;
    }
    .stButton>button {
        background: linear-gradient(90deg, #0066ff, #00ccff);
        color: white;
        border-radius: 10px;
        border: none;
        font-weight: bold;
        animation: glow 1.5s infinite alternate;
    }
    @keyframes glow {
        from { box-shadow: 0 0 5px #00ccff; }
        to { box-shadow: 0 0 20px #0066ff; }
    }
    .prediction-box {
        padding: 15px;
        border-radius: 10px;
        text-align: center;
        font-size: 20px;
        font-weight: bold;
        margin-top: 20px;
    }
    .normal {
        background-color: #e6f7ff;
        color: #0066cc;
        animation: fadeIn 2s;
    }
    .attack {
        background-color: #ffe6e6;
        color: #cc0000;
        animation: fadeIn 2s;
    }
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1 style='text-align:center; animation: fadeIn 3s;'>🔒 Network Intrusion Detection System</h1>", unsafe_allow_html=True)
st.write("Detect malicious network traffic (intrusions/attacks) using Machine Learning.")

# Sidebar for user input
st.sidebar.header("Input Network Traffic Features")

def user_input_features():
    data = {}
    for col in columns:
        data[col] = st.sidebar.number_input(f"{col}", value=0.0)
    features = pd.DataFrame(data, index=[0])
    return features

input_df = user_input_features()

# Predict button
if st.button("🔮 Predict"):
    # Scale input
    scaled_input = scaler.transform(input_df)

    # Prediction
    prediction = model.predict(scaled_input)
    prediction_proba = model.predict_proba(scaled_input)

    # Display prediction with styled box
    if prediction[0] == 0:
        st.markdown("<div class='prediction-box normal'>🟢 Normal Traffic Detected</div>", unsafe_allow_html=True)
    else:
        st.markdown("<div class='prediction-box attack'>🔴 Malicious Attack Detected</div>", unsafe_allow_html=True)

    # Probability scores
    st.subheader("Prediction Probability")
    st.write(f"Normal: {prediction_proba[0][0]:.4f}, Attack: {prediction_proba[0][1]:.4f}")

# Batch prediction
st.subheader("Batch Prediction")
uploaded_file = st.file_uploader("Upload CSV file with traffic data", type=["csv"])
if uploaded_file is not None and st.button("📂 Predict Batch"):
    batch_df = pd.read_csv(uploaded_file)
    batch_df = batch_df[columns]  # ensure correct column order
    batch_scaled = scaler.transform(batch_df)
    batch_pred = model.predict(batch_scaled)
    batch_df["Prediction"] = ["Attack" if p == 1 else "Normal" for p in batch_pred]
    st.write(batch_df.head())
    st.download_button("Download Predictions", batch_df.to_csv(index=False), "predictions.csv")

# Feature importance visualization
st.subheader("Top Features")
importances = model.feature_importances_
feat_imp = pd.Series(importances, index=columns)
st.bar_chart(feat_imp.nlargest(15))







# import streamlit as st
# import pandas as pd
# import numpy as np
# import joblib

# # Load saved artifacts
# model = joblib.load("model.pkl")
# scaler = joblib.load("scaler.pkl")
# columns = joblib.load("columns.pkl")

# # Custom CSS for white background and black text
# st.markdown("""
#     <style>
#     body, .stApp {
#         background-color: #FFFFFF;
#         color: #000000;
#     }
#     h1, h2, h3, h4, h5, h6, p, label, .css-1offfwp, .css-10trblm {
#         color: #000000 !important;
#     }
#     .stButton>button {
#         background: linear-gradient(90deg, #0066ff, #00ccff);
#         color: white;
#         border-radius: 10px;
#         border: none;
#         font-weight: bold;
#         animation: glow 1.5s infinite alternate;
#     }
#     @keyframes glow {
#         from { box-shadow: 0 0 5px #00ccff; }
#         to { box-shadow: 0 0 20px #0066ff; }
#     }
#     .prediction-box {
#         padding: 15px;
#         border-radius: 10px;
#         text-align: center;
#         font-size: 20px;
#         font-weight: bold;
#         margin-top: 20px;
#     }
#     .normal {
#         background-color: #e6f7ff;
#         color: #0066cc;
#         animation: fadeIn 2s;
#     }
#     .attack {
#         background-color: #ffe6e6;
#         color: #cc0000;
#         animation: fadeIn 2s;
#     }
#     @keyframes fadeIn {
#         from { opacity: 0; }
#         to { opacity: 1; }
#     }
#     </style>
# """, unsafe_allow_html=True)

# # Title with animation
# st.markdown("<h1 style='text-align:center; animation: fadeIn 3s;'>🔒 Network Intrusion Detection System</h1>", unsafe_allow_html=True)
# st.write("Detect malicious network traffic (intrusions/attacks) using Machine Learning.")

# # Sidebar for user input
# st.sidebar.header("Input Network Traffic Features")

# def user_input_features():
#     data = {}
#     for col in columns:
#         data[col] = st.sidebar.number_input(f"{col}", value=0.0)
#     features = pd.DataFrame(data, index=[0])
#     return features

# input_df = user_input_features()

# # Scale input
# scaled_input = scaler.transform(input_df)

# # Prediction
# prediction = model.predict(scaled_input)
# prediction_proba = model.predict_proba(scaled_input)

# # Display prediction with styled box
# if prediction[0] == 0:
#     st.markdown("<div class='prediction-box normal'>🟢 Normal Traffic Detected</div>", unsafe_allow_html=True)
# else:
#     st.markdown("<div class='prediction-box attack'>🔴 Malicious Attack Detected</div>", unsafe_allow_html=True)

# # Probability scores
# st.subheader("Prediction Probability")
# st.write(f"Normal: {prediction_proba[0][0]:.4f}, Attack: {prediction_proba[0][1]:.4f}")

# # Batch prediction
# st.subheader("Batch Prediction")
# uploaded_file = st.file_uploader("Upload CSV file with traffic data", type=["csv"])
# if uploaded_file is not None:
#     batch_df = pd.read_csv(uploaded_file)
#     batch_df = batch_df[columns]  # ensure correct column order
#     batch_scaled = scaler.transform(batch_df)
#     batch_pred = model.predict(batch_scaled)
#     batch_df["Prediction"] = ["Attack" if p == 1 else "Normal" for p in batch_pred]
#     st.write(batch_df.head())
#     st.download_button("Download Predictions", batch_df.to_csv(index=False), "predictions.csv")

# # Feature importance visualization
# st.subheader("Top Features")
# importances = model.feature_importances_
# feat_imp = pd.Series(importances, index=columns)
# st.bar_chart(feat_imp.nlargest(15))









# # import streamlit as st
# # import pandas as pd
# # import numpy as np
# # import joblib

# # # Load saved artifacts
# # model = joblib.load("model.pkl")
# # scaler = joblib.load("scaler.pkl")
# # columns = joblib.load("columns.pkl")

# # # Custom CSS for full black theme and animations
# # st.markdown("""
# #     <style>
# #     body, .stApp {
# #         background-color: #000000;
# #         color: #FFFFFF;
# #     }
# #     h1, h2, h3, h4, h5, h6, p, label, .css-1offfwp, .css-10trblm {
# #         color: #FFFFFF !important;
# #     }
# #     .stButton>button {
# #         background: linear-gradient(90deg, #ff0000, #ff6600);
# #         color: white;
# #         border-radius: 10px;
# #         border: none;
# #         font-weight: bold;
# #         animation: glow 1.5s infinite alternate;
# #     }
# #     @keyframes glow {
# #         from { box-shadow: 0 0 5px #ff6600; }
# #         to { box-shadow: 0 0 20px #ff0000; }
# #     }
# #     .prediction-box {
# #         padding: 15px;
# #         border-radius: 10px;
# #         text-align: center;
# #         font-size: 20px;
# #         font-weight: bold;
# #         margin-top: 20px;
# #     }
# #     .normal {
# #         background-color: #004d00;
# #         color: #00ff00;
# #         animation: fadeIn 2s;
# #     }
# #     .attack {
# #         background-color: #4d0000;
# #         color: #ff3333;
# #         animation: fadeIn 2s;
# #     }
# #     @keyframes fadeIn {
# #         from { opacity: 0; }
# #         to { opacity: 1; }
# #     }
# #     </style>
# # """, unsafe_allow_html=True)

# # # Title with animation
# # st.markdown("<h1 style='text-align:center; animation: fadeIn 3s;'>🔒 Network Intrusion Detection System</h1>", unsafe_allow_html=True)
# # st.write("Detect malicious network traffic (intrusions/attacks) using Machine Learning.")

# # # Sidebar for user input
# # st.sidebar.header("Input Network Traffic Features")

# # def user_input_features():
# #     data = {}
# #     for col in columns:
# #         data[col] = st.sidebar.number_input(f"{col}", value=0.0)
# #     features = pd.DataFrame(data, index=[0])
# #     return features

# # input_df = user_input_features()

# # # Scale input
# # scaled_input = scaler.transform(input_df)

# # # Prediction
# # prediction = model.predict(scaled_input)
# # prediction_proba = model.predict_proba(scaled_input)

# # # Display prediction with styled box
# # if prediction[0] == 0:
# #     st.markdown("<div class='prediction-box normal'>🟢 Normal Traffic Detected</div>", unsafe_allow_html=True)
# # else:
# #     st.markdown("<div class='prediction-box attack'>🔴 Malicious Attack Detected</div>", unsafe_allow_html=True)

# # # Probability scores
# # st.subheader("Prediction Probability")
# # st.write(f"Normal: {prediction_proba[0][0]:.4f}, Attack: {prediction_proba[0][1]:.4f}")

# # # Batch prediction
# # st.subheader("Batch Prediction")
# # uploaded_file = st.file_uploader("Upload CSV file with traffic data", type=["csv"])
# # if uploaded_file is not None:
# #     batch_df = pd.read_csv(uploaded_file)
# #     batch_df = batch_df[columns]  # ensure correct column order
# #     batch_scaled = scaler.transform(batch_df)
# #     batch_pred = model.predict(batch_scaled)
# #     batch_df["Prediction"] = ["Attack" if p == 1 else "Normal" for p in batch_pred]
# #     st.write(batch_df.head())
# #     st.download_button("Download Predictions", batch_df.to_csv(index=False), "predictions.csv")

# # # Feature importance visualization
# # st.subheader("Top Features")
# # importances = model.feature_importances_
# # feat_imp = pd.Series(importances, index=columns)
# # st.bar_chart(feat_imp.nlargest(15))






# # # import streamlit as st
# # # import pandas as pd
# # # import numpy as np
# # # import joblib

# # # # Load saved artifacts
# # # model = joblib.load("model.pkl")
# # # scaler = joblib.load("scaler.pkl")
# # # columns = joblib.load("columns.pkl")

# # # # Custom CSS for dark theme and animations
# # # st.markdown("""
# # #     <style>
# # #     body {
# # #         background-color: black;
# # #         color: white;
# # #     }
# # #     .stApp {
# # #         background-color: black;
# # #         color: white;
# # #     }
# # #     h1, h2, h3, h4, h5, h6, p, label {
# # #         color: white !important;
# # #     }
# # #     .stButton>button {
# # #         background: linear-gradient(90deg, #ff0000, #ff6600);
# # #         color: white;
# # #         border-radius: 10px;
# # #         animation: glow 1.5s infinite alternate;
# # #     }
# # #     @keyframes glow {
# # #         from { box-shadow: 0 0 5px #ff6600; }
# # #         to { box-shadow: 0 0 20px #ff0000; }
# # #     }
# # #     </style>
# # # """, unsafe_allow_html=True)

# # # # Title with animation
# # # st.markdown("<h1 style='text-align:center; animation: fadeIn 3s;'>🔒 Network Intrusion Detection System</h1>", unsafe_allow_html=True)

# # # st.write("Detect malicious network traffic (intrusions/attacks) using Machine Learning.")

# # # # Sidebar for user input
# # # st.sidebar.header("Input Network Traffic Features")

# # # def user_input_features():
# # #     data = {}
# # #     for col in columns:
# # #         data[col] = st.sidebar.number_input(f"{col}", value=0.0)
# # #     features = pd.DataFrame(data, index=[0])
# # #     return features

# # # input_df = user_input_features()

# # # # Scale input
# # # scaled_input = scaler.transform(input_df)

# # # # Prediction
# # # prediction = model.predict(scaled_input)
# # # prediction_proba = model.predict_proba(scaled_input)

# # # st.subheader("Prediction")
# # # st.write("🟢 Normal" if prediction[0] == 0 else "🔴 Attack")

# # # st.subheader("Prediction Probability")
# # # st.write(f"Normal: {prediction_proba[0][0]:.4f}, Attack: {prediction_proba[0][1]:.4f}")

# # # # Batch prediction
# # # st.subheader("Batch Prediction")
# # # uploaded_file = st.file_uploader("Upload CSV file with traffic data", type=["csv"])
# # # if uploaded_file is not None:
# # #     batch_df = pd.read_csv(uploaded_file)
# # #     batch_df = batch_df[columns]  # ensure correct column order
# # #     batch_scaled = scaler.transform(batch_df)
# # #     batch_pred = model.predict(batch_scaled)
# # #     batch_df["Prediction"] = ["Attack" if p == 1 else "Normal" for p in batch_pred]
# # #     st.write(batch_df.head())
# # #     st.download_button("Download Predictions", batch_df.to_csv(index=False), "predictions.csv")

# # # # Feature importance visualization
# # # st.subheader("Top Features")
# # # importances = model.feature_importances_
# # # feat_imp = pd.Series(importances, index=columns)
# # # st.bar_chart(feat_imp.nlargest(15))









# # # # import streamlit as st
# # # # import pandas as pd
# # # # import joblib
# # # # from xgboost import XGBClassifier

# # # # # Load model
# # # # model = XGBClassifier()
# # # # model.load_model("model.json")

# # # # columns = joblib.load("columns.pkl")

# # # # try:
# # # #     encoders = joblib.load("encoders.pkl")
# # # # except:
# # # #     encoders = None

# # # # st.title("🔐 Network Intrusion Detection System")

# # # # uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

# # # # if uploaded_file:
# # # #     df = pd.read_csv(uploaded_file)

# # # #     # Drop target if exists
# # # #     for col in ["label", "attack", "target"]:
# # # #         if col in df.columns:
# # # #             df.drop(col, axis=1, inplace=True)

# # # #     # Fix columns
# # # #     for col in columns:
# # # #         if col not in df.columns:
# # # #             df[col] = 0

# # # #     df = df[columns]

# # # #     # Encoding
# # # #     if encoders:
# # # #         for col in df.select_dtypes(include='object').columns:
# # # #             if col in encoders:
# # # #                 try:
# # # #                     df[col] = encoders[col].transform(df[col].astype(str))
# # # #                 except:
# # # #                     df[col] = 0

# # # #     if st.button("Predict"):
# # # #         pred = model.predict(df)

# # # #         st.write("Prediction:", pred[:10])