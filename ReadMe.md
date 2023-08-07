# Instalation

1. cd to your project
2. clone project
3. run `python read filename` 

# How To Use

1. create file with .batman
2. request
3. run `python read filename`

### write your first with batman
<br />
in file, you can add somethin like: link, method
<br />
link: your url
<br />
method: GET
<br />

**You must put a space after the attribute**
<br />
code
<br />

```
link: http://127.0.0.1:8000/
method: GET
```

<br />
-------------------------------------------------
<br />


response like this:
```
res:
-------------------------------------------
================RESPONSE===================
-------------------------------------------
STATUS: 200   
TIME: 0.004538
SIZE: 23

-------------------------------------------
CONTENT: 
{"id":1,"title":"test"}

-------------------------------------------
HEADERS:
['date', 'server', 'content-length', 'content-type']

-------------------------------------------
SESSION & COOKIE:
[]
```
# Feuture
* handle get method
* show response
* response details like: time, size, header, cookie, content and more...
* fast
* remove response after run program(clean interface)

# Version
1.0.0

# Author
sajjad mirave :D