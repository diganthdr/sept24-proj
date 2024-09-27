import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Step 1: Set up the SMTP server
smtp_server = "smtp.gmail.com"
port = 587  # For TLS
sender_email = "bitsandbytes01000100@gmail.com"
receiver_email = "diganth@gmail.com"
password = "BitsAndBytes1234" 
password = "rcvvxhzztqgiffgi"

def sendemail(receiver_email, subject, body):
    # Step 2: Create the email content

    # Create a multipart message
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    # Attach the body of the email
    message.attach(MIMEText(body, "plain"))

    # Step 3: Establish a connection and send the email
    try:
        # Connect to the server
        server = smtplib.SMTP(smtp_server, port)
        server.starttls()  # Secure the connection

        # Login to the email account
        server.login(sender_email, password)

        # Send the email
        server.sendmail(sender_email, receiver_email, message.as_string())
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Close the connection
        server.quit()

subject = "Hello from Python boot camp Sept 2024!"
body = "This is a test email sent from Python."

rcvrs = ["sachin674@gmail.com,", "dhanyashreed2006@gmail.com",
"simhakip@gmail.com", "rashmihiremath003@gmail.com", "pasupula123@gmail.com",
"cherosh@gmail.com"]

for s in rcvrs:
    sendemail(s, subject, body)

# sendemail(rcvrs, "Guten Morgen!", "Wie geht es dir?!")