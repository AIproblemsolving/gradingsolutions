import streamlit as st
from security import check_password, check_api_key
from layout import create_header, set_background, emptylines, hide_st
from form_handler import handle_form_submission

# Set up layout and background
hide_st()
create_header()
set_background()
emptylines()
st.markdown("---")

# Initial session state setup
if "password_verified" not in st.session_state:
    st.session_state.password_verified = False

if "api_key_verified" not in st.session_state:
    st.session_state.api_key_verified = False

if "show_password_success" not in st.session_state:
    st.session_state.show_password_success = False

if "show_api_key_success" not in st.session_state:
    st.session_state.show_api_key_success = False

# Initialize form submission state
if "form_submitted" not in st.session_state:
    st.session_state.form_submitted = False

# Password input section
if not st.session_state.password_verified:
    st.title("Login")
    password = st.text_input("Enter password", type="password", key="password_input")

    if st.button("Submit Password"):
        if check_password(password):
            st.session_state.password_verified = True
            st.session_state.show_password_success = True
        else:
            st.error("Invalid password!")

# Show password success message if needed
if st.session_state.show_password_success:
    st.success("Password verified!")
    # Reset the success message after it is shown
    st.session_state.show_password_success = False

# API key input section
if st.session_state.password_verified and not st.session_state.api_key_verified:
    st.title("API Key Verification")
    api_key = st.text_input("Enter API key", type="password", key="api_key_input")

    if st.button("Submit API Key"):
        if check_api_key(api_key):
            st.session_state.api_key_verified = True
            st.session_state.api_key = api_key  # Store the verified API key
            st.session_state.show_api_key_success = True
        else:
            st.error("Invalid API key!")

# Show API key success message if needed
if st.session_state.show_api_key_success:
    st.success("API key verified!")
    # Reset the success message after it is shown
    st.session_state.show_api_key_success = False

# Handle form submission when both password and API key are verified
if st.session_state.password_verified and st.session_state.api_key_verified:
    if "api_key" in st.session_state:
        handle_form_submission()
    else:
        st.error("API key is missing. Please re-enter the API key.")
