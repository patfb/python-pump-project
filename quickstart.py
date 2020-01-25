import os.path
import pickle

from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

SPREADSHEET_ID = '1nQhYukEuUahxMTMkZoB3pbye2bFABTraQXXcvZTbyzY'
RANGE_NAME = 'Pump!A:B'


def main():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('sheets', 'v4', credentials=creds)

    values = [
        ["on", "off"],
        ["1", "2"],
        ["3", "4"],
        ["5", "6"],
    ]

    body = {
        "values": values
    }

    result = service.spreadsheets().values().append(
        spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME, valueInputOption="USER_ENTERED",
        body=body).execute()

    print('{0} cells appended.'.format(result
                                       .get('updates')
                                       .get('updatedCells')))


if __name__ == '__main__':
    main()
