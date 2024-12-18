import streamlit as st
from security import check_password, check_api_key
from layout import create_header, set_background, emptylines, hide_st
from form_handler import handle_form_submission

# Set up layout and background
hide_st()
create_header()
set_background()
emptylines()

# Initialize session state
if "password_verified" not in st.session_state:
    st.session_state.password_verified = False

if "api_key_verified" not in st.session_state:
    st.session_state.api_key_verified = False

if "form_submitted" not in st.session_state:
    st.session_state.form_submitted = False

# Callback for password verification
def verify_password():
    password = st.session_state.password_input
    if check_password(password):
        st.session_state.password_verified = True
        st.success("Password verified!")
    else:
        st.error("Invalid password!")

# Callback for API key verification
def verify_api_key():
    api_key = st.session_state.api_key_input
    if check_api_key(api_key):
        st.session_state.api_key_verified = True
        st.session_state.api_key = api_key  # Store the verified API key
        st.success("API key verified!")
    else:
        st.error("Invalid API key! Make sure there are no spaces before or after the API key.")

# Password input section
if not st.session_state.password_verified:
    st.title("Login")
    password = st.text_input("Enter password", type="password", key="password_input")
    st.button("Submit Password", on_click=verify_password)

# API key input section
if st.session_state.password_verified and not st.session_state.api_key_verified:
    st.title("API Key Verification")
    api_key = st.text_input("Enter API key", type="password", key="api_key_input")
    st.button("Submit API Key", on_click=verify_api_key)

# Main form submission section
if st.session_state.password_verified and st.session_state.api_key_verified:
    if "api_key" in st.session_state:
        update_logs = st.expander(":construction: Update Logs")
        update_logs.markdown("""
* 30.10.2024 | v1.0 launch
* 04.11.2024 | v1.1 - Added L4 Asset options in the form.
* 20.11.2024 | v1.1.1 - Optimized Login process with callback functions
""")
        st.markdown("---")
        handle_form_submission()
    else:
        st.error("API key is missing. Please re-enter the API key.")
