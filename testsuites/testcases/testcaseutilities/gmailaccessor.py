import imaplib
import re
from testutilities import Settings
import time

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
    type1, data = mail.search(None, '(FROM "WealthForge Technologies" SUBJECT "Welcome to the WealthForge Platform" TO "'+ newbduseremail +'")')

    for num in data[0].split():
        typ, data = mail.fetch(num, '(RFC822)')

        match = re.search(r'(confirmUser).{42}', str(data[0][1]))
        return '/login/#/' + match.group()


def get_new_ip_user_password_reset_url(newUserEmail):
    '''
    Gets the password reset link for IP new users.  
    Currently only wealthforgedev1@gmail.com and it's + variations are allowed because of the api keys
    :param newbduseremail: The new user's email
    :return: reset password link not including the environment (/login/#/confirmUser...)
    '''

    # for some reason this email is slower and needs to be waited for
    time.sleep(5)
    if Settings.VERBOSITY >= 5: print('Retrieving new IP confirmation email for', newUserEmail)
    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login("wealthforgedev1@gmail.com","Test123!")
    mail.select('inbox')
    type1, data = mail.search(None, '(FROM "WealthForge Technologies" SUBJECT "Welcome to WealthForge Investing" TO "' + newUserEmail + '")')
    #TODO: add assert an email was found
    for num in data[0].split():

        typ, data = mail.fetch(num, '(RFC822)')
        # The first replace() is to get rid of the \r\n
        # The second replace() gets rid of a weird RFC822 thing where equal signs show as =3D (3D is ascii for =)
        match = re.search(r'(passwordReset).{81}', str(data[0][1]).replace('=\\r\\n', '').replace('=3D', '='))
        print('/IP/#/' + match.group())
        return '/IP/#/' + match.group()
