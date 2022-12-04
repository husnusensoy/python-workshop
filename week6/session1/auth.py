from __future__ import print_function

from google.oauth2 import service_account
from googleapiclient.discovery import build

SCOPES = [
'https://www.googleapis.com/auth/spreadsheets',
'https://www.googleapis.com/auth/drive'
]
credentials = service_account.Credentials.from_service_account_file('python-workshop-369005-76946b8c739d.json', scopes=SCOPES)
spreadsheet_service = build('sheets', 'v4', credentials=credentials)
drive_service = build('drive', 'v3', credentials=credentials)