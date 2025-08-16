import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
import pickle



with open('model.pkl', 'rb') as f:
    model = pickle.load(f)


st.title('Spam classifier')
import streamlit as st

placeholder = st.empty()

if st.button("Revive Box"):
    with placeholder.container():
        st.text_input("Enter something:")



