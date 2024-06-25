import streamlit as st
import time
import pandas as pd

# Initialize the session state for users if it doesn't exist
if 'users' not in st.session_state:
    st.session_state.users = {
        "user1": "password1",
        "user2": "password2",
    }

# Function to simulate a task that takes 2 seconds
def simulate_task():
    # Simulate a task with a spinner and success message after 2 seconds
    with st.spinner("Performing task..."):
        time.sleep(2)  # Simulate a task that takes 2 seconds
        st.success("Task completed successfully!")

# Function to handle the main interface after login
def display_main_interface(username):
    st.success(f"Welcome, {username}!")
    st.write("Please select a task:")

    # Checkbox options for different tasks
    if st.checkbox("Task 1: Select Date and Time"):
        st.session_state.page = 'select_date_time'
        st.session_state.selected_task = "Task 1"

    if st.checkbox("Task 2: Feedback Form"):
        st.session_state.page = 'Feedback_Form'
        st.session_state.selected_task = "Task 2"

    if st.checkbox("Task 3: Data Visualization"):
        st.session_state.page = 'Data_Visualization'
        st.session_state.selected_task = "Task 3"

def display_select_date_time_page():
    st.header("Task 1: Select Date and Time")
    date = st.date_input("Select a date")
    time = st.time_input("Select a time")
    
    # Submit button to display selected date and time
    if st.button("Submit"):
        with st.spinner("Processing..."):
            simulate_task()  # Simulate a task
        st.success(f"Selected Date: {date}, Selected Time: {time}")
        st.balloons()  # Display animated balloons
    
    # Back button to return to the main interface
    if st.button("Back to Main"):
        st.session_state.page = 'main_interface'

def display_feedback():
    st.header("Task 2: Feedback Form")
    
    # Feedback form fields
    name = st.text_input("Enter Your Name:")
    fname = st.text_input("Enter Your Father Name:")
    adrs = st.text_area("Enter Your Address:")
    
    # Slider for selecting class
    classdata = st.select_slider("Select Your Class:", options=["1st", "2nd", "3rd", "4th", "5th", "6th"])

    # Additional information toggle
    show_additional_info = st.checkbox("Show Additional Information")

    # Submit button to display entered information
    if st.button("Done"):
        with st.spinner("Processing..."):
            simulate_task()  # Simulate a task
            st.balloons()  # Display animated balloons
            
        # Display formatted information using st.empty()
        result_container = st.empty()
        result_container.markdown(f"""
              **Name:** {name}  
              **Father Name:** {fname}  
              **Address:** {adrs}  
              **Class:** {classdata}
           """)
    
    # Back button to return to the main interface
    if st.button("Back to Main"):
        st.session_state.page = 'main_interface'

def display_data_visualization():
    st.header("Task 3: Data Visualization")
    
    # Load dataset (replace with your own dataset)
    dataset = pd.DataFrame({
        'Category': ['A', 'B', 'C', 'D'],
        'Values': [10, 20, 15, 25]
    })
    
    # Checkbox to show/hide dataset
    if st.checkbox("Show Dataset"):
        st.dataframe(dataset)
    
    # Bar chart
    st.subheader("Bar Chart")
    st.bar_chart(dataset.set_index('Category')['Values'])

    # Line chart
    st.subheader("Line Chart")
    st.line_chart(dataset.set_index('Category')['Values'])

    # Back button to return to the main interface
    if st.button("Back to Main"):
        st.session_state.page = 'main_interface'

def main():
    st.title("Welcome to My Website")

    # Check if 'page' exists in session state, otherwise set to 'login'
    if 'page' not in st.session_state:
        st.session_state.page = 'login'

    # Handle different pages based on 'page' value
    if st.session_state.page == 'login':
        # Display login or sign up options
        menu = ["Login", "Sign Up"]
        choice = st.sidebar.selectbox("Menu", menu)

        if choice == "Login":
            # Login section
            st.subheader("Login Section")

            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            login_button = st.button("Login")

            # Validate login credentials
            if login_button:
                if username != "" and password != "":
                    if username in st.session_state.users and st.session_state.users[username] == password:
                        st.success("Successful login!")  # Display success message with balloon animation
                        st.balloons()  # Display balloon animation

                        # Set session state for logged-in user
                        st.session_state.page = 'main_interface'
                        st.session_state.username = username
                    else:
                        st.error("Incorrect username or password")
                else:
                    st.warning("Please enter username and password")

        elif choice == "Sign Up":
            # Sign up section
            st.subheader("Create New Account")
            new_user = st.text_input("New Username")
            new_password = st.text_input("New Password", type="password")
            confirm_password = st.text_input("Confirm Password", type="password")
            sign_up_button = st.button("Sign Up")

            # Validate sign-up details and create new account
            if sign_up_button:
                if new_password == confirm_password:
                    if new_user not in st.session_state.users:
                        st.session_state.users[new_user] = new_password
                        st.success("You have successfully created an account")
                        st.info("Go to Login Menu to login")
                    else:
                        st.error("Username already exists")
                else:
                    st.error("Passwords do not match")

    elif st.session_state.page == 'main_interface':
        # Display main interface with different task options
        display_main_interface(st.session_state.username)

    elif st.session_state.page == 'select_date_time':
        # Display task 1: select date and time page
        display_select_date_time_page()

    elif st.session_state.page == 'Feedback_Form':
        # Display task 2: feedback form page
        display_feedback()

    elif st.session_state.page == 'Data_Visualization':
        # Display task 3: data visualization page
        display_data_visualization()

if __name__ == '__main__':
    main()
