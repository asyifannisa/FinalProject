import streamlit as st
import streamlit.components.v1 as stc

import sys
from custom_transformers import DropColumns  # class yang sama seperti saat training
# registrasi ke modul yang sedang berjalan (= __main__ / app.py)
setattr(sys.modules[__name__], "DropColumns", DropColumns)
# pastikan alias __main__ menunjuk ke modul ini juga (aman di Streamlit)
sys.modules["__main__"] = sys.modules[__name__]

from prediction_app import run_prediction_app 

html_temp = """
            <div style="
            background: linear-gradient(90deg, #3d8d92, #36e0eb, #3b367c);
            padding: 14px;
            border-radius: 12px;
            margin-bottom: 10px;
            font-family: Arial, sans-serif;
            color: white;
            text-align: center;
            ">
            <h1 style="margin: 0;">Delivery Processing Time Predictor</h1>
            <p style="margin: 4px 0 0;">Porter Ops • ETA &amp; Ops Intelligence</p>
            </div>
            """
desc_temp = """
            ### Delivery Porter Predictor
            This app will be used by the Operation team to predict the delivery processing time to give better service for customers.
            #### Data Source
            - https://www.kaggle.com/datasets/ranitsarkar01/porter-delivery-time-estimation/data
            #### App Content
            - Home
            - Prediction Section
            """
def main():
    st.set_page_config(page_title="Porter Delivery Time Predictor", page_icon="⏱️", layout="wide")
    stc.html(html_temp)
    
    menu = ['Home', 'Prediction']
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == 'Home':
        st.subheader("Go Predict Processing Time for Better Operational 🚀")
        st.markdown(desc_temp)
        with st.expander("How to use this Machine"):
            st.markdown("""
            1) Open tab **Prediction**  
            2) Input your data (form)  
            3) Click **Predict** → results in **minutes** + interpretation
            """)
    elif choice == "Prediction":
        # st.subheader("Welcome to Our Prediction Machine")
        run_prediction_app()


if __name__ == '__main__':
    main()
