Master Branch: The older version(done by Sept 2024)
Log:  <br />
Since successfully set up the Azure, and gathered the sentiment design, it is time to send it to the OPEN AI! <br />
Main Branch: Updated version(Nov 2024)
<br />
<br />
Change: <br />
Try to switch the mail server(i.e. Gmail --> 163.com) as the Gmail's safety restrictions  <br />
Result: Still unsuccessful, but better. Gmail restricted the access fully and I cannot turn on the IMAP restriction(as a regular user) <br />
<br />
_Output: <br />
Connected to IMAP server.  <br />
IMAP Error: b'[AUTHENTICATIONFAILED] Invalid credentials (Failure)'  <br />_
<br />
As for the 163.com, I am able to turn on the IMAP restrictions, but the fetching process is still unsuccessful, (and it seems like a common issue?)<br />
<br />
Output: <br />
_Connected to IMAP server. <br />
Logged in successfully. <br />
Failed to select mailbox: [b'SELECT Unsafe Login. Please contact kefu@188.com for help'] <br />_

As well, realized that the labels of the classification is unnessary and making the program more problematic<br />
as if the label doesn't exist, the program will spend almost forever to proceed and affecting the other modules<br />
eventually cause errors. <br />

I still keep the module and the original usage as in comments(partially, as one is a part of a string)<br />
to let the fellow developer see _why it was there_<br />
