from tree import Tree
import web

test = Tree('106 Gaskin Avenue Gambier, Ohio 43022', ['red maple', '//*[@id="species-option-container"]/span[7]'], '20.4', '//*[@id="condition"]/option[2]',
            '//*[@id="exposure"]/option[2]', True, '//*[@id="vintage"]/option[2]', '//*[@id="distance"]/option[2]', '//*[@id="direction"]/option[2]')
web.enter_tree(test)
