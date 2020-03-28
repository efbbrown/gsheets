
from __future__ import print_function
import os.path
import pickle
import pandas as pd
import pygsheets
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


class gsheets():

    def __init__(self, credentials_file="credentials.json"):
        pass

    def download_sheets(
            self,
            spreadsheet_id,
            range_name,
            scopes=['https://www.googleapis.com/auth/spreadsheets.readonly']):
        """
        Downloads a sheet & returns it as pandas dataframe
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
                    self.credentials_file, scopes)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)
        service = build('sheets', 'v4', credentials=creds)
        # Call the Sheets API
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=spreadsheet_id,
                                    range=range_name).execute()
        values = result.get('values', [])
        if not values:
            print('No data found.')
            return None
        else:
            return pd.DataFrame(values[1:], columns=values[0])

    def write_to_sheets(
            self,
            sheet,
            worksheet,
            dataframe):
        gc = pygsheets.authorize(service_file=self.credentials_file)
        wks = gc.open(sheet).worksheet_by_title(worksheet)
        wks.set_dataframe(dataframe, (1, 1))
