from tree import Tree
import web
import pandas as pd
import gspread
from gspread_dataframe import set_with_dataframe
from google.oauth2 import service_account
from google.auth.transport.requests import AuthorizedSession

#TODO accept more general trees

itree_inputs = ['Species', 'Diameter at breast height (inches)', 'Type', 'Condition', 'Is the tree within 60 ft of a building?', 'Building Year', 'Distance to Building', 'Direction from tree to building', 'Exposure']
itree_outputs = ['Total Benefits ($)', 'CO2sec ($)',
                 'CO2stor (lbs)', 'Storm Water ($)', 'Rainfall Intercepted (gal)', 'Air Pollution Removed Each Year ($)']
input_keys = ['Species', 'Diameter at breast height (inches)', 'Condition', 'Type', 'Is the tree within 60 ft of a building?', 'Building Year', 'Distance to Building', 'Direction from tree to building', 'Total Benefits ($)', 'Exposure']

credentials = service_account.Credentials.from_service_account_file(
    'services_account.json')

scoped_credentials = credentials.with_scopes(
        ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
        )
gc = gspread.Client(auth=scoped_credentials)
gc.session = AuthorizedSession(scoped_credentials)
sheet = gc.open('Kenyon College Tree Campus Dynamic Inventory')
import pdb; pdb.set_trace()
dataframe = pd.DataFrame(sheet.sheet1.get_all_records()).to_dict()
df = {k:v for (k,v) in dataframe.items() if k in input_keys}
unupdated = []
for key in df['Total Benefits ($)']:
  if df['Total Benefits ($)'][key] == '':
    unupdated.append(key)
    # get indices of unupdated entries
trees = []
for i in unupdated:
  trees.append([])
  for key in itree_inputs:
    trees[-1].append(df[key][i])
forest = []
for tree in trees:
  #needs to accept more
  tree[0] = ['Red maple', '//*[@id="species-option-container"]/span[7]']
  if tree[4] == 'No':  # check for not near building
    tree[5] = '0'
    tree[6] = '0'
    tree[7] = '0'
  forest.append(Tree('106 Gaskin Avenue Gambier, Ohio 43022', tree[0], tree[1], tree[2], tree[3], tree[8], tree[4], tree[5], tree[6], tree[7]))

responses = web.get_forest_metrics(forest)

for i in unupdated:
  j=0
  for key in itree_outputs:
    dataframe[key][i] = responses[i][j]
    j+=1

pd.DataFrame.from_dict(dataframe).to_excel('test1.xlsx')
set_with_dataframe(sheet.sheet1, pd.DataFrame.from_dict(dataframe))
