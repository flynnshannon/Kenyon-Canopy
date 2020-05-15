import gspread
import pandas as pd
from google.oauth2 import service_account
from google.auth.transport.requests import AuthorizedSession


credentials = service_account.Credentials.from_service_account_file(
    'services_account.json')

scoped_credentials = credentials.with_scopes(
        ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
        )
gc = gspread.Client(auth=scoped_credentials)
gc.session = AuthorizedSession(scoped_credentials)
sheet = gc.open('Kenyon College Tree Campus Dynamic Inventory')
dataframe = pd.DataFrame(sheet.sheet1.get_all_records()).to_dict()

# Open a sheet from a spreadsheet in one go
wks = gc.open("Where is the money Lebowski?").sheet1

# Update a range of cells using the top left corner address
wks.update('A1:B2', [[1, 2], [3, 4]])


# Format the header
wks.format('A1:B1', {'textFormat': {'bold': True}})
