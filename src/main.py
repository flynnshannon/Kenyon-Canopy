from tree import Tree
import web

# code for reading from spreadsheet will go here

test = Tree('106 Gaskin Avenue Gambier, Ohio 43022', ['red maple', '//*[@id="species-option-container"]/span[7]'], '20.4', '//*[@id="condition"]/option[2]',
            '//*[@id="exposure"]/button[3]', True, '//*[@id="vintage"]/option[3]', '//*[@id="distance"]/option[2]', '//*[@id="direction"]/option[2]')
response = web.get_metrics(test)
