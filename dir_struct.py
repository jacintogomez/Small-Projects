import os

def crawler(fpath,ignor,level):
    if level>4:
        return
    stands='|   '*(level-1) if level>=2 else ''
    rakes='|---' if level>0 else ''
    isdir=os.path.isdir(fpath)
    ending='/' if isdir else ''
    print(stands+rakes+os.path.basename(fpath)+ending)
    contents=[]
    if isdir:
        contents=os.listdir(fpath)
    for d in contents:
        if d not in ignor and d[0]!='.':
            crawler(fpath+'/'+d,ignor,level+1)

def givepath(pathname,ignored):
    crawler(pathname,ignored,0)


def main():
    ignored=[
        '.venv',
        'venv',
        'env',
        '__pycache__',
        '.pytest_cache',
        '.mypy_cache',
        'node_modules',
        '.next',
        '.nuxt',
        '.svelt-kit',
        '.turbo',
        '.yarn',
        'jspm_packages',
        'target',
        'build',
        '.gradle',
        '.mvn',
        'out',
        '.idea',
        '.git',
        '.vscode',
        'logs',
        '.DS_Store',
        'Thumbs.db',
        'desktop.ini',
    ]
    name=str(input('Enter a directory or path: '))
    givepath(name,ignored)

main()
