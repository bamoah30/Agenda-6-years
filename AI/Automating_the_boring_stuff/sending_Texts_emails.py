'''SMTP:
Whilst HTTP is the protocol used by computers to send web pages across the internet,
SMTP (Simple Mail Transfer Protocol) is the protocol used for sending email.

SMTP dictates how email messages should be formatted, 
encrypted, and relayed between mail servers, and all the other details that 
your computer handles after you click Send.

NB: SMTP just deals with sending emails to others. A different protocol, 
called IMAP, deals with retrieving emails sent to you.




Provider                    SMTP server domain name
Gmail                               smtp.gmail.com
Outlook.com/Hotmail.com             smtp-mail.outlook.com
Yahoo Mail                          smtp.mail.yahoo.com
AT&T                                smtp.mail.att.net (port 465)
Comcast                             smtp.comcast.net
Verizon                             smtp.verizon.net (port 465)

NB: The default port number is 587

NB: Once you have the domain name and the port number, you can create an SMTP object.
'''
# Step 1: Creating SMTP object
import smtplib

# Replace 'smtp.example.com' and 587 with your provider's SMTP server and port
smtp = smtplib.SMTP('smtp.example.com', 587)


#Step 2: Sending SMTP "Hello Message"
# Send EHLO to the server to identify the client and get server capabilities
smtp.ehlo()


#Step 3: Starting TLS Encryption
'''NOTE:
If you are connecting to port 587 on the SMTP server (that is, you’re 
using TLS encryption), you’ll need to call the starttls() method next. This 
required step enables encryption for your connection. If you are connecting 
to port 465 (using SSL), then encryption is already set up, and you should 
skip this step.'''
# Start TLS to secure the connection (only for ports like 587)
smtp.starttls()
# Re-identify after starting TLS
smtp.ehlo()


# Step 4: Logging in to the SMTP Server
# Provide your real credentials here
username = 'your_email@example.com'
password = 'your_password'
smtp.login(username, password)


#Step 5: Sending an Email
from_addr = 'your_email@example.com'
to_addr = 'recipient@example.com'
subject = 'Test Email'
body = 'This is a test email sent via SMTP.'

# Simple RFC 2822 formatted message
'''Note:
RFC(Request For Comment) 2822 is the Internet standard that defines the format of email messages, including headers and body structure.'''
msg = f"Subject: {subject}\nFrom: {from_addr}\nTo: {to_addr}\n\n{body}"

smtp.sendmail(from_addr, to_addr, msg)


#Step 6: Disconnecting from the SMTP Server
smtp.quit()


'''Extra:
TLS (Transport Layer Security) and SSL (Secure Sockets Layer) are cryptographic protocols 
that secure communication over the internet by encrypting data, ensuring privacy, integrity, and authentication. 
SSL is the older protocol, while TLS is its modern, more secure successor'''