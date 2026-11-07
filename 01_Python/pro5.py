# Python Dictionary
# collection of items
# It store elements in key value pairs. Here keys are unique identifier that are associated with each value.
capitals = {'Nepal': 'Kathmandu', 'Italy': 'Rome', 'England': 'Rome'}

print(capitals)
capitals['Japan'] = 'Tokyo'
capitals['Italy'] = 'Florence'
print(capitals)

print(capitals['England'])

for i in capitals:
    print(capitals[i])
    
del capitals['Italy']

print(capitals)
map = {1: 2, 3: 4}

del map # delete entire map
print(map)
