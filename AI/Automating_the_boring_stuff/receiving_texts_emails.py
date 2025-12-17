#December 16, 2025

'''IMAP( Internet Message Access Protocol):
Just as SMTP is the protocol for sending email, the Internet Message Access 
Protocol (IMAP) specifies how to communicate with an email provider’s 
server to retrieve emails sent to your email address. Python comes with an 
imaplib module, but in fact the third-party imapclient module is easier to 
use.Here, we will be dealing with introduction to the third-party imapclient module.

The steps below shows you how to use the package.'''

#Step 1: Connecting to an IMAP Server
'''Just like you needed an SMTP object to connect to an SMTP server and send 
email, you need an IMAPClient object to connect to an IMAP server and 
receive email. First you’ll need the domain name of your email provider’s 
IMAP server. This will be different from the SMTP server’s domain name.

Provider                        IMAP server domain name
Gmail                               imap.gmail.com
Outlook.com/Hotmail.com             imap-mail.outlook.com
Yahoo Mail                          imap.mail.yahoo.com
AT&T                                imap.mail.att.net
Comcast                             imap.comcast.net
Verizon                             incoming.verizon.net

Once you have the domain name of the IMAP server, call the 
imapclient.IMAPClient() function to create an IMAPClient object. Most 
email providers require SSL encryption, so pass the ssl=True keyword 
argument. Enter the following into the interactive shell (using your 
provider’s domain name):'''
import imapclient
imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True)


#Step 2: Logging in to the IMAP Server
'''Once you have an IMAPClient object, call its login() method, passing in the 
username (this is usually your email address) and password as strings'''

imapObj.login('my_email_address@gmail.com', 'MY_SECRET_PASSWORD')

#Step 3:Searching for Email
'''Once you’re logged in, actually retrieving an email that you’re interested in is a two-step process. 
First, you must select a folder you want to search through. 
Then, you must call the IMAPClient object’s search() method, passing in a string of IMAP search keywords.'''


#Step 3.i.: Selecting a Folder
'''Almost every account has an INBOX folder by default, but you can also get a 
list of folders by calling the IMAPClient object’s list_folders() method. This 
returns a list of tuples. Each tuple contains information about a single 
folder. 
Code:   '''
import pprint
pprint.pprint(imapObj.list_folders())
imapObj.select_folder('INBOX', readonly=True)

'''Note:
You can ignore select_folder()’s return value. If the selected folder does 
not exist, Python will raise an imaplib.error exception.
The readonly=True keyword argument prevents you from accidentally 
making changes or deletions to any of the emails in this folder during the 
subsequent method calls. Unless you want to delete emails, it’s a good idea 
to always set readonly to True.'''

#Step 3.ii:Performing the Search
'''With a folder selected, you can now search for emails with the IMAPClient
object’s search() method. The argument to search() is a list of strings, each 
formatted to the IMAP’s search keys.

Search key                                              Meaning
'ALL'                                                   Returns all messages in the folder. You may run in to imaplib
                                                        size limits if you request all the messages in a large folder
                                                        ..
'BEFORE date', 'ON date', 'SINCE date'                  These three search keys return, respectively, messages that 
                                                        were received by the IMAP server before, on, or after the 
                                                        given date. The date must be formatted like 05-Jul-2015.
                                                        Also, while 'SINCE 05-Jul-2015' will match messages on 
                                                        and after July 5, 'BEFORE 05-Jul-2015' will match only messages before July 5 but not on July 5 itself.


'SUBJECT string','BODY string','TEXT string'             Returns messages where string is found in the subject, body, 
                                                         or either, respectively. If string has spaces in it, then enclose 
                                                         it with double quotes: 'TEXT "search with spaces"'.

'FROM string',TO string', 'CC string', 'BCC string'       Returns all messages where string is found in the “from” 
                                                          emailaddress, “to” addresses, “cc” (carbon copy) addresses, 
                                                          or “bcc” (blind carbon copy) addresses, respectively. If there 
                                                          are multiple email addresses in string, then separate them 
                                                          with spaces and enclose them all with double quotes: 
                                                          'CC "firstcc@example.com secondcc@example.com"'.


'SEEN','UNSEEN'                                             Returns all messages with and without the Seen flag, respectively. 
                                                            An email obtains the Seen flag if it has been accessed 
                                                            with a fetch() method call (described later) or if it is clicked 
                                                            when you’re checking your email in an email program or web 
                                                            browser. It’s more common to say the email has been “read” 
                                                            rather than “seen,” but they mean the same thing.


'ANSWERED','UNANSWERED'                                     Returns all messages with and without the Answered flag, 
                                                            respectively. A message obtains the Answered flag when it 
                                                            is replied to.


'DELETED','UNDELETED'                                       Returns all messages with and without the Deleted flag, respectively. 
                                                            Email messages deleted with the delete_messages()
                                                            method are given the Deleted flag but are not permanently 
                                                            deleted until the expunge() method is called. Note that some email providers, 
                                                            such as Gmail, automatically expunge emails.

                                                            
'DRAFT','UNDRAFT'                                           Returns all messages with and without the Draft flag, respectively. 
                                                            Draft messages are usually kept in a separate Drafts
                                                            folder rather than in the INBOX folder.


'FLAGGED','UNFLAGGED'                                       Returns all messages with and without the Flagged flag, respectively. 
                                                            This flag is usually used to mark email messages as “Important” or “Urgent.”


'LARGER N','SMALLER N'                                      Returns all messages larger or smaller than N bytes, respectively.


'NOT search-key'                                            Returns the messages that search-key would not have returned.



'OR search-key1   search-key2'                              Returns the messages that match either the first or second search-key.                                                        
                                                         
Example Usage:
1. imapObj.search(['ALL']): Returns every message in the currently selected folder.

2. imapObj.search(['ON 05-Jul-2015']) Returns every message sent on July 5, 2015.

3.imapObj.search(['SINCE 01-Jan-2015', 'BEFORE 01-Feb-2015', 'UNSEEN']): Returns every message sent in January 2015 that is unread. 
Note: This means on and after January 1 and up to but not including February 1.)

4.imapObj.search(['SINCE 01-Jan-2015', 'FROM alice@example.com']): Returns every message from alice@example.com sent since the start of 2015.

5.imapObj.search(['SINCE 01-Jan-2015', 'NOT FROM alice@example.com']): Returns every message sent from everyone except alice@example.com since the start of 2015.

6.imapObj.search(['OR FROM alice@example.com FROM bob@example.com']):  Returns every message ever sent from alice@example.com or bob@example.com.

7.imapObj.search(['FROM alice@example.com', 'FROM bob@example.com']) : This search will never return any messages, because messages must match all search keywords. 
Since there can be only one “from” address, it is impossible for a message to be from both alice@example.com and bob@example.com.


Code:
'''
UIDs = imapObj.search('SINCE 05-Jul-2015') #the list of message IDs (for messages received July 5 onward) returned by search() is stored in UIDs
print( UIDs)


'''Size Limits
If your search matches a large number of email messages, Python might 
raise an exception that says imaplib.error: got more than 10000 bytes.

When this happens, you will have to disconnect and reconnect to the IMAP server 
and try again.

This limit is in place to prevent your Python programs from eating up too much memory. 

Unfortunately, the default size limit is often too small. You can change this limit from 10,000 bytes to 10,000,000 bytes by running 
this code:'''
import imaplib
imaplib._MAXLINE = 10000000  # type: ignore

'''WARNING!!!:
This should prevent this error message from coming up again. You may
want to make these two lines part of every IMAP program you write.'''


#December 17, 2025
'''Size Limit'''