#Reading inbox emails from CLI.
#!/usr/bin/env python

import base64, imaplib, email, re, os
import getpass
from bs4 import BeautifulSoup
imaplib._MAXLINE = 400000

ORG_EMAIL   = "@gmail.com"
FROM_EMAIL  = "mohansha.don" + ORG_EMAIL
FROM_PWD    = getpass.getpass()
SMTP_SERVER = "imap.gmail.com"
SMTP_PORT   = 993

mail = imaplib.IMAP4_SSL(SMTP_SERVER)
mail.login(FROM_EMAIL, FROM_PWD)
mail.list()
mail.select('inbox')

i = 0

def main():
	global i
	clear()
	mail = imaplib.IMAP4_SSL(SMTP_SERVER)
	mail.login(FROM_EMAIL, FROM_PWD)
	mail.list()
	mail.select('inbox')
	inp = 'n'

	
	while(inp!='q'):
		print('Fetching mails. Please wait...')
		if inp == 'n':
			i += 1
		elif inp == 'p' and i != 1:
			i -= 1
		else:
			print('Please enter valid input.')
		result, data = mail.uid('search', None, "ALL") # search and return uids instead
		latest_email_uid = data[0].split()[-i] # fetch mails 
		result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
		raw_email = data[0][1]
		email_message = email.message_from_string(raw_email)

		clear() # clear screen and print mail
		print 'To:', email_message['To']
		print 'Sent from:', email_message['From']
		print 'Date:', email_message['Date']
		print 'Subject:', email_message['Subject']
		print '*'*30, 'MESSAGE', '*'*30
		maintype = email_message.get_content_maintype()
		#print maintype

		if maintype == 'multipart': # get the body of the mail
		    print email_message.get_payload()[0].get_payload() # to get the plain text only
		elif maintype == 'text':
			line = email_message.get_payload()[ 0 ]
			print line
		print '*'*69
		welcome()
		inp = raw_input('>> Enter your choice: ').lower()



def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def welcome():
    print '\n'
    print '>> Enter \'n\' to check NEXT mail'
    print '>> Enter \'p\' to check PREVIOUS mail'
    print '>> Enter \'q\' to QUIT'   

if __name__ == '__main__':
	main() 
