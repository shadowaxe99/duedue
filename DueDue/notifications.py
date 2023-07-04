```python
import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Shared dependencies
contract_dates = []
user_config = {}

def send_notification(contract_date, contract_name):
    """
    Function to send email notifications for approaching contract dates
    """
    # Check if the contract date is within the next 7 days
    if contract_date - datetime.datetime.now() <= datetime.timedelta(days=7):
        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = user_config['email']
        msg['To'] = user_config['email']
        msg['Subject'] = f"DueDue Reminder: {contract_name} is due soon"
        body = f"The contract {contract_name} is due on {contract_date.strftime('%Y-%m-%d')}."
        msg.attach(MIMEText(body, 'plain'))

        # Send the email
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(user_config['email'], user_config['password'])
        text = msg.as_string()
        server.sendmail(user_config['email'], user_config['email'], text)
        server.quit()

def check_notifications():
    """
    Function to check if there are any upcoming contract dates that require notifications to be sent
    """
    for contract in contract_dates:
        send_notification(contract['date'], contract['name'])
```