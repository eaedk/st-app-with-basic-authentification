import os

# Get the current script's directory
current_directory = os.path.dirname(os.path.realpath(__file__))


# --- Configuration ---
USERS_CSV_FILE = os.path.join(current_directory, "..",  "data", "secret",  "users.csv")

# Define login validity periods
VALIDITY_PERIOD_DAYS = 0 # Login valid for 2 days
VALIDITY_PERIOD_MINUTES = 1 # Login valid for 45 minutes (uncomment to use this)
