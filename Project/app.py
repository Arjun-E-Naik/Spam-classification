

# Streamlit UI
import streamlit as st
import pickle
import os

st.title("📧 Spam Classifier")

# Get the absolute path to this script's directory
BASE_DIR = os.path.dirname(__file__)

# Load the pipeline (vectorizer + model inside)
with open(os.path.join(BASE_DIR, "model_spam.pkl"), "rb") as f:
    pipeline = pickle.load(f)

# Input box
user_input = st.text_input("Enter your message:")

if user_input:
    # Directly predict (no need to manually transform)
    prediction = pipeline.predict([user_input])

    # Show result
    st.write(f"Prediction: {'🚨 Spam' if prediction[0] == 0 else '✅ Not Spam'}")

 



