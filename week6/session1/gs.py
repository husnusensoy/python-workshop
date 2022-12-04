import gspread
from auth import credentials, drive_service, spreadsheet_service

client = gspread.authorize(credentials)

sheet = client.create("First Session First File")
# sheet.share('husnu.sensoy@globalmaksimum.com', perm_type='user', role='writer')

details = {"properties": {"title": "Python-google-sheets-demo"}}

sheet = (
    spreadsheet_service.spreadsheets()
    .create(body=details, fields="spreadsheetId")
    .execute()
)

sheetID = sheet.get("spreadsheetId")

print(f"Spreadsheet ID: {sheetID}")

permission = {
    "type": "user",
    "role": "writer",
    "emailAddress": "husnu.sensoy@globalmaksimum.com",
}

drive_service.permissions().create(fileId=sheetID, body=permission).execute()

import pandas as pd

df = pd.DataFrame(
    [[21, 72, 67], [23, 78, 69], [32, 74, 42], [15, 24, 76]], columns=["a", "b", "c"]
)


body = {"values": df.values.tolist()}

result = (
    spreadsheet_service.spreadsheets()
    .values()
    .append(
        spreadsheetId=sheetID,
        body=body,
        valueInputOption="USER_ENTERED",
        range="Sheet1",
    )
    .execute()
)

print(f'{result.get("updates").get("updateCells")} cells appended')