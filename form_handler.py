import streamlit as st
import requests
import numpy as np
from security import get_api_key_user


def handle_form_submission():

    # Dropdown menu options
    menu_options = ["Choose Level to Grade", 
                    "Level 1", 
                    "Level 1.5", 
                    "Level 2", 
                    "Level 3", 
                    "Level 4", 
                    "Level 5", 
                    "Level 6"]

    # Motivation messages should be a 1D array or list
    motiv_messages = np.array([
        "Na",
        "PROCEED TO BUILDING YOUR TPIs",
        "PROVIDE PROOF OF PASSING L2 TO GET L3 ROLE",
        "PROVIDE PROOF OF PASSING L1.5 TO GET L3 ROLE",
        "PROCEED TO THE INFAMOUS VALLEY OF DESPAIR",
        "PROCEED TO BUILDING YOUR SOPS",
        "PROVE YOUR WORTH!",
        "Na"
    ])

    # Get Grader
    grader = get_api_key_user(st.session_state.api_key)

    # Dropdown to select the level
    selected_option = st.selectbox("Choose Level to Grade", menu_options, key="selected_option")

    # Get the index of the selected option
    current_index = menu_options.index(selected_option)

    # Get the motivation message based on the selected level
    motiv_message = motiv_messages[current_index]

    # Determine the next level (if the current index is not the last one)
    next_level = None
    if current_index < len(menu_options) - 1:
        next_level = menu_options[current_index + 1]
    else:
        next_level = "IM Role"  # if it's the last item

    if not (selected_option == "Choose Level to Grade"):
    
        # Form for Student ID, Attempt, Result, and Timeout
        with st.form(key="submission_form"):
            student_id = st.text_input("Student ID", value="", key="student_id")
            attempt = st.number_input("Attempt", min_value=1, step=1, key="attempt")
            
            # Mimicking horizontal sliders with radio buttons
            result = st.radio(
                "Result",
                options=["PASS", "FAIL", "NUKE"],
                horizontal=True,
                key="result"
            )
            
            timeout = st.radio(
                "Timeout",
                options=["None", "24H", "48H", "72H"],
                horizontal=True,
                key="timeout"
            )
            
            # Submit button for the form
            submit_button = st.form_submit_button("Submit")
    
            if submit_button:
                if selected_option == "Choose Level to Grade":
                    st.warning("Which Level are you Grading?")
                    st.stop()
                
                if not student_id or attempt < 1 or not result or not timeout:
                    st.warning("All fields must be filled out. Please check your inputs.")
                    st.stop()
    
            if submit_button:
                if result == "PASS":
                    timeout = "None"
    
                data = {
                    'grader' : grader,
                    'level': selected_option,
                    'id': student_id,
                    'attempt': attempt,
                    'result': result,
                    'timeout': timeout
                }
                
                # Send data to API
                url = f'https://script.google.com/macros/s/{st.session_state.api_key}/exec'
                response = requests.post(url, json=data)
    
                if response.status_code == 200:
                    st.session_state.form_submitted = True
                    st.success('Data sent successfully!')
    
                    if result in ["FAIL", "NUKE"]:
                        message = f"""
    <@{student_id}>
    **UID:** {student_id}  
    **Attempt:** {attempt}  
    **Result:** **{result}**  
    **Timeout:** {timeout}  
    
    **Feedback:** 
    -> 
    
    ***Keep in mind once we identify an issue we stop the grading there and don't go any further not to waste our time. So double check everything is good before resub!***
    """
                        st.code(message, language='markdown')
                    elif result == "PASS":
                        message = f"""
    <@{student_id}>
    **UID:** {student_id}  
    **Attempt:** {attempt}  
    **Result:** **{result}**  
    
    **Feedback:** 
    -> 
    
    **🔥🔥🔥 {next_level} IS YOURS 🔥🔥🔥**
    {motiv_message}
    """
                        st.code(message, language='markdown')
                else:
                    st.error(f'Failed to send data: {response.status_code} - {response.text}')
    
        # Show a message that the form was submitted successfully
        if st.session_state.form_submitted:
            st.success("Form has been successfully submitted and the data has been sent!")
