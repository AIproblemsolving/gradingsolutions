import streamlit as st

def create_header():
    st.markdown("""
        <style>
        .header {
            background-color: #0D1824;
            padding: 20px;
            text-align: center;
            color: white;
            font-size: 64px;
            font-weight: bold;
            width: 100vw;
            position: fixed;
            top: 0;
            left: 0;
            z-index: 1000;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            margin-top: 15px; /* Tiny space above the text */
        }
        .stApp {
            padding-top: 80px;
        }
        </style>
        <div class="header">
            Grading Assistant (Stable Version)
        </div>
        """, unsafe_allow_html=True)

def set_background():
    st.markdown("""
        <style>
        .stApp {
            background-color: #1D2B3A;
        }
        </style>
        """, unsafe_allow_html=True)


def emptylines():
    st.write("")
    st.write("")
    st.write("")
