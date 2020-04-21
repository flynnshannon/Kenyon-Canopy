from tree import Tree
import web
import pandas as pd

#TODO accept more general trees

itree_inputs = ['Species', 'DBH', 'Condition', 'Exposure', 'Near Building',
                'Building Year', 'Distance to Building', 'Cardinal Direction to Building']
itree_outputs = ['Total Benefit', 'Carbon Sequestered',
                 'Carbon Stored', 'Storm Water', 'Rainfall', 'Air pollution removed']

df = pd.read_excel('test.xlsx').to_dict()
unupdated = []
for key in df['Total Benefit']:
  if not (df['Total Benefit'][key] > 0):
    unupdated.append(key)
    # get indices of unupdated entries

trees = []
for i in unupdated:
  trees.append([])
  for key in itree_inputs:
    trees[-1].append(df[key][i])
forest = []

for tree in trees:
  #print('len: ' + str(len(tree)))
  tree[0] = [tree[0], '//*[@id="species-option-container"]/span[7]']
  if tree[4] == 'No':  # check for not near building
    tree[5] = '0'
    tree[6] = '0'
    tree[7] = '0'
  #print(tree)
  forest.append(Tree('106 Gaskin Avenue Gambier, Ohio 43022', tree[0], tree[1], tree[2], tree[3], tree[4], tree[5], tree[6], tree[7]))

test = Tree('106 Gaskin Avenue Gambier, Ohio 43022', ['red maple', '//*[@id="species-option-container"]/span[7]'], '20.4', '//*[@id="condition"]/option[2]',
            '//*[@id="exposure"]/button[3]', True, '//*[@id="vintage"]/option[3]', '//*[@id="distance"]/option[2]', '//*[@id="direction"]/option[2]')
response = web.get_metrics(test)
responses = [response]*2
for tree in forest:
  #responses.append(web.get_metrics(tree))
  pass

for i in unupdated:
  j=0
  for key in itree_outputs:
    df[key][i] = responses[i][j]
    j+=1

pd.DataFrame.from_dict(df).to_excel('test1.xlsx')
