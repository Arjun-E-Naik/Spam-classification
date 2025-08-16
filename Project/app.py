

# Streamlit UI
import streamlit as st
import pickle

st.title("📧 Spam Classifier")

# Load the pipeline (vectorizer + model inside)
with open("model_spam.pkl", "rb") as f:
    pipeline = pickle.load(f)

# Input box
user_input = st.text_input("Enter your message:")

if user_input:
    # Directly predict (no need to manually transform)
    prediction = pipeline.predict([user_input])

    # Show result
    st.write(f"Prediction: {'🚨 Spam' if prediction[0] == 0 else '✅ Not Spam'}")
 



