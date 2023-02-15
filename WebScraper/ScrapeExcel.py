import pandas as pd
import datetime
import smtplib
import os
import time
from email.mime.text import MIMEText

# Load the Excel file into a pandas dataframe
file_path = 'Dates.xlsx'

# Store the modification time of the file
previous_modification_time = os.path.getmtime(file_path)

while True:
    # Check if the file has been modified
    current_modification_time = os.path.getmtime(file_path)
    if current_modification_time != previous_modification_time:
        # Load the updated file into a pandas dataframe
        df = pd.read_excel(file_path)

        # Create a dictionary from the two columns
        data = dict(zip(df.iloc[:, 0], df.iloc[:, 1]))

        # Convert the values in the dictionary (dates) to datetime objects
        dates = {key: pd.to_datetime(value) for key, value in data.items()}

        dates['Make Excel Document'] = 'Feburary 16 2023'

        # Calculate the difference between each date and the current date
        now = pd.to_datetime(datetime.datetime.now().date())
        differences = {key: value - now for key, value in dates.items()}

        # Check if any difference is less than 30 days
        thirty_days = pd.Timedelta(days=30)
        for key, difference in differences.items():
            if difference < thirty_days:
                # Send an email alert
                subject = "Date Alert"
                message = f"The date '{dates[key]}' is less than 30 days away"
                msg = MIMEText(message)
                msg['Subject'] = subject
                from_address = input('enter email address you are sending from: ')
                pwd = input('Enter your password: ')
                msg['From'] = from_address
                msg['To'] = input('enter email address you are sending to: ')
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(from_address, pwd)
                server.send_message(msg)
                from_address = ''
                pwd = ''
                server.quit()
                break
        else:
            print("No date is less than 30 days away")

        # Update the modification time of the file
        previous_modification_time = current_modification_time
    else:
        # Sleep for 24 hours before checking again
        time.sleep(24 * 60 * 60)
