import imaplib
import re
from testutilities import Settings

def get_new_bd_user_password_reset_url(newbduseremail):
    '''
    Gets the password reset link for BD new users.  
    Currently only wealthforgedev1@gmail.com and it's + variations are allowed because of the api keys
    :param newbduseremail: The new user's email
    :return: reset password link not including the environment (/login/#/confirmUser...)
    '''
    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login("wealthforgedev1@gmail.com","Test123!")
    mail.select('inbox')
    type, data = mail.search(None, '(FROM "WealthForge Technologies" SUBJECT "Welcome to the WealthForge Platform" TO "'+ newbduseremail +'")')

    for num in data[0].split():
        typ, data = mail.fetch(num, '(RFC822)')

        match = re.search(r'(confirmUser).{42}', str(data[0][1]))
        return '/login/#/' + match.group()


def get_new_ip_user_password_reset_url(env, newbduseremail):
    '''
    Gets the password reset link for IP new users.  
    Currently only wealthforgedev1@gmail.com and it's + variations are allowed because of the api keys
    :param newbduseremail: The new user's email
    :return: reset password link not including the environment (/login/#/confirmUser...)
    '''
    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login("wealthforgedev1@gmail.com","Test123!")
    mail.select('inbox')
    type, data = mail.search(None, '(FROM "WealthForge Technologies" SUBJECT "Welcome to the WealthForge Platform" TO "'+ newbduseremail +'")')

    for num in data[0].split():
        typ, data = mail.fetch(num, '(RFC822)')

        match = re.search(r'(passwordReset).{42}', str(data[0][1]))
        return '/IP/#/' + match.group()

#/IP/#/passwordReset?id=
# https://ci.wealthforge.org/IP/#/passwordReset?id=5ee243ec-3da2-41a8-8803-a0008c167a50&dpo=ef05acea-9421-4dee-9397-8d8b454d669d