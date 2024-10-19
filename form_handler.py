import streamlit as st
import requests

def handle_form_submission():
    st.success("Both password and API key have been successfully verified!")
    
    # Dropdown menu options
    menu_options = ["Level 1", "Level 1.5", "Level 2", "Level 3", "Level 4", "Level 5", "Level 6"]
    selected_option = st.selectbox("Choose an option", menu_options, key="selected_option")

    # Get the index of the selected option
    current_index = menu_options.index(selected_option)
    
    # Determine the next level (if the current index is not the last one)
    next_level = None
    if current_index < len(menu_options) - 1:
        next_level = menu_options[current_index + 1]
    else:
        next_level = "IM Role"  # if it's the last item

    # Form for Student ID, Attempt, Result, and Timeout
    with st.form(key="submission_form"):
        student_id = st.text_input("Student ID", value="", key="student_id")
        attempt = st.number_input("Attempt", min_value=1, step=1, key="attempt")
        result = st.selectbox("Result", ["PASS", "FAIL", "NUKE"], key="result")
        timeout = st.selectbox("Timeout", ["None", "24H", "48H", "72H"], key="timeout")

        submit_button = st.form_submit_button("Submit")

        if submit_button:
            data = {
                'grader' : "admin",
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
**UID: {student_id}**  
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
**UID: {student_id}**  
**Attempt:** {attempt}  
**Result:** **{result}**  

**Feedback:** 
-> 

**🔥🔥🔥 {next_level} IS YOURS 🔥🔥🔥**
"""
                    st.code(message, language='markdown')
            else:
                st.error(f'Failed to send data: {response.status_code} - {response.text}')

    # Show a message that the form was submitted successfully
    if st.session_state.form_submitted:
        st.success("Form has been successfully submitted and the data has been sent!")
