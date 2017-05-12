from __future__ import print_function
import httplib2
import os

from requests import get
from apiclient import errors
from apiclient import http
from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.contrib import gce
from oauth2client.file import Storage

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

# Had to install (pip) httplib2, requests,
# sudo pip install --upgrade google-api-python-client


# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/admin-directory_v1-python-quickstart.json

def touch(path):
    with open(path, 'a'):
        os.utime(path, None)

def get_credentials():
    SCOPES = ("https://www.googleapis.com/auth/gmail.readonly ")
    CLIENT_SECRET_FILE = 'pysel_secret.json'
    APPLICATION_NAME = 'pysel'
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,'pysel_creds.json')
    # if not os.path.exists(credential_path):
    #     touch(credential_path)
    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials


def ListMessagesMatchingQuery(user_id, query=''):
    """List all Messages of the user's mailbox matching the query.

    Args:
      service: Authorized Gmail API service instance.
      user_id: User's email address. The special value "me"
      can be used to indicate the authenticated user.
      query: String used to filter messages returned.
      Eg.- 'from:user@some_domain.com' for Messages from a particular sender.

    Returns:
      List of Messages that match the criteria of the query. Note that the
      returned list contains Message IDs, you must use get with the
      appropriate ID to get the details of a Message.
    """
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('gmail', 'v1', http=http)

    try:
        response = service.users().messages().list(userId=user_id,q=query).execute()
        messages = []
        if 'messages' in response:
            messages.extend(response['messages'])

        while 'nextPageToken' in response:
            page_token = response['nextPageToken']
            response = service.users().messages().list(userId=user_id, q=query,pageToken=page_token).execute()
            messages.extend(response['messages'])

        return messages
    except errors.HttpError as error:
        print ('An error occurred: %s' % error)
