import sys
import requests
import colorama 
import re

# @gloabl
argument = sys.argv
url = ""
method = ""
response = ""
status = 0
response_time = 0
response_size = 0
header = []
sessions = []
newdata =[]

# delete file name from list
del argument[0]

# request to url
def request():
    global response
    global status
    global response_time
    global response_size
    global header
    global sessions
    global res
    if method == "GET":
        res = requests.get(url)
    elif method == "POST":
        # ~ bug
        res = requests.post(url)
    # save response in variable
    response += res.text
    status += res.status_code
    response_time += res.elapsed.total_seconds()
    response_size += len(res.content)
    header += res.headers
    session = requests.Session()
    sessions += session.cookies.get_dict()

def show_response():
    f = open(argument[1],'a')

    # create template for write
    temp = f"""
-------------------------------------------
================RESPONSE===================
-------------------------------------------
STATUS: {status}   
TIME: {response_time}
SIZE: {response_size}

-------------------------------------------
CONTENT: 
{response}

-------------------------------------------
HEADERS:
{header}

-------------------------------------------
SESSION & COOKIE:
{sessions}
    """
    f.write(f"{temp}\n")
    f.close()

def read_write():
    # read file
    global newdata
    f = open(argument[1],"r")
    data = f.read()
    newdata = data.split()


    # write file for response
    for index,item in  enumerate(newdata):
        #@Title delete response from .batman file
        #@Desc delete response and again write response
        if(item == "res:"):
            # find index and deleted
            newContent = re.sub(r'res:.*','res:',data,flags=re.DOTALL)

            # write again content witout response 
            f = open(argument[1],'w')
            f.write(newContent)
            f.close()

        elif(item == "link:"):
            global url
            #next index is url
            url_index = index+1

            # find index in list and pass into the variable
            url += newdata[url_index]
        
        elif(item == "method:"):
            global method
            method_index = index+1
            method += newdata[method_index]

            

# command
for item in argument:
    if(item == "read"):
        read_write()
        # request to server
        request()
        show_response()

