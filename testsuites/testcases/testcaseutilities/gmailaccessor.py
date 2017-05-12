import imaplib
import re

# This takes a string for the xyz.wealthforge.org
def get_new_bd_user_password_reset_url(env, newbduseremail):
    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login("wealthforgedev1@gmail.com","Test123!")
    mail.select('inbox')
    type, data = mail.search(None, '(FROM "WealthForge Technologies" SUBJECT "Welcome to the WealthForge Platform" TO "'+ newbduseremail +'")')
    for num in data[0].split():
        # TODO get this to return a string and not RFC822 because you currently get back
        # carriage returns + new lines (\r\n) in the string and it blows up the password reset url
        typ, data = mail.fetch(num, '(RFC822)')
        # TODO make this regular expression environment agnostic (replace 'q' with 'ci' or 'stage' dynamically )
        env = env.replace(".","\.", 1)
        env = env.replace(".org","\.=org")
        env = env.replace(".com","\.=com")
        match = re.search(r'(https:\/\/' + env + ').*(confirmUser).{42}', str(data[0][1]).replace('\\r\\n',''))
        return match.group().replace("=","",1)
