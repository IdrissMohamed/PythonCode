import urllib # this is for python 2.7, python 3 uses urllib.request
import json

# Write to a text file
def store_in_database(name, data):
    filename = 'pages/page' + str(name) + '.json'
    with open(filename, 'w') as file:
        file.write(json.dumps(data, indent=2, sort_keys=True))

links = []

with open('links.txt', 'r') as file:
    for line in file:
        links.append(line.strip()) # strip removes hidden \n from strings
     
# Alternate way to do file IO
# file = open('links.txt', 'r')
# # do something
# file.close()
        
print(links)

count = 0
for link in links:
    contents = {}
    page = urllib.urlopen(link)
    
    data = ""
    for line in page.readlines():
        data = data + line.strip()
        
    json_data = json.loads(data)
    store_in_database(count, json_data)
    count = count + 1
    
