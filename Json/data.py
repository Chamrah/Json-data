import json
data_open = open("data.json","r")
x = json.loads(data_open.read())
print(x)


data_write ={  
    "langage":"python"}
file = open("data.json","a")
file.write(json.dumps(data_write))
file.close()
