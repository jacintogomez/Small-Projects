def alphabetize_it(filename):
    with open(filename,'r') as file:
        items=[line.strip() for line in file if line.strip()]
    items.sort()
    with open(filename,'w') as file:
        for item in items:
            file.write(item+'\n')

fname=input('Enter filename: ')
alphabetize_it(fname)
print('Alphabetized file',fname)