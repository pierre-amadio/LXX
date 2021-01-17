#!/usr/bin/env python3
"""
https://zetcode.com/python/jinja/
"""
from jinja2 import Template, FileSystemLoader, Environment
file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)
template = env.get_template('book.xml')


testBook={}
testBook['name']="Genesis"
testBook['chapters']=[]

ch1={}
ch1["osisId"]="Gen 1"
ch1["title"]="The creation"
ch1["verses"]=[]
ch1["verses"].append({})
ch1["verses"][0]["osisId"]="Gen 1:1"
ch1["verses"][0]["content"]="in the beginning..."
ch1["verses"].append({})
ch1["verses"][1]["osisId"]="Gen 1:2"
ch1["verses"][1]["content"]="blablabla"

ch2={}
ch2["osisId"]="Gen 2"
#ch2["title"]="The second chapter title"
ch2["verses"]=[]
ch2["verses"].append({})
ch2["verses"][0]["osisId"]="Gen 2:1"
ch2["verses"][0]["content"]="blablabla 21"
ch2["verses"].append({})
ch2["verses"][1]["osisId"]="Gen 2:2"
ch2["verses"][1]["content"]="blablabla 22"


testBook["chapters"].append(ch1)
testBook["chapters"].append(ch2)



output = template.render(book=testBook)
print(output)
