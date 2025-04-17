# -*- coding: utf-8 -*-
import numpy as np
import pickle
import pandas as pd
import streamlit as st 
from PIL import Image

# Load the model from the full path
pickle_in = open("classifier.pkl", "rb")
classifier = pickle.load(pickle_in)

# Prediction function
def predict_note_authentication(variance, skewness, curtosis, entropy):
    prediction = classifier.predict([[float(variance), float(skewness), float(curtosis), float(entropy)]])
    return prediction[0]

# Streamlit main function
def main():
    st.title("Bank Authenticator")

    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Bank Authenticator ML App</h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    variance = st.text_input("Variance", "Type Here")
    skewness = st.text_input("Skewness", "Type Here")
    curtosis = st.text_input("Curtosis", "Type Here")
    entropy = st.text_input("Entropy", "Type Here")

    result = ""
    if st.button("Predict"):
        try:
            result = predict_note_authentication(variance, skewness, curtosis, entropy)
            st.success(f"The output is {result}")
        except Exception as e:
            st.error(f"Error: {e}")

    if st.button("About"):
        st.text("Let's Learn")
        st.text("Built with Streamlit")

if __name__ == '__main__':
    main()
