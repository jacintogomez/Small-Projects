import os

def crawler(fpath,ignor,level):
    if level>2:
        return
    for n in range(level):
        if n not in ignor:
            print('\t',end='')
    print(os.path.basename(fpath))
    contents=[]
    if os.path.isdir(fpath):
        contents=os.listdir(fpath)
    for d in contents:
        if d not in ignor and d[0]!='.':
            crawler(fpath+'/'+d,ignor,level+1)

def givepath(pathname,ignored):
    crawler(pathname,ignored,0)


def main():
    ignored=['venv','.DS_Store','node_modules','venv','__pycache__']
    name=str(input('Enter a directory or path: '))
    givepath(name,ignored)

main()
