import os

def crawler(fpath,level):
    for n in range(level):
        print('\t',end='')
    print(os.path.basename(fpath))
    contents=[]
    if os.path.isdir(fpath):
        contents=os.listdir(fpath)
    for d in contents:
        crawler(fpath+'/'+d,level+1)


def givepath(pathname):
    crawler(pathname,0)


name=str(input('Enter a directory or path: '))
givepath(name)