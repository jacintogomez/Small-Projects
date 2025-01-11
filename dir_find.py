import os

def crawler(fpath,sterm,level):
    contents=[]
    if os.path.isdir(fpath):
        contents=os.listdir(fpath)
    for d in contents:
        if sterm in d:
            print(d)
        crawler(fpath+'/'+d,sterm,level+1)

def givepath(pathname,st):
    crawler(pathname,st,0)

name=str(input('Enter a directory or path: '))
searchterm=str(input('Enter a search term: '))
givepath(name,searchterm)
