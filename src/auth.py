import streamlit as st
import pandas as pd
import os
from datetime import datetime, timedelta
from .config import *
import time # For simulating file changes if needed


# --- Helper Functions for User Management ---

def create_initial_users_csv():
    """
    Creates a dummy users.csv file if it doesn't exist.
    In a real application, you'd manage users via a proper system.
    """
    if not os.path.exists(USERS_CSV_FILE):
        df = pd.DataFrame({
            "username": ["admin", "user1", "testuser"],
            "password": ["adminpass", "userpass123", "testpass"]
        })
        df.to_csv(USERS_CSV_FILE, index=False)
        st.success(f"Created initial '{USERS_CSV_FILE}' with dummy users.")
        st.info("You can edit this CSV file manually to add/remove users.")

def load_users_from_csv():
    """
    Loads user credentials from the CSV file.
    Reloads only if the file has been modified.
    """
    try:
        current_mtime = os.path.getmtime(USERS_CSV_FILE)
        if 'last_csv_mtime' not in st.session_state or st.session_state['last_csv_mtime'] != current_mtime:
            df = pd.read_csv(USERS_CSV_FILE)
            users_dict = {row['username']: row['password'] for index, row in df.iterrows()}
            st.session_state['users'] = users_dict
            st.session_state['last_csv_mtime'] = current_mtime
            st.info(f"User data reloaded from '{USERS_CSV_FILE}'.")
        return st.session_state['users']
    except FileNotFoundError:
        st.error(f"Error: '{USERS_CSV_FILE}' not found. Please create it or restart the app.")
        create_initial_users_csv() # Attempt to create it if missing
        return {} # Return empty dict if file is still not there
    except Exception as e:
        st.error(f"Error loading user data: {e}")
        return {}

def authenticate(username, password):
    """
    Checks if the provided username and password are valid against loaded users.
    """
    users = load_users_from_csv()
    if username in users and users[username] == password:
        return True
    return False

def check_session_validity():
    """
    Checks if the current login session is still valid based on the set period.
    Logs out the user if the session has expired.
    """
    if 'authenticated' in st.session_state and st.session_state['authenticated']:
        if 'login_time' in st.session_state:
            login_time = st.session_state['login_time']
            current_time = datetime.now()

            # Choose the validity period based on your configuration-
            validity_duration = timedelta(days=VALIDITY_PERIOD_DAYS, minutes=VALIDITY_PERIOD_MINUTES) # For 2 days

            if current_time - login_time > validity_duration:
                st.warning("Your session has expired. Please log in again.")
                logout_user()
                st.rerun() # Rerun to show the login page
        else:
            # If authenticated but no login_time, something is off, force logout
            logout_user()
            st.rerun()

def logout_user():
    """Clears authentication-related session state variables."""
    if 'authenticated' in st.session_state:
        del st.session_state['authenticated']
    if 'username' in st.session_state:
        del st.session_state['username']
    if 'login_time' in st.session_state:
        del st.session_state['login_time']
    st.info("You have been logged out.")

# --- Reusable Authentication Interface ---

def authentication_widget():
    """
    Provides a reusable login/logout interface.
    Returns True if authenticated, False otherwise.
    """
    if 'authenticated' not in st.session_state:
        st.session_state['authenticated'] = False

    if st.session_state['authenticated']:
        # Display logout button if authenticated
        st.sidebar.write(f"Logged in as: **{st.session_state['username']}**")
        if st.sidebar.button("Logout", key="sidebar_logout"):
            logout_user()
            st.rerun()
        return True
    else:
        # Display login form if not authenticated
        st.sidebar.header("Login")
        username = st.sidebar.text_input("Username", key="login_username")
        password = st.sidebar.text_input("Password", type="password", key="login_password")

        if st.sidebar.button("Login", key="sidebar_login"):
            if authenticate(username, password):
                st.session_state['authenticated'] = True
                st.session_state['username'] = username
                st.session_state['login_time'] = datetime.now() # Record login time
                st.sidebar.success(f"Welcome, {username}!")
                st.rerun()
            else:
                st.sidebar.error("Invalid username or password.")
        return False
