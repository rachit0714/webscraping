import pandas as pd
import datetime
import smtplib
import os
import time
from email.mime.text import MIMEText
'''
    Reads an excel sheet that is made up of tasks to do and duedates and sends an email when the item is less than 1 month away from being due
'''
def main(from_address, to_address, file_path ):
    #stores the last time file has been modified
    previous_modification_time = os.path.getmtime(file_path)

    while True:

        #checks if file has been modified again
        current_modification_time = os.path.getmtime(file_path)
        print(f'Previously modified {previous_modification_time} and currently modified {current_modification_time}')
        
        if previous_modification_time != current_modification_time:

            #loads the excel file
            df = pd.read_excel(file_path)

            #grabs columns using iloc function and [:,0] grabs whole of the first column
            #then zip makes it to a dictionary
            data = dict(zip(df.iloc[:,0],df.iloc[:,1]))

            print(f'The variable data looks like {data}')

            #converts the dates in the dictionary to datetime objects
            dates = {key: pd.to_datetime(value) for key, value in data.items()}

            print('Dates dictionary looks like:')
            for key, value in dates.items():
                print(f'{key} has the value {value}')

            # Calculates the difference between each date and the current time
            now = pd.to_datetime(datetime.datetime.now().date())
            differences = {key: value - now for key, value in dates.items()}

            #checks the if there is less than 30 days for any project
            thirty_days = pd.Timedelta(days = 30)
            for key, difference in differences.items():
                if difference < thirty_days:
                    #Send an email alert
                    subject = str(key)
                    message = f'{subject} will expire in 30 days at {dates[key]}'
                    msg = MIMEText(message)
                    msg['Subject'] = subject
                    pwd = input('Input your password: ')
                    msg['From'] = from_address
                    msg['To'] = to_address
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
        else:
            #Sleep for 24 hours before checking again
            print('waiting 1 hour')
            time.sleep(60 * 60)

        previous_modification_time = current_modification_time
        
if __name__ == '__main__':
    fa = input('Enter the email address you want to send from: ')
    ta = input('Enter the address you are sending to: ')
    
    file = input("What file do you want to open? ")
    main(fa,ta, file)


