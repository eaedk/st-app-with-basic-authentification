import streamlit as st
import pandas as pd
import os
from datetime import datetime, timedelta
import time # For simulating file changes if needed
from src.config import USERS_CSV_FILE
from src.auth import authentication_widget, create_initial_users_csv, check_session_validity


# --- Main Application Pages (Examples) ---

def home_page():
    st.title("Home Page")
    st.write("This is the public home page. Anyone can see this.")
    st.info("Please log in to access private content.")

def dashboard_page():
    st.title("Dashboard")
    st.write(f"Welcome to your personalized dashboard, **{st.session_state['username']}**!")
    st.write("Here you can see your private data and analytics.")
    st.bar_chart(pd.DataFrame({"Data": [10, 20, 15, 25, 30]}, index=["A", "B", "C", "D", "E"]))

def settings_page():
    st.title("Settings")
    st.write(f"Adjust your settings here, **{st.session_state['username']}**.")
    st.slider("Volume", 0, 100, 50)
    st.checkbox("Enable notifications")

# --- Main App Flow ---

def run_app():
    st.set_page_config(layout="wide")

    # Check if 'first_run' exists in session_state
    if not os.path.exists(USERS_CSV_FILE):
        # Run the function on the first execution
        # Ensure the CSV file exists
        create_initial_users_csv()

    # Always check session validity at the start of the app run
    check_session_validity()

    # Display the authentication widget in the sidebar
    is_authenticated = authentication_widget()

    # Navigation for authenticated users
    if is_authenticated:
        
        pg = st.navigation([st.Page(dashboard_page, title="Dashboard"), 
                            st.Page(settings_page, title="Settings")] ,
                             )
    else:
        # Navigation for unauthenticated users (home page and contact)

        # pg = st.navigation({"Home": [st.Page(home_page)] ,
        #                     #  "B": [st.Page(home_page)] ,
        #                      })
        pg = st.navigation([st.Page(home_page), 
                            st.Page('./_pages/contact.py')] ,
                             )
    
    pg.run()

if __name__ == "__main__":
    run_app()
